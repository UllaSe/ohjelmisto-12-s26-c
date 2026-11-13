"use strict";

console.log("Before fetch.");

fetch("https://api.tvmaze.com/singlesearch/shows?q=emmerdale")
  .then(function (response) {
    if (!response.ok) {
      throw new Error("HTTP error! Status: " + response.status);
    }

    return response.json();
  })
  .then(function (data) {
    console.log("Fetched data:");
    console.log(data);
    console.log("Show name:", data.name);
  })
  .catch(function (error) {
    console.error("Fetch failed:", error.message);
  });

console.log("After fetch.");
