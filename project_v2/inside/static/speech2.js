attachEvents();

function attachEvents() {
    let workingEls = getWorkingEls();
    workingEls.forEach(attachEvent);
}

function getWorkingEls() {
    return [
        {
            id_start_btn: "#start-btn-1",
            id_output_txta: "#output-textarea-1"
        },
        {
            id_start_btn: "#start-btn-2",
            id_output_txta: "#output-textarea-2"
        },
        {
            id_start_btn: "#start-btn-3",
            id_output_txta: "#output-textarea-3"
        },
    ]
}

function attachEvent(element, index, array) {
    let startBtnEl = document.querySelector(element.id_start_btn);
    let outputTextAreaEl = document.querySelector(element.id_output_txta);

    // new speech recognition object
    let speechRecognition = window.SpeechRecognition || webkitSpeechRecognition;
    let recognition = new speechRecognition();

    // captures single result each time
    recognition.continuous = false
    startBtnEl.disable = true;

    startBtnEl.onclick = function () {
        startBtnEl.disabled = true;
        outputTextAreaEl.value = "";
        recognition.start();
    };

    recognition.onend = function() {
        startBtnEl.disabled = false;
    }

    recognition.onresult = function (event) {
        let current = event.resultIndex;
        outputTextAreaEl.value = `${event.results[current][0].transcript}`;
    }

}
