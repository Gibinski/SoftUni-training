function pascalCaseSplitter(text) {
    let output = [];
    let word = "";
    for (const ch of text) {
        let ascii = ch.charCodeAt(0);
        if (65 <= ascii && ascii <= 90) {
            output.push(word);
            word = "";
        }
        word += ch;
    }
    output.push(word);
    output.shift();
    console.log(output.join(", "));
}

pascalCaseSplitter('SplitMeIfYouCanHaHaYouCantOrYouCan');
pascalCaseSplitter('HoldTheDoor');
pascalCaseSplitter('ThisIsSoAnnoyingToDo');

console.log(" ")
// with Regex
function withRegex (text) {
    let output = text.split(/(?=[A-Z])/g);
    console.log(output.join(", "))
}

withRegex('SplitMeIfYouCanHaHaYouCantOrYouCan');
withRegex('HoldTheDoor');
withRegex('ThisIsSoAnnoyingToDo');