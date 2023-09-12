const n_header = document.querySelector("#update_header");
n_header.onclick = update_header;

function update_header() {
    let element = document.querySelector("header");
    element.textContent = "New Header!!!";
}
