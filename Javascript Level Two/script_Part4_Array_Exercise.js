var roster = ['rahim', 'karim', 'shafiq'];
var other = prompt("Enter a student name: ");

roster.push(other);
var i = 0;
while(i < roster.length){
  console.log(roster[i]);
  i++;
}
