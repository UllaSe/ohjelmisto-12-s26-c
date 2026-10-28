"use strict";

const name = "Joa";
console.log(typeof name);

const age = 28;
console.log(age, typeof age);

const ageString = age.toString();
console.log(ageString, typeof ageString);

const ageString2 = "23";
const ageInteger = parseInt(ageString2);
console.log(ageInteger, typeof ageInteger);

const floatString = "3.14";
const floatNumber = parseFloat(floatString);
console.log(floatNumber);

const floatStringUnaryPlus = +floatString;
console.log(floatStringUnaryPlus);
