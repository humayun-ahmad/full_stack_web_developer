function hello(name1, name2){
  console.log(name1 + name2);
}

function addition(num1, num2){
  console.log(num1 + num2);
}

function helloSomeone(name = "Humayun"){
  console.log("Hello " + name);
}

function formal(name = "someone", title = "general people"){
  return "welcome " + name + " " + title;
}

var v = "global variable";
var stuff = "Global Stuff";

function fun(stuff = "Reassign stuff inside func") {
  console.log(v);
  console.log(stuff);
}

fun();
console.log(stuff);
