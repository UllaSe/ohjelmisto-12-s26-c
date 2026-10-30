"use strict";

const quadraticSum = (a, b) => a * a + b * b;

const quadraticSumBlock = (a, b) => {
  const result = a * a + b * b;
  return result;
};

console.log(quadraticSum(2, 3));
console.log(quadraticSumBlock(2, 3));

const object = {}; // initializing empty object
object.quad = (a, b) => a * a + b * b;
console.log(object.quad(2, 3));

object.hello = () => console.log("Hello World!");
object.hello();
console.log(object);
