"use strict";

const form = document.querySelector("#search-form");
const query = document.querySelector("#query");
const status = document.querySelector("#status");

form.addEventListener("submit", async function (event) {
  event.preventDefault();

  status.innerText = "Loading...";

  try {
    const response = await fetch(
      `https://api.tvmaze.com/search/people?q=${query.value}`
    );

    if (!response.ok) {
      throw new Error("HTTP error! Status: " + response.status);
    }

    const data = await response.json();

    console.log(data);
    status.innerText = `Found ${data.length} results. Check the console.`;
  } catch (error) {
    console.error(error);
    status.innerText = "Search failed.";
  }
});
