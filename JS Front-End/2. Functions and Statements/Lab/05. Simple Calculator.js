function simpleCalculator(a, b, operator) {
    const operations = {
        'add': a + b,
        'subtract': a - b,
        'multiply': a * b,
        'divide': a / b
    }
    return operations[operator];
}

console.log(simpleCalculator(5,5,'multiply'));
console.log(simpleCalculator(40,8,'divide'));
console.log(simpleCalculator(12,19,'add'));
console.log(simpleCalculator(50,13,'subtract'));