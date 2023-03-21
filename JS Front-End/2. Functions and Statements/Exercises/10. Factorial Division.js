function factorialDivision(firstNumm, secondNum) {
    function getFactorial(number) {
        if (number === 1) {
            return number
        }
        return number * getFactorial(number - 1)
    }
    let firstFactorial = getFactorial(firstNumm);
    let secondFactorial = getFactorial(secondNum);
    let result = firstFactorial / secondFactorial;

    return result.toFixed(2)
 }

 console.log(factorialDivision(5, 2));
 console.log(factorialDivision(6, 2));
