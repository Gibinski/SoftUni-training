function sumDigits(num) {
    let sum = 0;
    let numAsStr = num.toString();
    for (const digitAsStr of numAsStr) {
        let digitAsNum = Number(digitAsStr);
        sum += digitAsNum;
    }
    console.log(sum);
}

sumDigits(245678);
sumDigits(97561);
sumDigits(543);