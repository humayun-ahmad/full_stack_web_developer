var employee = {
  name : "John Smith",
  job : "Programmer",
  age : 31,
  nameLength : function () {
    console.log("Name length is " + this.name.length);
  },
  pairs : function () {
    alert("Name is " + this.name + ", " + "Job is " + this.job + ", age is " + this.age);
  },
  lastName : function () {
    console.log("The last name is " + this.name);
  }
}
