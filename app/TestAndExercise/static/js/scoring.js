let result = [{ 
        "stress" : 1,
        "score" : document.getElementById("words-1").value +
                  document.getElementById("words-2").value +
                  document.getElementById("words-3").value 
        },
        { 
        "stress" : 2,
        "score" : document.getElementById("words-4").value +
                  document.getElementById("words-5").value +
                  document.getElementById("words-6").value 
        },
        {
        "stress" : 3,
        "score" : document.getElementById("words-7").value +
                  document.getElementById("words-8").value +
                  document.getElementById("words-9").value 
        },
        {
        "stress" : 4,
        "score" : document.getElementById("words-10").value +
                  document.getElementById("words-11").value +
                  document.getElementById("words-12").value 
        },
        {
        "stress" : 5,
        "score" : document.getElementById("words-13").value +
                  document.getElementById("words-14").value +
                  document.getElementById("words-15").value 
        }
];

result.sort(function(a, b) {
        return a.score - b.score;
});
                 
let xhr = new XMLHttpRequest();
xhr.open("POST", "/result");
xhr.setRequestHeader("Content-Type", "application/json");
xhr.send(JSON.stringify(result));




