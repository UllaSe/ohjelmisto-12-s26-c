"use strict";

let heads = 0;
let tails = 0;

while (heads + tails < 10000) {
  const randomNumber = Math.random();

  if (randomNumber > 0.5) {
    heads++;
  } else {
    tails++;
  }
}

console.log("Heads: " + heads + ", tails: " + tails);
