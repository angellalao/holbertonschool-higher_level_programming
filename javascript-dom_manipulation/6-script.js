const URL = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
const character =  document.querySelector("#character");

async function fetchName() {
    const response = await fetch(URL);
    const data = await response.json();
    console.log(data);
    character.textContent = data.name;
}

fetchName();
