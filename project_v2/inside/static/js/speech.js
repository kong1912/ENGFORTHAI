var textBox = document.querySelector("textarea");
var startBtn = document.querySelector("#start-btn");
var stopBtn = document.querySelector("#stop-btn");

// stores the transcript of speech recognized
var content = "";
// boolean flag
var speechRecognitionIsOn = false;

var speechRecognition = window.webkitSpeechRecognition
// creates an instance of speechRecognition
var recognition = new speechRecognition();
// captures single result each time
recognition.continuous = false

startBtn.addEventListener('click',() => {
    speechRecognitionIsOn = true;
    console.log("voice recognition started");
    recognition.start();
});
stopBtn.addEventListener('click',() => {
    speechRecognitionIsOn = false;
    console.log("voice recognition stopped");
    textBox.value = "";
    recognition.stop();
});

recognition.onstart = () => {
    // clears content (optional)
    if(content.length){ 
        content = '';
    }
}
recognition.onend = () => {
    if(speechRecognitionIsOn){
        recognition.start();
    }
}
recognition.onerror = (event) => {
    // failed to recognize speech
    console.log('Speech recognition error detected: '+event.error);
}
recognition.onresult = (event) => {
    let current = event.resultIndex;
    let transcript = event.results[current][0].transcript;
    content += transcript;
    textBox.value = content;
    console.log(transcript);
}

