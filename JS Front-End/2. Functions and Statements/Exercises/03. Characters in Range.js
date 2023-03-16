function charactersInRange(firstCh, secondCh) {
    let first = firstCh.charCodeAt(0);
    let second = secondCh.charCodeAt(0);
    let min = Math.min(first, second);
    let max = Math.max(first, second);
    
    let charsArr = [];
    for (let i = min + 1; i < max; i++) {
        charsArr.push(String.fromCharCode(i))
    }
    
    return charsArr.join(" ")
}
console.log(charactersInRange('a','d') === "b c");
console.log(charactersInRange('#',':') === "$ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9");
console.log(charactersInRange('C','#') === "$ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B");
