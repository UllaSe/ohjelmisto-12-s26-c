"use strict";

const student = {
  name: "Joa",
  age: 21,
  courses: ["Python", "Webdev"]
};

console.log("JavaScript object:");
console.log(student);

const jsonText = JSON.stringify(student);

console.log("JSON text:");
console.log(jsonText);

const parsedStudent = JSON.parse(jsonText);

console.log("Parsed back to JavaScript:");
console.log(parsedStudent);
console.log(parsedStudent.name);
