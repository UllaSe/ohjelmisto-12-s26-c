"use strict";

const numbers = [420, 67, 1337, 42];
const numbersCopy = [...numbers]; // spread operator => creates a separate (shallow) copy

numbersCopy.sort();
console.log("After sort():", numbersCopy);

numbers.sort((a, b) => a - b); // anonymous (arrow) function
console.log("After sort((a, b) => a - b):", numbers);
