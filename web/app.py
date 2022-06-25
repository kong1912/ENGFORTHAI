from app import app,VAR_DIR, LOG_DIR, CACHE_DIR, \
UPLOAD_DIR, ANNOTATIONS_FILE, AUDIO_DIR,MODEL_FILE,ANNOTATIONS_FILE_TEST
import math
import os
import pathlib
import subprocess
import sys
import uuid
import pandas as pd
import torch
import torch.nn.functional as F
import torchaudio
from flask import Flask, request, flash, redirect
from flask import render_template
from torch import nn
from torch.utils.data import Dataset



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


class GowajeeDataset(Dataset):

    def __init__(self, annotations_file, audio_dir):
        self.annotations = pd.read_csv(annotations_file)
        self.audio_dir = audio_dir

    def __len__(self):
        return len(self.annotations)

    def __getitem__(self, index):
        audio_sample_path = self._get_audio_sample_path(index)
        label = self._get_audio_sample_label(index)
        waveform, sr = torchaudio.load(audio_sample_path)
        return waveform, sr, label

    def _get_audio_sample_path(self, index):
        path = os.path.join(self.audio_dir, self.annotations.iloc[
            index, 0])
        return path

    def _get_audio_sample_label(self, index):
        return self.annotations.iloc[index, 1]


gwj = GowajeeDataset(ANNOTATIONS_FILE, AUDIO_DIR)
gwj_test = GowajeeDataset(ANNOTATIONS_FILE_TEST, AUDIO_DIR)
print(f"There are {len(gwj)} samples in the dataset.")
waveform, sample_rate, label = gwj[0]


class M5(nn.Module):
    def __init__(self, n_input=1, n_output=24, stride=16, n_channel=32):
        super().__init__()
        self.conv1 = nn.Conv1d(n_input, n_channel, kernel_size=80, stride=stride)
        self.bn1 = nn.BatchNorm1d(n_channel)
        self.pool1 = nn.MaxPool1d(4)
        self.conv2 = nn.Conv1d(n_channel, n_channel, kernel_size=3)
        self.bn2 = nn.BatchNorm1d(n_channel)
        self.pool2 = nn.MaxPool1d(4)
        self.conv3 = nn.Conv1d(n_channel, 2 * n_channel, kernel_size=3)
        self.bn3 = nn.BatchNorm1d(2 * n_channel)
        self.pool3 = nn.MaxPool1d(4)
        self.conv4 = nn.Conv1d(2 * n_channel, 2 * n_channel, kernel_size=3)
        self.bn4 = nn.BatchNorm1d(2 * n_channel)
        self.pool4 = nn.MaxPool1d(4)
        self.fc1 = nn.Linear(2 * n_channel, n_output)

    def forward(self, x):
        x = self.conv1(x)
        x = F.relu(self.bn1(x))
        x = self.pool1(x)
        x = self.conv2(x)
        x = F.relu(self.bn2(x))
        x = self.pool2(x)
        x = self.conv3(x)
        x = F.relu(self.bn3(x))
        x = self.pool3(x)
        x = self.conv4(x)
        x = F.relu(self.bn4(x))
        x = self.pool4(x)
        x = F.avg_pool1d(x, x.shape[-1])
        x = x.permute(0, 2, 1)
        x = self.fc1(x)
        return F.log_softmax(x, dim=2)


model = torch.load(MODEL_FILE)
labels = sorted(list(set(datapoint[2] for datapoint in gwj)))


def get_likely_index(tensor):
    # find most likely label index for each element in the batch
    return tensor.argmax(dim=-1)


def label_to_index(word):
    # Return the position of the word in labels
    return torch.tensor(labels.index(word))


def index_to_label(index):
    # Return the word corresponding to the index in labels
    # This is the inverse of label_to_index
    return labels[index]

@app.route('/save-record', methods=['POST'])
def save_record():
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
    file_name = str(uuid.uuid4()) + ".wav"
    full_file_name = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
    file.save(full_file_name)
    return '<h1>Success</h1>'


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
            # "-ac", "2",
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
    tensor, predict_score = predict(waveform)

    # return '<h1>Success</h1>'
    # return f"<div>Predicted: {predict(waveform)}</div>"
    return {
        "text": tensor,
        "score": predict_score,
    }


def test1():
    full_file_name = r"D:\lst-dlt\flask-asr\files\f2e5cc25-941a-42c2-9f1d-b3619d69f3e4.webm"
    # full_file_name = r"D:\lst-dlt\flask-asr\files\output.wav"
    # full_file_name = r"D:\lst-dlt\flask-asr\files\recording.wav"
    # full_file_name = r"D:\lst-dlt\flask-asr\files\eighth.aac.wav"
    full_file_name_wav = full_file_name + ".wav"
    # subprocess.run(["ping", "-c", "3", host], shell=False)

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
    tensor, predict_score = predict(waveform)
    return {
        "text": tensor,
        "score": predict_score,
    }

if __name__ == '__main__':
    app.run(debug=True)