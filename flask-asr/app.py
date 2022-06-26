import math
import os
import pathlib
import subprocess
import sys
import uuid
import logging

import pandas as pd
import torch
import torch.nn.functional as F
import torchaudio
from flask import Flask, request, flash, redirect, jsonify
from flask import render_template
from torch import nn
from torch.utils.data import Dataset

from asr.e2e_asr import *

# var
APP_DIR: pathlib.Path = pathlib.Path.cwd()
VAR_DIR: pathlib.Path = APP_DIR / "var"
LOG_DIR: pathlib.Path = VAR_DIR / "log"
UPLOAD_DIR: pathlib.Path = VAR_DIR / "upload"
CACHE_DIR: pathlib.Path = VAR_DIR / "cache"

LOG_FILE: pathlib.Path = LOG_DIR / "flask_asr.log"


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
CORPUS_BASE_DIR: pathlib.Path = pathlib.Path(r"D:\_tp\iSAI-NLP-2021")

END_TO_END_SETTINGS: (EndToEndSetting,) = (
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
END_TO_END_ASRS: [EndToEndASR] = []
for s in END_TO_END_SETTINGS:
    asr = EndToEndASR(s)
    END_TO_END_ASRS.append(asr)

# flask
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = str(UPLOAD_DIR)


@app.route('/')
def root_index():  # put application's code here
    return render_template(
        'index.html.jinja2',
    )


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

    asr_results: list = []
    for asr in END_TO_END_ASRS:
        tensor, predict_score = asr.predict(waveform)
        asr_results.append({
            "text": tensor,
            "score": predict_score,
        })

    return jsonify(asr_results)


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
    # logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG)
    # logging.debug("debug")
    # logging.info("info")
    # logging.warning("warning")

    # app.run()
    app.run(debug=True)
    # print(test2())
