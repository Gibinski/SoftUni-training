function oddOccurrences(text) {
    let allWords = text.toLowerCase().split(" ");
    let setOfWords = {};
    for (const word of allWords) {
        if (setOfWords[word] === undefined) {
            setOfWords[word] = 1;
        } else {
            setOfWords[word]++;
        }
    }
    let result = "";
    let oddWords = Object.entries(setOfWords).filter((w) => w[1] % 2 !== 0);
    for (word of oddWords) {
        result += word[0] + " ";
    }
    console.log(result);
}

oddOccurrences('Java C# Php PHP Java PhP 3 C# 3 1 5 C#');
console.log("");
oddOccurrences('Cake IS SWEET is Soft CAKE sweet Food');