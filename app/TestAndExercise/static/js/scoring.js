

let s1_s =  parseInt(document.getElementById("score-1").value) +
            parseInt(document.getElementById("score-2").value) +
            parseInt(document.getElementById("score-3").value);

let s2_s = parseInt(document.getElementById("score-4").value) +
           parseInt(document.getElementById("score-5").value) +   
           parseInt(document.getElementById("score-6").value);

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




