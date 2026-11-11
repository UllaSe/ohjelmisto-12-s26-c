"use strict";

const names = ["Joa", "Nea", "Jada", "Kastanja"];
const target = document.querySelector("#target");

for (const name of names) {
  const item = document.createElement("li");
  item.innerText = name;
  item.title = "Student name: " + name;
  target.appendChild(item);
}

target.classList.add("name-list");
const items = document.querySelectorAll("#target li"); // multiple selectors
items[0].classList.add("highlight");
