"use strict";

function grow(array) {
  for (let i = 0; i < array.length; i++) {
    array[i]++;
  }
  return;
}

const numbers = [1, 2, 3];
console.log("Before:", [...numbers]);

grow(numbers);
console.log("After:", numbers);

function squares(amount) {
  const squares = [];
  for (let i = 1; i <= amount; i++) {
    squares.push(i * i);
  }
  return squares;
}

const numbers2 = squares(10);
console.log(numbers2);
