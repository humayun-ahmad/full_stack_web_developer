var hot = false
var temp = 10

// if-else if-else condition

if(temp > 0 && temp < 25){
  console.log("temparature is very cold");
}else if(temp > 25 && temp < 35){
  console.log("It's day pretty good");
}else{
  console.log("It's very hot today");
}

// compare
console.log("\n\n\n\nCompare:\n");
if('2' === 2){
  console.log("that's not true");
}else if(2 === 2){
  console.log("that's true");
}

if(2 == 2)

// while loop

var x = 0;
while(x < 5){
  console.log("x is currently: " + x);
  console.log("x is still less then 5, adding 1 to x");
  x = x + 1;
  if(x == 3){
    break;
  }
}



/*
For loop:

javascript has three types of For Loops:
  1. For loops through a nubmber of times
  2. For/In - loops through a JS object
  3. For/of - used with arrays
*/


for (var i = 0; i < 5; i++){
  console.log("Number is " + i);
}


var word = "ABCDEFGHIJK"

for (var i = 0; i < word.length; i++){
  console.log(word[i]);
}
