"use strict";

const names = ["Joa", "Nea", "Jada", "Jessica"];

for (let i = 0; i < names.length; i++) {
  console.log(`for: ${names[i]}`);
}

for (const name of names) {
  console.log(`for of: ${name}`);
}
