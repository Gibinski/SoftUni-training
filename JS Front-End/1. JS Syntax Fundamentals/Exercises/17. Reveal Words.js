function revealWords(words, text) {
    let wordsArr = words.split(", ");
    let textArr = text.split(" ");

    for (let index = 0; index < textArr.length; index++) {
        if ([...textArr[index]][0] === "*" ) {
            for (const word of wordsArr) {
                if (textArr[index].length === word.length) {
                    textArr[index] = word;
                }
            }
        }
    }
    console.log(textArr.join(" "))
}

revealWords('great','softuni is ***** place for learning new programming languages');
revealWords('great, learning','softuni is ***** place for ******** new programming languages');