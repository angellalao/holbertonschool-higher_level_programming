document.addEventListener("DOMContentLoaded", function () {
    async function getHello() {
        const URL = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
        const selector = document.getElementById('hello');
        const response = await fetch(URL);
        const data = await response.json();
        console.log(data);
        selector.textContent = data.hello;
    }
    getHello();
});