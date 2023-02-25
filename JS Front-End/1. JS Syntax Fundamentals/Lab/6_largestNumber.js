function solve(num0, num1, num2) {
    let largestNum;
    if (num0 > num1 && num0 > num2) {
        largestNum = num0;
    } else if (num1 > num2) {
        largestNum = num1;
    } else {
        largestNum = num2;
    }
    console.log(`The largest number is ${largestNum}.`);
}

solve(1, 3, 7);
solve(-3, -7, 5);
solve(30, 7, 13);
