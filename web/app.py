from cgitb import text
import math
import os
import pathlib
import subprocess
import sys
import uuid
import logging
from colorama import Cursor

import pandas as pd
import torch
import torch.nn.functional as F
import torchaudio
from flask import Flask, request, flash, redirect, jsonify, session
from flask import render_template
from torch import nn
from torch.utils.data import Dataset
from app import app, cursor, cursor_dict, conn
from asr.e2e_asr import *
import speech_recognition as sr


VAR_DIR: pathlib.Path = pathlib.Path(r"E:\SciUsProject_ENGFORTHAI\web\var")
LOG_DIR: pathlib.Path = VAR_DIR / "log"
UPLOAD_DIR: pathlib.Path = VAR_DIR / "upload"
CACHE_DIR: pathlib.Path = VAR_DIR / "cache"

# LOG_FILE: pathlib.Path = LOG_DIR / "flask_asr.log"


def ensure_folder(path: pathlib.Path, path_name: str = "") -> None:
    try:
        path.mkdir(parents=True, exist_ok=False)
    except FileExistsError:
        print(f"{path_name}folder is already there: {path}")
    else:
        print(f"{path_name}folder was created: {path}")


def ensure_folders() -> None:
    ensure_folder(VAR_DIR, "Generated files (cache, logs, etc.) ")
    ensure_folder(LOG_DIR, "Logging ")
    ensure_folder(CACHE_DIR, "Cache ")
    ensure_folder(UPLOAD_DIR, "Upload ")


ensure_folders()

# E2E_ASR
CORPUS_BASE_DIR: pathlib.Path = pathlib.Path(r"E:\SciUsProject_ENGFORTHAI\asr-data")

END_TO_END_SETTINGS: (EndToEndSetting) = (
    EndToEndSetting(
        annotations_file_train=CORPUS_BASE_DIR / "cb1_clean1_train.csv",
        annotations_file_test=CORPUS_BASE_DIR / "cb1_clean1_test.csv",
        model_file=CACHE_DIR / "cb1_clean1_model.pickle",
        audio_dir=CORPUS_BASE_DIR / "wav",
    ),
    EndToEndSetting( 
        annotations_file_train=CORPUS_BASE_DIR / "cb2_clean1_train.csv",
        annotations_file_test=CORPUS_BASE_DIR / "cb2_clean1_test.csv",
        model_file=CACHE_DIR / "cb2_clean1_model.pickle",
        audio_dir=CORPUS_BASE_DIR / "wav",
    ),
    EndToEndSetting(
        annotations_file_train=CORPUS_BASE_DIR / "cb3_clean1_train.csv",
        annotations_file_test=CORPUS_BASE_DIR / "cb3_clean1_test.csv",
        model_file=CACHE_DIR / "cb3_clean1_model.pickle",
        audio_dir=CORPUS_BASE_DIR / "wav",
    ),
    EndToEndSetting(
        annotations_file_train=CORPUS_BASE_DIR / "cb4_clean1_train.csv",
        annotations_file_test=CORPUS_BASE_DIR / "cb4_clean1_test.csv",
        model_file=CACHE_DIR / "cb4_clean1_model.pickle",
        audio_dir=CORPUS_BASE_DIR / "wav",
    ),
    EndToEndSetting(
        annotations_file_train=CORPUS_BASE_DIR / "cb5_clean1_train.csv",
        annotations_file_test=CORPUS_BASE_DIR / "cb5_clean1_test.csv",
        model_file=CACHE_DIR / "cb5_clean1_model.pickle",
        audio_dir=CORPUS_BASE_DIR / "wav",
    ),
)

# Tuple from generator
# END_TO_END_ASRS: [EndToEndASR] = [EndToEndASR(e) for e in END_TO_END_SETTINGS]
END_TO_END_ASRS: EndToEndASR = []
for s in END_TO_END_SETTINGS:
    asr = EndToEndASR(s)
    END_TO_END_ASRS.append(asr)



