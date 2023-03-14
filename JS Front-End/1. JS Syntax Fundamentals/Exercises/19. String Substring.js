function stringSubstring(word, text) {
    let wordToLowerCase = word.toLowerCase();
    let textToLowerCase = text.toLowerCase().split(" ");

    for (const w of textToLowerCase) {
        if (w === wordToLowerCase) {
            return word;
        }
    }
    return `${word} not found!`
}

console.log(stringSubstring('javascript','JavaScript is the best programming language'));
console.log(stringSubstring('python','JavaScript is the best programming language'));
