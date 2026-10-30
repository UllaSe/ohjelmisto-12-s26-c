"use strict";

const names = ["Joa", "Nea", "Jada", "Jessica"];
console.log("Original array:", names.join(", "));

names.push("Kastanja");
console.log("After push():", names.join(", "));
console.log("Includes \"Kastanja\":", names.includes("Kastanja"));

console.log("pop() return value:", names.pop());
console.log("After pop():", names.join(", "));

console.log("shift() return value:", names.shift());
console.log("After shift():", names.join(", "));

console.log("Includes \"Jada\":", names.includes("Jada"));
console.log("Includes \"Joa\":", names.includes("Joa"));

names.reverse();
console.log("Reversed array:", names.join(", "));

names.sort();
console.log("Sorted array:", names.join(", "));
