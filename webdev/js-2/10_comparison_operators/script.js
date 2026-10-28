"use strict";

const first = 10;
const second = 20;
const third = "10";

console.log(first === second);
console.log(first !== second);
console.log(first > second);
console.log(first >= second);
console.log(first < second);
console.log(first <= second);

console.log(first == third); // first.toString() === third.toString()
console.log(first === third);
