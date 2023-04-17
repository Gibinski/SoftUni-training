function addItem() {
    const newElement = document.createElement("li");
    let input = document.getElementById("newItemText");
    newElement.textContent = input.value;
    document.getElementById("items").appendChild(newElement);
    input.value = "";
}