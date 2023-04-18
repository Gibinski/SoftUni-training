function addItem() {
    const newOption = document.createElement("option");
    const inputText = document.getElementById("newItemText");
    const inputValue = document.getElementById("newItemValue");
    const menu = document.getElementById("menu");

    newOption.textContent = inputText.value;
    newOption.value = inputValue.value;
    menu.appendChild(newOption);

    inputText.value = "";
    inputValue.value = "";
}