function solve() {
  const outputDiv = document.getElementById("output");
  const textArea = document.getElementById("input");
  let input = textArea.value;
  let sentences = input.split(".");
  sentences.pop();

  while (sentences.length > 0) {
    const p = document.createElement("p");
    let sentence = sentences.splice(0, 3);
    p.textContent = sentence.join(". ") + ".";
    outputDiv.appendChild(p)
  }

  textArea.value = "";
}