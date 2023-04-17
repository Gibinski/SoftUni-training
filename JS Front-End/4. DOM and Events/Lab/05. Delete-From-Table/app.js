function deleteByEmail() {
    const email = document.getElementsByName("email").value;
    let elements = Array.from(document.querySelectorAll("li"));
    for (const li of elements) {
        if (li.textContent === email) {
            let a;
        }
    }
}