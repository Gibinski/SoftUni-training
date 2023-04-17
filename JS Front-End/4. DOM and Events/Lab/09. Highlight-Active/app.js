function focused() {
    const inputs = document.getElementsByTagName("input");
    for (let i of inputs) {
        i.addEventListener("focus", focused);
        i.addEventListener("blur", blurred);
        
    }

    function focused(e) {
        const input = this;
        input.parentElement.classList.add("focused");
    }

    function blurred(e) {
        const input = this;
        input.parentElement.classList.remove("focused")
    }
}