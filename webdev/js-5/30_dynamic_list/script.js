"use strict";

const input = document.querySelector("#name");
const addButton = document.querySelector("#add");
const removeButton = document.querySelector("#remove");
const names = document.querySelector("#names");

function addName() {
  if (input.value === "") return; // early return if-else rakenteen sijaan

  if (input.value === "Joa") return;

  const item = document.createElement("li");
  item.innerText = input.value;
  names.appendChild(item);
  input.value = "";
}

function removeName() {
  if (names.lastElementChild !== null)
    names.removeChild(names.lastElementChild);
}

addButton.addEventListener("click", addName);
removeButton.addEventListener("click", removeName);
