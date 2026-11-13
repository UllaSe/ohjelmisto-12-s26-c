'use strict';

console.log('Client-sovellus hereillä.');

// Haetaat kahden luvun summa käyttäen flask-serverin tarjoamaa palvelua
// http://127.0.0.1:3000/sum?number1=3&number2=6
async function getSum(num1, num2) {
   const response = await fetch(`http://127.0.0.1:3000/sum?number1=${num1}&number2=${num2}`);
   const result = await response.json();
   return result;
}


// sidotaan HTTP-pyynnön lähettäminen napin click-eventtiin ja tulostetaan palvelimen
// lähettämä vastaus DOMiin
const button = document.querySelector('button');
button.addEventListener('click', async function (){
    const output = document.querySelector('#output');
    // laskettava arvot toistaiseki kovakoodattu funktiokutsuun
    const result = await getSum(2, 5);
    console.log('result', result);
    output.textContent = result.result;
});
