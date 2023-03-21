function loadingBar(number) {
    if (number === 100) {
        return "100% Complete!\n[%%%%%%%%%%]"
    } else {
        let charCount = number / 10;
        let load = "[" + "%".repeat(charCount) + ".".repeat(10 - charCount) + "]";

        return number + "% " + load + "\nStill loading..."
    }
}

console.log(loadingBar(30));
console.log(loadingBar(50));
console.log(loadingBar(100));