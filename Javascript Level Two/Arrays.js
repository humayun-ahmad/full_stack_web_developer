// array length
var fruits = ['Apple', 'Banana'];
console.log(fruits.length);

//access an array element
var first = fruits[0]
console.log(first);

var last = fruits[1]
console.log(last);

// loop over an Arrays
var i = 0;
console.log("//loop over an array");
fruits.forEach(function (item,index,array) {
  console.log(item,index);
  console.log(i);
  i++;
})

// add to the end of an Arrays and get the length size
var newLength = fruits.push('Orange');
console.log(newLength);
console.log(fruits);

// remove from the end of an array
var last = fruits.pop()
console.log(last); // remove Banana(form the end)
console.log(fruits);

// remove from the front of an array
var first = fruits.shift(); // remove Apple from the fornt
console.log(first);

// add to the front of an array
var newLength = fruits.unshift('Strawberry');
console.log(newLength + " " + fruits);

// find the index of an item in the array
fruits.push('Mango');
console.log(fruits);
var pos = fruits.indexOf('Banana');
console.log("Position of Banana " + pos);


// remove an item by index Position
var removeItem = fruits.splice(2,1);// first parameter is postion and second parameter is  how many item removed form Position
console.log(removeItem);

// Copy an Array
var shallowcopy = fruits.slice(); // this is how to make a Copy
console.log(shallowcopy);
