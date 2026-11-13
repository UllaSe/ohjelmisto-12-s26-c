"use strict";

const form = document.querySelector("#search-form");
const query = document.querySelector("#query");
const results = document.querySelector("#results");

form.addEventListener("submit", async function (event) {
  event.preventDefault();

  results.innerHTML = "";

  try {
    const response = await fetch(
      `https://api.tvmaze.com/search/people?q=${query.value}`
    );

    if (!response.ok) {
      throw new Error("HTTP error! Status: " + response.status);
    }

    const data = await response.json();

    for (const result of data) {
      const person = result.person;

      const article = document.createElement("article");
      const heading = document.createElement("h2");
      const image = document.createElement("img");
      const link = document.createElement("a");

      heading.innerText = person.name;

      if (person.image !== null) {
        image.src = person.image.medium;
      } else {
        image.src = "https://placehold.co/210x295?text=Not%20Found";
      }

      link.innerText = "Open details";
      article.appendChild(heading);
      article.appendChild(image);
      article.appendChild(link);
      results.appendChild(article);
    }
  } catch (error) {
    console.error(error);
    results.innerText = "Could not load results.";
  }
});
