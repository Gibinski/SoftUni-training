function sortingNumbers(arr) {
    let resultArr = [];
    arr.sort((a, b) => a - b);
    while (arr.length) {
        resultArr.push(arr.shift());
        if (arr.length) {
            resultArr.push(arr.pop());
        }
    }  
    return resultArr;
}

console.log(sortingNumbers([1, 65, 3, 52, 48, 63, 31, -3, 18, 56]));