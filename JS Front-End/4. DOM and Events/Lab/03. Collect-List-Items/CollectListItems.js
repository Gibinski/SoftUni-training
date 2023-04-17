function extractText() {
    const liElements = document.getElementsByTagName("li");
    let result = ""
    for (const li of liElements) {
        result += li.textContent + "\n";
    }
    document.getElementById("result").textContent = result;
}