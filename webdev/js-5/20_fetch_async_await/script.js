"use strict";

async function fetchShow() {
  console.log("Starting fetch.");

  try {
    const response = await fetch(
      "https://api.tvmaze.com/singlesearch/shows?q=emmerdale"
    );

    if (!response.ok) {
      throw new Error("HTTP error! Status: " + response.status);
    }

    const data = await response.json();

    console.log("Fetched data:");
    console.log(data);
    console.log("Show name:", data.name);
  } catch (error) {
    console.error("Fetch failed:", error.message);
  } finally {
    console.log("Fetch finished.");
  }
}

console.log("Before function call.");
fetchShow();
console.log("After function call.");
