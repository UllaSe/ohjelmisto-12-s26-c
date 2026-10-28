"use strict";

let result;

do {
  result = Math.floor(Math.random() * 6) + 1;
  console.log(result);
} while (result < 6);
