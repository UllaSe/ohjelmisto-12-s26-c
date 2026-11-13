"use strict";

const trigger = document.querySelector("#trigger");
const result = document.querySelector("#result");

trigger.addEventListener("mouseenter", () => {
  result.innerText = "The mouse entered the element.";
  result.classList.add("active");
});

trigger.addEventListener("mouseleave", function () {
  result.innerText = "The mouse left the element.";
  result.classList.remove("active");
});
