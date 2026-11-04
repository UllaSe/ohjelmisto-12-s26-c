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

// Tehdään uusi lista taulukon perusteella ja lisätään DOMiin
const inventoryItems = ['miekka', 'kilpi', 'porkkana'];
// 1. haetaan dom-viittaus div-"laatikkoon/containeriin"
const inventoryDiv = document.querySelector('#inventory');
// 2. haetaan viittaus divin sisällä olevaan ol-elementtiin
const inventoryList = inventoryDiv.querySelector('ol');
// 3. rakennetaan lista html-koodina
let listHTML = '';
for (let i = 0; i < inventoryItems.length; i++) {
  listHTML = listHTML + '<li>' + inventoryItems[i] + '</li>';
}
console.log('html stringi:', listHTML);
// 4. lisätään generoitu html ol-elementin sisään
inventoryList.innerHTML = listHTML;

// TOINEN (ehkä joskus työläämpi, mutta suositeltu) tapa:
// 3. luodaan DOM-elementit jokaiselle taulukon alkiolle/listan elementille
// ja lisätään DOMin ol-elementin lapsiksi (for-of silmukkaesimerkki)
for (const item of inventoryItems) {
  const newLi = document.createElement('li');
  newLi.textContent = item;
  inventoryList.append(newLi);
}

// Inventaarion näyttäminen kysymällä aluksi käyttäjältä
/**
const displayInventory = confirm('Näytetäänkö inventaario?');
if (displayInventory) {
    inventoryDiv.classList.remove('hidden');
}
*/

// Inventaarion näyttäminen nappulaan sidotun tapahtumankäsittelijän avulla
const button = document.querySelector('button');
// Napin tekstin muuttamista varten tarvitsee tietää, onko lista näkyvissä vai ei
let isInventoryVisible = false;
button.addEventListener('click', function (event) {
  console.log('napin click-event-olio:', event);
  inventoryDiv.classList.toggle('hidden');
  isInventoryVisible = !isInventoryVisible;
  if (isInventoryVisible) {
    button.textContent = 'Piilota esineet';
  } else {
    button.textContent = 'Näytä esineet';
  }
});
