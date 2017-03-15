var myNumber = 42;
var myName = "Joel";

var tempNum = myNumber;
myNumber = myName;
myName = tempNum;
console.log(myName + "," + myNumber);