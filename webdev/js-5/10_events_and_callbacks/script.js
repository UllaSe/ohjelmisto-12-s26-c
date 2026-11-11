"use strict";

const buttons = document.querySelectorAll("button");
const result = document.querySelector("#result");

function handleClick(event) {
  console.log(event);
  console.log(event.currentTarget);
  result.innerText = "Hello " + event.currentTarget.innerText + "!";
}

function printHello(event) {
  console.log("Print Hello!");
}

for (const button of buttons) {
  button.addEventListener("click", handleClick);
}

buttons[0].addEventListener("click", printHello); // vain yhteen nappiin eventin lisääminen
