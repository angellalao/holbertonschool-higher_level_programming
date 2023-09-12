const add_item = document.querySelector("#add_item");
add_item.onclick = newli;

function newli() {
    let element = document.querySelector("ul.my_list");
    let new_li = document.createElement("li");
    new_li.textContent = "Item"
    element.appendChild(new_li)
}
