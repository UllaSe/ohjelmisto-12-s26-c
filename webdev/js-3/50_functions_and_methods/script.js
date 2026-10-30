"use strict";

// function definition:
function greet() {
  console.log("Hello World!");
  return;
}

greet(); // function call

const student = {
  firstName: "Joa",
  lastName: "Lampela",
  credits: 175,
  // anonymous function:
  studiesLeft: function () {
    return 240 - this.credits;
  }
};

console.log(`Student is missing ${student.studiesLeft()} ECTs for graduation.`);

student.greet = greet;
student.greet();
console.log(student);
