'use strict';

// window viittaa aina selainikkunaan
console.log(window);

//window.alert('Selainikkuna huutelee!');

//const isTrue = window.confirm('On totta?');
//console.log(isTrue);

// window.location viittaa selainikkunan osoitteseeen (url)
console.log(window.location.host); // tulostaa palvelimen, josta html on ladattu
//window.location.href = 'page2.html'; // suhteellinen (relatiivinen) sijainti
//window.location.href = 'https://www.metropolia.fi'; // absoluuttinen sijainti

// DOM
// document viittaa html-tiedostosta ladattuun rakenteeseen (DOM)
console.log(window.document);

// haetaan viittaus DOM-elementtiin
//const liELements = document.getElementsByTagName('li');
//console.log(liELements);
//liELements[0].textContent = 'ensimmäinen elementti päivitetty skriptistä.';

// sama käyttäen css-valitsinta (css selector)
// querySelectorAll palauttaa aina "listana"
const liElements = document.querySelectorAll('li');
//console.log(liElements);
liElements[1].textContent = 'toinen päivitetty';

// querySelector() palauttaa aina vain yhden löydetyn elementin (ensimmäisen, jos useampi)
const outputP = document.querySelector('#output');
outputP.textContent = 'Sisältö skriptistä.';
