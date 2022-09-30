



function pythagorean(sideA, sideB){
    var answer = Math.sqrt(Math.pow(sideA, 2) + Math.pow(sideB, 2));
    document.getElementById("answerBox").innerHTML = "C = " + answer;
  }
  
function findCircle(radius){
    let answer = 3.14 * (Math.pow(radius,2));
    document.getElementById("answerBox2").innerHTML = "Area = " + answer;
}

function findSphere(radius){
    let actualRadius = Math.pow(radius,3)
    let answer = (4/3)*(3.14)*(actualRadius);
    
    document.getElementById("answerBox3").innerHTML = "Volume = " + answer;
}


