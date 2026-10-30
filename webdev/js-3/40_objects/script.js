"use strict";

// object literal:
const student = {
  firstName: "Joa",
  lastName: "Lampela",
  studentId: "2026420",
  phone: "(+358) 45 6789101",
};

console.log(student);
console.log("[\"firstName\"]:", student["firstName"]);
console.log(".firstName:", student.firstName);
console.log(".phone::", student.phone);

const studentCopy = {...student}; // spread operator => shallow copy
studentCopy.city = "Espoo";
delete studentCopy.phone;
console.log(studentCopy);
