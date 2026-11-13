"use strict";

const form = document.querySelector("#converter");
const temperature = document.querySelector("#temperature");
const direction = document.querySelector("#direction");
const result = document.querySelector("#result");

form.addEventListener("submit", function (event) {
  event.preventDefault();

  const value = parseFloat(temperature.value);
  let converted;

  if (direction.value === "c-to-f") {
    converted = value * 9 / 5 + 32;
    result.innerText = `${value} °C is ${converted.toFixed(1)} °F.`;
    return;
  }

  converted = (value - 32) * 5 / 9;
  result.innerText = `${value} °F is ${converted.toFixed(1)} °C.`;
});
