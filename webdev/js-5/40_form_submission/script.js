"use strict";

const form = document.querySelector("#form");
const firstName = document.querySelector("input[name=firstName]");
const lastName = document.querySelector("input[name=lastName]");
const greeting = document.querySelector("#greeting");
const result = document.querySelector("#result");

form.addEventListener("submit", function (event) {
  event.preventDefault();

  result.innerText = `${greeting.value}, ${firstName.value} ${lastName.value}!`;

  // Ohjelma voi sittemmin käyttää annettuja arvoja verkkosivun operointiin
  const obj = {
    greeting: greeting.value,
    firstName: firstName.value,
    lastName: lastName.value
  }
  // await sendObject(obj)
});
