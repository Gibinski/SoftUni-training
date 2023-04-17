function addItem() {
    const ulContainer = document.getElementById("items")
    const input = document.getElementById("newItemText");
    const newLi = document.createElement("li");
    const newAncher = document.createElement("a");
    newLi.textContent = input.value;
    newAncher.textContent = "[Delete]";
    newAncher.setAttribute("href", "#")
    newAncher.addEventListener("click", deleteHandler);
    newLi.appendChild(newAncher);
    ulContainer.appendChild(newLi);
    input.value = "";

    function deleteHandler(e) {
        e.currentTarget.parentElement.remove();
    }
}