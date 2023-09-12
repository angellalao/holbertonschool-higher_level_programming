const red_header = document.querySelector("#red_header");
red_header.onclick = addClassRed;

function addClassRed() {
    let element = document.getElementsByTagName("header")[0];
    element.classList.add("red")
}
