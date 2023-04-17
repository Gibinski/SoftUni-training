function deleteByEmail() {
    const result = document.getElementById("result");
    const input = document.querySelector("input[name=email");
    const evenTds = document.querySelectorAll("td:nth-child(even)");
    let emailValue = input.value;
    for (let li of evenTds) {
        if (li.textContent === emailValue) {
            li.parentElement.remove();
            result.textContent = "Delete";
            return;
        }
    }        
    result.textContent = 'Not found.';
}