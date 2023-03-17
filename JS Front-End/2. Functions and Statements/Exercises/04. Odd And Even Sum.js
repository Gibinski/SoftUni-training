function oddAndEvenSum(num) {
    let arrNum = String(num)
    .split("")
    .map((ch) => Number(ch));
     
    let sum = function(arrNum) {
        let odds = 0;
        let evens = 0;

        for (const n of arrNum) {
            if (n % 2 == 0) {
                evens += n;
            } else {
                odds += n;
            }
        }
        return [odds, evens]
    }
    let [oddSum, evenSum] = sum(arrNum);
    return `Odd sum = ${oddSum}, Even sum = ${evenSum}`
}


// Test
console.log(oddAndEvenSum(1000435) === "Odd sum = 9, Even sum = 4");
console.log(oddAndEvenSum(3495892137259234) === "Odd sum = 54, Even sum = 22");
console.log(oddAndEvenSum(1000435));
console.log(oddAndEvenSum(3495892137259234));
