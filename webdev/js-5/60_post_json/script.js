"use strict";

const form = document.querySelector("#message-form");
const name = document.querySelector("#name");
const message = document.querySelector("#message");
const result = document.querySelector("#result");

form.addEventListener("submit", async function (event) {
  event.preventDefault();

  const data = {
    name: name.value,
    message: message.value,
  };

  try {
    const response = await fetch(
      "https://jsonplaceholder.typicode.com/posts",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      }
    );

    if (!response.ok) {
      throw new Error("HTTP error! Status: " + response.status);
    }

    const responseData = await response.json();

    console.log(responseData);
    result.innerText = JSON.stringify(responseData, null, 2);
  } catch (error) {
    console.error(error);
    result.innerText = "Request failed.";
  }
});
