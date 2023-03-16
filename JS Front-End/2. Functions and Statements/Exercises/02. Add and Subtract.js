function solve(firstNum, secondNUm, thirtNum) {
    const add = (a, b) => a + b;
    const subtract = (c, d) => c - d

    return subtract(add(firstNum, secondNUm), thirtNum)
}

console.log(solve(23,6,10) === 19);
console.log(solve(1,17,30) === -12);
console.log(solve(42,58,100) === 0);
