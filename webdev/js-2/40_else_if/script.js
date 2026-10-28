"use strict";

const age = prompt("Enter your age");

if (age >= 65) {
  console.log("You are of retirement age");
} else if (age >= 30) {
  console.log("You are middle aged");
} else if (age >= 18) {
  console.log("You are a young adult");
} else {
  console.log("You are a minor")
}
