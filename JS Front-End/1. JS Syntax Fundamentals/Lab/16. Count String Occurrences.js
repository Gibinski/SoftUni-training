function solve(text, serchedWord) {
    let words = text.split(' '); 
    let count = 0;
    for (const word of words) {
        if (word === serchedWord) {
            count++
        }
    }
    console.log(count)
}

solve('This is a word and it also is a sentence.', 'is');
