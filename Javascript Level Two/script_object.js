var carInfo = {make: "toyota",year:1999, model:"Camry"};
console.dir(carInfo);
console.log(carInfo);
console.log(carInfo['make']);

var myNewO = {a:'hello',b:[1,2,3],c:{inside:['a','b']}};

//travel every element
console.log(myNewO['c']['inside'][1]);

// key traversal
console.log("\nKey traversal:");
for (key in carInfo){
  console.log(key);
}

// key and value traversal
console.log("\nkey and value traversal:");
for(key in carInfo){
  console.log(key + ": " + carInfo[key]);
}
