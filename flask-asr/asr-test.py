"""Copy of Thai speech command recognition with torchaudio

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ensKfWzt6WEvmAZTrtMtyUrX1i5JBkMk
"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import math

"""
Thai Speech Command Recognition with torchaudio
******************************************

"""
import os
import pathlib

# import IPython.display as ipd
import matplotlib.pyplot as plt
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torchaudio
from torch.utils.data import Dataset
from tqdm import tqdm

CORPUS_BASE_DIR: pathlib.Path = pathlib.Path(r"D:\_tp\iSAI-NLP-2021")
# ANNOTATIONS_FILE: pathlib.Path = CORPUS_BASE_DIR / "gwjcommand_train.csv"
# ANNOTATIONS_FILE_TEST: pathlib.Path = CORPUS_BASE_DIR / "gwjcommand_test.csv"
ANNOTATIONS_FILE: pathlib.Path = CORPUS_BASE_DIR / "cb1_train.csv"
ANNOTATIONS_FILE_TEST: pathlib.Path = CORPUS_BASE_DIR / "cb1_test.csv"
AUDIO_DIR: pathlib.Path = CORPUS_BASE_DIR / "wav"

APP_DIR: pathlib.Path = pathlib.Path.cwd()
VAR_DIR: pathlib.Path = APP_DIR / "var"
CACHE_DIR: pathlib.Path = VAR_DIR / "cache"
print(f"APP_DIR = {APP_DIR}")
print(f"VAR_DIR = {VAR_DIR}")
print(f"CACHE_DIR = {CACHE_DIR}")

print(f"ensuring VAR_DIR")
VAR_DIR.mkdir(exist_ok=True)

print(f"ensuring CACHE_DIR")
CACHE_DIR.mkdir(exist_ok=True)

MODEL_FILE: pathlib.Path = CACHE_DIR / "model.pickle"

if not MODEL_FILE.exists():
    print(f"model not found")
    exit(2)

"""Let’s check if a CUDA GPU is available and select our device. Running
the network on a GPU will greatly decrease the training/testing runtime.



"""

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device)

"""Importing the Dataset
---------------------

Gowajee V0.9.2 (downloaded 27/Jul/2021) 
from

https://github.com/ekapolc/gowajee_corpus



"""


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


# ANNOTATIONS_FILE = "/content/drive/MyDrive/iSAI-NLP/gwjcommand_train.csv"
# ANNOTATIONS_FILE_TEST  = "/content/drive/MyDrive/iSAI-NLP/gwjcommand_test.csv"
# AUDIO_DIR = "/content/drive/MyDrive/iSAI-NLP/wav"
gwj = GowajeeDataset(ANNOTATIONS_FILE, AUDIO_DIR)
gwj_test = GowajeeDataset(ANNOTATIONS_FILE_TEST, AUDIO_DIR)
print(f"There are {len(gwj)} samples in the dataset.")
waveform, sample_rate, label = gwj[0]

"""A data point in the SPEECHCOMMANDS dataset is a tuple made of a waveform
(the audio signal), the sample rate, the utterance (label), the ID of
the speaker, the number of the utterance.



"""

print("Shape of waveform: {}".format(waveform.size()))
print("Sample rate of waveform: {}".format(sample_rate))

plt.plot(waveform.t().numpy())
"""Let’s find the list of labels available in the dataset.



"""

labels = sorted(list(set(datapoint[2] for datapoint in gwj)))

"""Formatting the Data
-------------------

This is a good place to apply transformations to the data. For the
waveform, we downsample the audio for faster processing without losing
too much of the classification power.

We don’t need to apply other transformations here. It is common for some
datasets though to have to reduce the number of channels (say from
stereo to mono) by either taking the mean along the channel dimension,
or simply keeping only one of the channels. Since SpeechCommands uses a
single channel for audio, this is not needed here.



"""

new_sample_rate = 8000
transform = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=new_sample_rate)
transformed = transform(waveform)

# ipd.Audio(transformed.numpy(), rate=new_sample_rate)

"""We are encoding each word using its index in the list of labels.



"""


def label_to_index(word):
    # Return the position of the word in labels
    return torch.tensor(labels.index(word))


def index_to_label(index):
    # Return the word corresponding to the index in labels
    # This is the inverse of label_to_index
    return labels[index]


# word_start = "ปิดโปรแกรม"
# index = label_to_index(word_start)
# word_recovered = index_to_label(index)
#
# print(word_start, "-->", index, "-->", word_recovered)


def pad_sequence(batch):
    # Make all tensor in a batch the same length by padding with zeros
    batch = [item.t() for item in batch]
    batch = torch.nn.utils.rnn.pad_sequence(batch, batch_first=True, padding_value=0.)
    return batch.permute(0, 2, 1)


def collate_fn(batch):
    # A data tuple has the form:
    # waveform, sample_rate, label, speaker_id, utterance_number

    tensors, targets = [], []

    # Gather in lists, and encode labels as indices
    for waveform, _, label, *_ in batch:
        tensors += [waveform]
        targets += [label_to_index(label)]

    # Group the list of tensors into a batched tensor
    tensors = pad_sequence(tensors)
    targets = torch.stack(targets)

    return tensors, targets


batch_size = 5

if device == "cuda":
    num_workers = 1
    pin_memory = True
else:
    num_workers = 0
    pin_memory = False


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


def get_likely_index(tensor):
    # find most likely label index for each element in the batch
    return tensor.argmax(dim=-1)


def predict(tensor):
    # Use the model to predict the label of the waveform
    tensor = tensor.to(device)
    tensor = transform(tensor)
    tensor = model(tensor.unsqueeze(0))
    tensor_index = get_likely_index(tensor)
    predict_index = tensor_index.squeeze()

    tensor_list = tensor[0][0].tolist()
    predict_log_score = tensor_list[tensor_index[0].item()]
    predict_score = math.exp(predict_log_score)
    # print(predict_score)

    tensor = index_to_label(predict_index)
    # tensor = index_to_label(tensor.squeeze())
    return (tensor, predict_score)


def load_audio():
    # TEST_FILE: pathlib.Path = CORPUS_BASE_DIR / "wav/2017/M0000000002_0041.wav"
    TEST_FILE: pathlib.Path = AUDIO_DIR / "1) -ð- - -θ- - -tθ-/-ð-/AJ.Aom(เเนน)/Smooth .aac.wav"
    print(TEST_FILE)

    return torchaudio.load(str(TEST_FILE))


# waveform, sample_rate = record()
waveform, sample_rate = load_audio()
print(f"Predicted: { predict(waveform) }.")
