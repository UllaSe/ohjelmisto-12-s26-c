"use strict";

let totalJoules = 0; // reassignable variable
const multiplier = 4.1868; // constant variable

const kcal1 = prompt("Give the amount of energy for lunch in kcal.");
const joules1 = multiplier * kcal1;
totalJoules += joules1;

const kcal2 = prompt("Enter the amount of energy for dinner in kcal.");
const joules2 = multiplier * kcal2;
totalJoules += joules2;
console.log(`At breakfast you got ${joules1} kJ and at dinner you got ${joules2} kJ for a total of ${totalJoules} kJ.`);
