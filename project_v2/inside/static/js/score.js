function sendData() {
    let score = document.getElementById("score").innerHTML;
    const URL = '/pretest';
    const xhr = new XMLHttpRequest();
    score = JSON.stringify(score);
    xhr.open('POST', URL);
    xhr.send(score);

}