<!-- <script>
            result = 0; 
            attachEvents();
            function attachEvents() 
            {
                let workingEls = getWorkingEls();
                workingEls.forEach(attachEvent);
            }

            function getWorkingEls() 
            {
                return [
                    {
                        id_start_btn: "#start-btn-{{ loop.index }}",
                        id_output_txta: "#output-textarea-{{ loop.index }}",
                        id_score: "#score-{{ loop.index }}",
                    }
                ]
            }
            function attachEvent(element, index, array) 
            {
                let cnt = 0;
                let result;
                let startBtnEl = document.querySelector(element.id_start_btn);
                let outputTextAreaEl = document.querySelector(element.id_output_txta);
                let scoreTextAreaEl = document.querySelector(element.id_score);
                // new speech recognition object
                let speechRecognition = window.SpeechRecognition || webkitSpeechRecognition;
                let recognition = new speechRecognition();
                let score = 100;
                if (cnt >= 4) {

                    startBtnEl.disabled = true;
                    result = score;
                    scoreTextAreaEl.value = result;
                    
                }
             
                // captures single result each time
                recognition.continuous = false

                startBtnEl.onclick = function () {
                    ++cnt;
                    outputTextAreaEl.value = "";
                    recognition.start();
                    console.log(`cnt =  ${cnt}`);
                };
            
              /*  recognition.onend = function() {
                    startBtnEl.disabled = false;
                } */
            
                recognition.onresult = function (event) 
                {
                    
                    let current = event.resultIndex;
                    outputTextAreaEl.value += `${event.results[current][0].transcript}`; // (${event.results[current][0].confidence})
                    let prob = document.querySelector("#words-{{ loop.index }}").innerHTML;
                    let resultText = document.querySelector("#output-textarea-{{ loop.index }}").value;
                    let result1 = prob.trim();
                    let result2 = resultText.trim();
                    let rLower = result1.toLowerCase();
                    let pLower = result2.toLowerCase();
                    if (!(rLower === pLower))
                    {
                        score -= 25;
                    }
                    else
                    {
                        startBtnEl.disabled = true;
                        result = score;
                        scoreTextAreaEl.value = result;
                    }     
                   
                    if (cnt >= 4) {
                        startBtnEl.disabled = true;
                        result = score;
                        scoreTextAreaEl.value = result;
                    }
                    console.log(`score =  ${score}`);
                    console.log(`result =  ${result}`);

                    let xxx = get_sum();
                    console.log(xxx);
                }
                
                recognition.onnomatch = function() 
                {
                    console.log('Speech not recognized');
                }

            } 
            
            function get_sum() {
                
                let s1_s =  Number(document.getElementById("score-1").value) +
                            Number(document.getElementById("score-2").value) +
                            Number(document.getElementById("score-3").value);
                
                let s2_s = Number(document.getElementById("score-4").value) +
                            Number(document.getElementById("score-5").value) +   
                            Number(document.getElementById("score-6").value);
                
                let s3_s = Number(document.getElementById("score-7").value) +
                            Number(document.getElementById("score-8").value) +
                            Number(document.getElementById("score-9").value);
                
                let s4_s = Number(document.getElementById("score-10").value) +
                            Number(document.getElementById("score-11").value) +
                            Number(document.getElementById("score-12").value);
                
                let s5_s  = Number(document.getElementById("score-13").value) +
                            Number(document.getElementById("score-14").value) +
                            Number(document.getElementById("score-15").value);

                let total = s1_s + s2_s + s3_s + s4_s + s5_s;
                let result = {"s1": s1_s, "s2": s2_s, "s3": s3_s, "s4": s4_s, "s5": s5_s, "total": total};
              return result;                  
            }
            
        </script> -->