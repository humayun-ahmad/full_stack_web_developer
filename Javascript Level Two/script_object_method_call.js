var simple ={
  prop: "hello",
  myMethod : function(){
    console.log("The myMethod was called");
  }
}
console.dir(simple);

console.log(simple.myMethod());

var myObj  = {
  name : "rafiq",
  greet : function() {
    console.log("Hello " + this.name);
  }
}

console.log(myObj.greet());
