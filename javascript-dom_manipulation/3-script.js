const toggle_header = document.querySelector("#toggle_header");
toggle_header.onclick = switchClassRedGreen;

function switchClassRedGreen() {
    let element = document.getElementsByTagName("header")[0];
    element.classList.toggle("red")
    element.classList.toggle("green")
}
