// var x = document.getElementById("moisture1").value;
// var y = document.getElementById("moisture2").value;
//
// //var val1 = giveVal(x);
// //var val2 = giveVal(y);
//
// var randomNumber = Math.floor(Math.random() * 150);
// var randomNumber2 = Math.floor(Math.random() * 30);

var randomNumber = 40;
var randomNumber2 = 110;


function randomWholeNum() {

    // Only change code below this line.

    return Math.random();
}




$(document).ready(function() {

    $('.pour') //Pour Me Another Drink, Bartender!
        .delay(2000)
        .animate({
            height: '360px'
        }, 1500)
        .delay(1600)
        .slideUp(500);



    $('#liquid') // I Said Fill 'Er Up!
        .delay(3400)
        .animate({
            height: randomNumber
        }, 2500);

    $('#liquid2') // I Said Fill 'Er Up!
        .delay(3400)
        .animate({
            height: randomNumber2
        }, 2500);


});


function giveVal(val) {
    if(val>0 && val<20){
        return 20;
    }
    else if(val>21 && val<40){
        return 40;
    }
    else if(val>41 && val<60){
        return 60;
    }
    else if(val>61  && val<80){
        return 80;
    }
    else if(val>81 && val<100){
        return 95;
    }
}