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