def predict(tensor):
    # Use the model to predict the label of the waveform
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    tensor = tensor.to(device)

    new_sample_rate = 8000
    transform = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=new_sample_rate)

    tensor = transform(tensor)
    tensor = model(tensor.unsqueeze(0))
    # tensor = model(tensor.unsqueeze(1))
    tensor_index = get_likely_index(tensor)
    predict_index = tensor_index.squeeze()

    tensor_list = tensor[0][0].tolist()
    predict_log_score = tensor_list[tensor_index[0].item()]
    predict_score = math.exp(predict_log_score)
    # print(predict_score)

    tensor = index_to_label(predict_index)
    # tensor = index_to_label(tensor.squeeze())
    return (tensor, predict_score)
    
@app.route('/asr', methods=['POST'])
def asr():
    # check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['file']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    # file.text
    # webm/opus
    file_name = str(uuid.uuid4()) + ".webm"
    full_file_name = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
    file.save(full_file_name)
    print(full_file_name)

    full_file_name_wav = full_file_name + ".wav"
    if sys.platform.startswith('win32'):
        ffmpeg_cmd = [
            "wsl",
            "ffmpeg",
            "-y",
            "-i", f'`wslpath -a "{full_file_name}"`',
            "-vn",
            "-ac", "2",
            f'`wslpath -a "{full_file_name_wav}"`',
        ]
    else:
        ffmpeg_cmd = [
            "ffmpeg",
            "-y",
            "-i", full_file_name,
            "-vn",
            "-ac", "2",
            full_file_name_wav,
        ]

    print(ffmpeg_cmd)
    try:
        # pass
        subprocess.run(ffmpeg_cmd, check=True)
    except subprocess.CalledProcessError as e:
        print("ffmpeg execution failed: ", e)

    waveform, sample_rate = torchaudio.load(full_file_name_wav)
    
    word = request.form['word']
    print(f"word={word}")
    
    cursor.execute(f"SELECT lesson FROM word_list WHERE word = '{word}' ")
    level = cursor.fetchone()
    level = int(level[0])

    #google asr
    # Create an instance of the Recognizer class
    recognizer = sr.Recognizer()
    # Set the energy threshold
    recognizer.energy_threshold = 300
    # Convert audio to AudioFile
    clean_support_call = sr.AudioFile(f"{full_file_name_wav}")
    # Convert AudioFile to AudioData
    with clean_support_call as source:
        clean_support_call_audio = recognizer.record(source)
    # Transcribe AudioData to text
    google_text = recognizer.recognize_google(clean_support_call_audio,
                                   language="en-US")
    print(f"google text = {google_text}")
    # google asr end
    
    # asr predict
    stress = {1:"/ð/ - /θ/ - /tθ/", 2: "/ʒ/ - /ʃ/", 3: "/dʒ/ - /tʃ/", 4: "/z/ - /s/", 5: "/b/ - /p/"}
    asr_results: list = []
    if word == google_text:
        cursor.execute(f"SELECT s{level}_s from score WHERE u_id = {session['u_id']} ")
        old_s = cursor.fetchone()
        old_s = old_s[0]
        print(f"old_s = {old_s}")
        new_s = 1 + old_s
        print(f"new_s = {new_s}")
        cursor.execute(f"UPDATE score SET s{level}_s = {new_s}  WHERE u_id = {session['u_id']}")
        conn.commit()

        #insert to asr table
        cursor.execute(f"INSERT INTO asr (u_id,word,google_text,score) VALUES({int(session['u_id'])},'{word}','{google_text}',1)")
        conn.commit()
        return jsonify("You said it right! Your score is increased by 1 point.")

    for asr in END_TO_END_ASRS:
        tensor, predict_score = asr.predict(waveform)
        asr_results.append({
            "text": tensor,
            "score": predict_score,
        })
    print(f"asr_results={asr_results}")
    
    # if asr can recognize the word
    for asr_result in asr_results:
        if word == asr_result['text']:
            cursor.execute(f"INSERT INTO asr (u_id,word,google_text,model_phoneme,model_word,model_prob,score) VALUES({int(session['u_id'])},'{word}','{google_text}',{level},'{asr_result['text']}',{asr_result['score']},0)")
            conn.commit()
            return jsonify(f"You said it wrong. You have problem with {stress[level]}. Your score is not changed.")
    
    # if asr can't recognize the word
    asr_results.sort(key=lambda x: x['score'], reverse=True)
    print(f"asr_results={asr_results}")
    asr_text = asr_results[0]['text']
    cursor.execute(f"SELECT lesson FROM word_list WHERE word = '{asr_text}' ")
    asr_level = cursor.fetchone()
    asr_level = int(asr_level[0])
    cursor.execute(f"INSERT INTO asr (u_id,word,google_text,model_phoneme,model_word,model_prob,score) VALUES({int(session['u_id'])},'{word}','{google_text}',{asr_level},'{asr_text}',{asr_results[0]['score']},0)")
    conn.commit()
    return jsonify(f"You said it wrong.You have problem with {stress[asr_level]} Your score is not changed.")


