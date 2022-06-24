import json
import os
import math
import pathlib
import subprocess
import sys
import uuid
import pandas as pd
import torch
import torch.nn.functional as F
import torchaudio
from torch import nn
from torch.utils.data import Dataset
from flask import Blueprint, redirect, url_for, render_template, jsonify, request, session, flash
from app import conn, cursor, cursor_dict, app
from ..user import login_required

# CORPUS_BASE_DIR: pathlib.Path = pathlib.Path(r"E:\SciUsProject_ENGFORTHAI\iSAI-NLP-2021")
# ANNOTATIONS_FILE: pathlib.Path = CORPUS_BASE_DIR / "cb1_train.csv"
# ANNOTATIONS_FILE_TEST: pathlib.Path = CORPUS_BASE_DIR / "cb1_test.csv"
# AUDIO_DIR: pathlib.Path = CORPUS_BASE_DIR / "wav"
# CORPUS_BASE_DIR: pathlib.Path = pathlib.Path(r"E:\SciUsProject_ENGFORTHAI\iSAI-NLP-2021")
# ANNOTATIONS_FILE: pathlib.Path = pathlib.Path(r"E:\SciUsProject_ENGFORTHAI\iSAI-NLP-2021\cb1_train.csv")
# ANNOTATIONS_FILE_TEST: pathlib.Path = pathlib.Path(r"E:\SciUsProject_ENGFORTHAI\iSAI-NLP-2021\cb1_train.csv")
# AUDIO_DIR: pathlib.Path = pathlib.Path(r"E:\SciUsProject_ENGFORTHAI\iSAI-NLP-2021\Word level - Copy")

# APP_DIR: pathlib.Path = pathlib.Path.cwd()
# VAR_DIR: pathlib.Path = APP_DIR / "var"
# LOG_DIR: pathlib.Path = VAR_DIR / "log"
# UPLOAD_DIR: pathlib.Path = VAR_DIR / "upload"
# CACHE_DIR: pathlib.Path = VAR_DIR / "cache"
# MODEL_FILE: pathlib.Path = CACHE_DIR / "model.pickle"


# def ensure_folder(path: pathlib.Path, path_name: str = "") -> None:
#     try:
#         path.mkdir(parents=True, exist_ok=False)
#     except FileExistsError:
#         print(f"{path_name}folder is already there: {path}")
#     else:
#         print(f"{path_name}folder was created: {path}")


# def ensure_folders() -> None:
#     ensure_folder(VAR_DIR, "Generated files (cache, logs, etc.) ")
#     ensure_folder(LOG_DIR, "Logging ")
#     ensure_folder(CACHE_DIR, "Cache ")
#     ensure_folder(UPLOAD_DIR, "Upload ")


# ensure_folders()


# class GowajeeDataset(Dataset):

#     def __init__(self, annotations_file, audio_dir):
#         self.annotations = pd.read_csv(annotations_file)
#         self.audio_dir = audio_dir

#     def __len__(self):
#         return len(self.annotations)

#     def __getitem__(self, index):
#         audio_sample_path = self._get_audio_sample_path(index)
#         label = self._get_audio_sample_label(index)
#         waveform, sr = torchaudio.load(audio_sample_path)
#         return waveform, sr, label

#     def _get_audio_sample_path(self, index):
#         path = os.path.join(self.audio_dir, self.annotations.iloc[
#             index, 0])
#         return path

#     def _get_audio_sample_label(self, index):
#         return self.annotations.iloc[index, 1]


# gwj = GowajeeDataset(ANNOTATIONS_FILE, AUDIO_DIR)
# gwj_test = GowajeeDataset(ANNOTATIONS_FILE_TEST, AUDIO_DIR)
# print(f"There are {len(gwj)} samples in the dataset.")
# waveform, sample_rate, label = gwj[0]


# class M5(nn.Module):
#     def __init__(self, n_input=1, n_output=24, stride=16, n_channel=32):
#         super().__init__()
#         self.conv1 = nn.Conv1d(n_input, n_channel, kernel_size=80, stride=stride)
#         self.bn1 = nn.BatchNorm1d(n_channel)
#         self.pool1 = nn.MaxPool1d(4)
#         self.conv2 = nn.Conv1d(n_channel, n_channel, kernel_size=3)
#         self.bn2 = nn.BatchNorm1d(n_channel)
#         self.pool2 = nn.MaxPool1d(4)
#         self.conv3 = nn.Conv1d(n_channel, 2 * n_channel, kernel_size=3)
#         self.bn3 = nn.BatchNorm1d(2 * n_channel)
#         self.pool3 = nn.MaxPool1d(4)
#         self.conv4 = nn.Conv1d(2 * n_channel, 2 * n_channel, kernel_size=3)
#         self.bn4 = nn.BatchNorm1d(2 * n_channel)
#         self.pool4 = nn.MaxPool1d(4)
#         self.fc1 = nn.Linear(2 * n_channel, n_output)

