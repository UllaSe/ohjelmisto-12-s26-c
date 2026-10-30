"use strict";

const variable1 = 1;

function hello() {
  const variable2 = 2;
  if (variable2 > 0) {
    const variable3 = 3;
    var variable4 = 4;
    console.log("Inside if-block:", variable1, variable2, variable3, variable4);
  }
  console.log("Inside function:", variable1, variable2, variable4); // 3 not accessible in this scope
}

hello();
console.log("In main program:", variable1); // only 1 accessible
