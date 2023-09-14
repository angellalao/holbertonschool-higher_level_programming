const header = document.querySelector("#red_header");
header.onclick = changeColor;

function changeColor() {
    let headerElement = document.getElementsByTagName("header")[0];
    headerElement.style.color = "#FF0000";
}
