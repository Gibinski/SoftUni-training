function palindromeIntegers(arr) {
    const isPalindorme = function(str) {
        return str === str.split("").reverse().join("")
    }

    for (const number of arr) {
        let result = isPalindorme(String(number));
        console.log(result);
    }

}

palindromeIntegers([123,323,421,121]);
console.log(" ");
palindromeIntegers([32,2,232,1010]);