#     def forward(self, x):
#         x = self.conv1(x)
#         x = F.relu(self.bn1(x))
#         x = self.pool1(x)
#         x = self.conv2(x)
#         x = F.relu(self.bn2(x))
#         x = self.pool2(x)
#         x = self.conv3(x)
#         x = F.relu(self.bn3(x))
#         x = self.pool3(x)
#         x = self.conv4(x)
#         x = F.relu(self.bn4(x))
#         x = self.pool4(x)
#         x = F.avg_pool1d(x, x.shape[-1])
#         x = x.permute(0, 2, 1)
#         x = self.fc1(x)
#         return F.log_softmax(x, dim=2)


# model = torch.load(MODEL_FILE)
# labels = sorted(list(set(datapoint[2] for datapoint in gwj)))


# def get_likely_index(tensor):
#     # find most likely label index for each element in the batch
#     return tensor.argmax(dim=-1)


# def label_to_index(word):
#     # Return the position of the word in labels
#     return torch.tensor(labels.index(word))


# def index_to_label(index):
#     # Return the word corresponding to the index in labels
#     # This is the inverse of label_to_index
#     return labels[index]

test_bp = Blueprint('test', __name__,
                    template_folder='templates',
                    static_folder='static', 
                    static_url_path='/TestAndExercise/static')


@test_bp.route('/exercise_lesson1',methods=['GET', 'POST'])
@login_required
def exercise_lesson1():
    cursor.execute("SELECT word FROM word_list WHERE lesson = 1")
    words = cursor.fetchall()
    return render_template('exercise_lesson1.html.jinja', words=words)
    
@test_bp.route('/exercise_lesson2')
@login_required
def exercise_lesson2():
    cursor.execute("SELECT word FROM word_list WHERE lesson = 2")
    words = cursor.fetchall()

    return render_template('exercise_lesson2.html.jinja',words=words)
  
@test_bp.route('/exercise_lesson3')
@login_required
def exercise_lesson3():

    cursor.execute("SELECT word FROM word_list WHERE lesson = 3")
    words = cursor.fetchall()

    return render_template('exercise_lesson3.html.jinja',words=words)


@test_bp.route('/exercise_lesson4')
@login_required
def exercise_lesson4():
    cursor.execute("SELECT word FROM word_list WHERE lesson = 4")
    words = cursor.fetchall()
    
    return render_template('exercise_lesson4.html.jinja',words=words)
    
@test_bp.route('/exercise_lesson5')
@login_required
def exercise_lesson5():
    cursor.execute("SELECT word FROM word_list WHERE lesson = 5")
    words = cursor.fetchall()

    return render_template('exercise_lesson5.html.jinja',words=words)
     
@test_bp.route('/pre-test')
def pretest():
    cursor.execute("SELECT word FROM word_list WHERE lesson = 1")
    words = cursor.fetchall()

    return render_template('pretest.html.jinja',words=words)

@test_bp.route('/post-test')
def postteset():

    return render_template('posttest.html.jinja')

@test_bp.route('/insert_score',methods=['POST'])
def insert_score():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        cursor.execute(f"INSERT INTO score (s1_s,s2_s,s3_s,s4_s,s5_s) \
                         VALUES ({data[0].score},{data[1].score},{data[2].score},{data[3].score},{data[4].score})")
        conn.commit()
        return jsonify({})

@test_bp.route('/result')
def result():
    cursor.execute("SELECT pre_s FROM score WHERE u_id = %s", (session['u_id']))
    pre_s = cursor.fetchone()
    cursor_dict.execute("SELECT s1_s,s2_s,s3_s,s4_s,s5_s FROM score WHERE u_id = %s", (session['u_id']))
    stress = cursor_dict.fetchone()
    print(stress)
    # sort stress ascending
    stress = sorted(stress, key=lambda x: x[1:])
    print(stress)
    return render_template('result.html.jinja',stress=stress,pre_s=pre_s)