def test1():
    full_file_name = str(UPLOAD_DIR / "95d7f1f6-2bde-40e8-805c-b6d68e41190c.webm")
    full_file_name_wav = str(full_file_name) + ".wav"

    if sys.platform.startswith('win32'):
        ffmpeg_cmd = [
            "wsl",
            "ffmpeg",
            "-y",
            "-i", f'`wslpath -a "{full_file_name}"`',
            "-vn",
            "-ac", "2",
            f'`wslpath -a "{full_file_name_wav}"`',
        ]
    else:
        ffmpeg_cmd = [
            "ffmpeg",
            "-y",
            "-i", full_file_name,
            "-vn",
            "-ac", "2",
            full_file_name_wav,
        ]

    print(ffmpeg_cmd)
    try:
        # pass
        subprocess.run(ffmpeg_cmd, check=True)
    except subprocess.CalledProcessError as e:
        print("ffmpeg execution failed: ", e)

    asr: EndToEndASR = EndToEndASR(EndToEndSetting(
        audio_dir=APP_DIR,
        model_file=CACHE_DIR / "model.pickle",
        annotations_file_train=CORPUS_BASE_DIR / "cb1_train.csv",
        annotations_file_test=CORPUS_BASE_DIR / "cb1_test.csv",
    ))

    waveform, sample_rate = torchaudio.load(full_file_name_wav)
    tensor, predict_score = asr.predict(waveform)
    return {
        "text": tensor,
        "score": predict_score,
    }


def test2():
    full_file_name = str(UPLOAD_DIR / "95d7f1f6-2bde-40e8-805c-b6d68e41190c.webm")
    full_file_name_wav = str(full_file_name) + ".wav"

    if sys.platform.startswith('win32'):
        ffmpeg_cmd = [
            "wsl",
            "ffmpeg",
            "-y",
            "-i", f'`wslpath -a "{full_file_name}"`',
            "-vn",
            "-ac", "2",
            f'`wslpath -a "{full_file_name_wav}"`',
        ]
    else:
        ffmpeg_cmd = [
            "ffmpeg",
            "-y",
            "-i", full_file_name,
            "-vn",
            "-ac", "2",
            full_file_name_wav,
        ]

    print(ffmpeg_cmd)
    try:
        # pass
        subprocess.run(ffmpeg_cmd, check=True)
    except subprocess.CalledProcessError as e:
        print("ffmpeg execution failed: ", e)

    asr: EndToEndASR = END_TO_END_ASRS[0]

    waveform, sample_rate = torchaudio.load(full_file_name_wav)
    tensor, predict_score = asr.predict(waveform)
    return {
        "text": tensor,
        "score": predict_score,
    }

if __name__ == '__main__':
    app.run(debug=True)