
    attachEvents();

function attachEvents() {
    let workingEls = getWorkingEls();
    workingEls.forEach(attachEvent);
}

function getWorkingEls() {
    return [
        {
            id_start_btn: "#start-btn-{{ loop.index }}",
            id_output_txta: "#output-textarea-{{ loop.index }}",
            id_data: "#words-{{ loop.index }}"
        }
        
    ]
}

function attachEvent(element, index, array) {
    let startBtnEl = document.querySelector(element.id_start_btn);
    let outputTextAreaEl = document.querySelector(element.id_output_txta);
    let pro = document.querySelector(element.id_data);
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
        let prob = document.querySelector("#words-{{ loop.index }}").innerHTML;
        let resultText = document.querySelector("#output-textarea-{{ loop.index }}").value;
        outputTextAreaEl.value = resultText;
        let result1 = prob.trim();
        let result2 = resultText.trim();
        var rLower = result1.toLowerCase();
        var pLower = result2.toLowerCase();
        if ( !(rLower.localeCompare(pLower))){

        	let score = document.querySelector("#score");
        
            i += 1;
            score.value = i;
        
			}
        }
    }

