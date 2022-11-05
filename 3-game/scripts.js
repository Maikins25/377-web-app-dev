let boardX = [0,0,0,
              0,0,0,
              0,0,0]

let boardO = [0,0,0,
              0,0,0,
              0,0,0]

let player = 1;
    


// This function takes in the square that was clicked and sets the use of
// the square to either x or o depending on the value of the variable player
// It also keeps track of the board by updating the 2 arrays
function putMark(square){
    if(player == 1){
        if(square == 1){
            $("#square1x").attr("visibility","visible");
            boardX[0]=1;
            player = 2;
        }else if(square == 2){
            $("#square2x").attr("visibility","visible");
            boardX[1]=1;
            player = 2;
        }else if(square == 3){
            $("#square3x").attr("visibility","visible");
            boardX[2]=1;
            player = 2;
        }else if(square == 4){
            $("#square4x").attr("visibility","visible");
            boardX[3]=1;
            player = 2;
        }else if(square == 5){
            $("#square5x").attr("visibility","visible");
            boardX[4]=1;
            player = 2;
        }else if(square == 6){
            $("#square6x").attr("visibility","visible");
            boardX[5]=1;
            player = 2;
        }else if(square == 7){
            $("#square7x").attr("visibility","visible");
            boardX[6]=1;
            player = 2;
        }else if(square == 8){
            $("#square8x").attr("visibility","visible");
            boardX[7]=1;
            player = 2;
        }else if(square == 9){
            $("#square9x").attr("visibility","visible");
            boardX[8]=1;
            player = 2;
        }

    }else if(player == 2){
        if(square == 1){
            $("#square1o").attr("visibility","visible");
            boardO[0]=1;
            player = 1;
        }else if(square == 2){
            $("#square2o").attr("visibility","visible");
            boardO[1]=1;
            player = 1;
        }else if(square == 3){
            $("#square3o").attr("visibility","visible");
            boardO[2]=1;
            player = 1;
        }else if(square == 4){
            $("#square4o").attr("visibility","visible");
            boardO[3]=1;
            player = 1;
        }else if(square == 5){
            $("#square5o").attr("visibility","visible");
            boardO[4]=1;
            player = 1;
        }else if(square == 6){
            $("#square6o").attr("visibility","visible");
            boardO[5]=1;
            player = 1;
        }else if(square == 7){
            $("#square7o").attr("visibility","visible");
            boardO[6]=1;
            player = 1;
        }else if(square == 8){
            $("#square8o").attr("visibility","visible");
            boardO[7]=1;
            player = 1;
        }else if(square == 9){
            $("#square9o").attr("visibility","visible");
            boardO[8]=1;
            player = 1;
        }    
    }
    var result = checkWinner();

    if( result == 1){
        console.log("x win")
    }else if(result==2){
        console.log("o win")
    }else{

    }
   
}




    // This function takes in boardX and boardY and either runs the end game
    // function passing in the parameter 1 or 2, or it returns 0 and continues the game
    function checkWinner(){
        console.log("Board X: " + boardX)
        console.log("Board O: " + boardO)

        if(boardX[0] == 1 & boardX[1] == 1 & boardX[2] == 1){
            gameEnd(1);
        }else if(boardX[3] == 1 & boardX[4] == 1 & boardX[5] == 1){
            gameEnd(1);
        }else if(boardX[6] == 1 & boardX[7] == 1 & boardX[8] == 1){
            gameEnd(1);
        }else if(boardX[0] == 1 & boardX[3] == 1 & boardX[6] == 1){
            gameEnd(1);
        }else if(boardX[1] == 1 & boardX[4] == 1 & boardX[7] == 1){
            gameEnd(1);
        }else if(boardX[2] == 1 & boardX[5] == 1 & boardX[8] == 1){
            gameEnd(1);
        }else if(boardX[0] == 1 & boardX[4] == 1 & boardX[8] == 1){
            gameEnd(1);
        }else if(boardX[2] == 1 & boardX[4] == 1 & boardX[6] == 1){
            gameEnd(1);
//------------------------------------------------seperates the two boards

        }else if(boardO[0] == 1 & boardO[1] == 1 & boardO[2] == 1){
            gameEnd(2);
        }else if(boardO[3] == 1 & boardO[4] == 1 & boardO[5] == 1){
            gameEnd(2);
        }else if(boardO[6] == 1 & boardO[7] == 1 & boardO[8] == 1){
            gameEnd(2);
        }else if(boardO[0] == 1 & boardO[3] == 1 & boardO[6] == 1){
            gameEnd(2);
        }else if(boardO[1] == 1 & boardO[4] == 1 & boardO[7] == 1){
            gameEnd(2);
        }else if(boardO[2] == 1 & boardO[5] == 1 & boardO[8] == 1){
            gameEnd(2);
        }else if(boardO[0] == 1 & boardO[4] == 1 & boardO[8] == 1){
            gameEnd(2);
        }else if(boardO[2] == 1 & boardO[4] == 1 & boardO[6] == 1){
            gameEnd(2);
        }else{
            if(checkTie()== 1){
                
            }else{
                return 0;
            }
        }


            
    }


function checkTie(){
    console.log("checkTie is running")
    let totalMarks = 0;
    for(var i=0;i<boardX.length; i++){
        if(boardX[i] == 1){
            totalMarks+=1;
        }
    }
    for(var i=0;i<boardO.length; i++){
        if(boardO[i] == 1){
            totalMarks+=1;
        }
    }
    if(totalMarks == 9){
        gameEnd(0)
    }else{
        return 1;
    }
}

function gameEnd(winner){
    console.log("winner" + winner)
    if(winner == 0){
        $("#gameEnd").html("Tie!");
        
        //edit h1 to say tie
    }else if(winner == 1){
        $("#gameEndUse").attr("href","x");
        $("#gameEnd").html("X wins");
        //edit h1 to say X wins
    }else if(winner == 2){
        $("#gameEndUse").attr("href","o");
        $("#gameEnd").html("O wins!");
        //edit h1 to say O wins
    }
}

function clearBoard(){
    boardX[0] = 0;
    boardX[1] = 0;
    boardX[2] = 0;
    boardX[3] = 0;
    boardX[4] = 0;
    boardX[5] = 0;
    boardX[6] = 0;
    boardX[7] = 0;
    boardX[8] = 0;

    boardO[0] = 0;
    boardO[1] = 0;
    boardO[2] = 0;
    boardO[3] = 0;
    boardO[4] = 0;
    boardO[5] = 0;
    boardO[6] = 0;
    boardO[7] = 0;
    boardO[8] = 0;
    
    player = 1;
    $("#gameEnd").html("");

    $("#square1x").attr("visibility", "hidden");
    $("#square2x").attr("visibility", "hidden");
    $("#square3x").attr("visibility", "hidden");
    $("#square4x").attr("visibility", "hidden");
    $("#square5x").attr("visibility", "hidden");
    $("#square6x").attr("visibility", "hidden");
    $("#square7x").attr("visibility", "hidden");
    $("#square8x").attr("visibility", "hidden");
    $("#square9x").attr("visibility", "hidden");

    $("#square1o").attr("visibility", "hidden");
    $("#square2o").attr("visibility", "hidden");
    $("#square3o").attr("visibility", "hidden");
    $("#square4o").attr("visibility", "hidden");
    $("#square5o").attr("visibility", "hidden");
    $("#square6o").attr("visibility", "hidden");
    $("#square7o").attr("visibility", "hidden");
    $("#square8o").attr("visibility", "hidden");
    $("#square9o").attr("visibility", "hidden");
}
