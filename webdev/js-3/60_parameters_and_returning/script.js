"use strict";

function info(name, credits) {
  console.log(`${name} has ${credits} ECTs.`);
  // return can be omitted => function returns undefined when it runs out of scope
}

info("Joa", 175);
console.log(info("Jada", 240)); // prints "undefined"

function mathOperation(first, second) {
  const result = first * first + second * second;
  return result;
}

const num1 = 2;
const num2 = 3;
const result = mathOperation(num1, num2);
console.log(`The result is ${result}`);
