function addItem() {
    const newItemText = document.getElementById("newItemText").value;
    document.getElementById("items").innerHTML += `<li>${newItemText}</li>`;
}