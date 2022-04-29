let s1 =  Number(document.getElementById("score-1").value) +
          Number(document.getElementById("score-2").value) +
          Number(document.getElementById("score-3").value);

let s2 = Number(document.getElementById("score-4").value) +
         Number(document.getElementById("score-5").value) +   
         Number(document.getElementById("score-6").value);

let s3 = Number(document.getElementById("score-7").value) +
         Number(document.getElementById("score-8").value) +
         Number(document.getElementById("score-9").value);

let s4 = Number(document.getElementById("score-10").value) +
         Number(document.getElementById("score-11").value) +
         Number(document.getElementById("score-12").value);

let s5  = Number(document.getElementById("score-13").value) +
          Number(document.getElementById("score-14").value) +
          Number(document.getElementById("score-15").value);
let result = [{ 
        "stress" : 1,
        "score" : s1
        },
        { 
        "stress" : 2,
        "score" : s2
        },
        {
        "stress" : 3,
        "score" : s3
        },
        {
        "stress" : 4,
        "score" : s4
        },
        {
        "stress" : 5,
        "score" : s5
        },
];
// let xhr = new XMLHttpRequest();
// xhr.open("POST", "/insert_score");
// xhr.setRequestHeader("Content-Type", "application/json");
// xhr.send(JSON.stringify(result));
$.ajax({
        type: "POST",
        url: "/insert_score",
        data: JSON.stringify(result),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function(data){
                console.log(data);
                }
        });




