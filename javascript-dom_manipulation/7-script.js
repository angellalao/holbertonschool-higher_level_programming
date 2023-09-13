const URL = 'https://swapi-api.hbtn.io/api/films/?format=json';
const movies = document.querySelector('#list_movies');

async function getTitles() {
    const response = await fetch(URL);
    const data = await response.json();
    console.log(data);
    const films = data.results;
  
    for (let i = 0; i < films.length; i++) {
        let newListItem = document.createElement('li');
        newListItem.textContent = films[i].title;
        movies.appendChild(newListItem); 
    }
}

getTitles();