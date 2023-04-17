function extractText() {
    const liElements = Array.from(document.getElementsByTagName("li"));
    for (const li of liElements) {
        document.getElementById("result").textContent += li.textContent + "\n";
    }
}