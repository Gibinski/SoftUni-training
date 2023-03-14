function printEveryNThElementFromAnArray(arr, step) {
    let arrToPrint = [];
    for (let index = 0; index < arr.length; index++) {
        if (index % step == 0) {
            arrToPrint.push(arr[index]);
        }
    }
    return arrToPrint;
}

console.log(printEveryNThElementFromAnArray(['5', '20', '31', '4', '20'], 2));
console.log(printEveryNThElementFromAnArray(['dsa','asd', 'test', 'tset'], 2));
console.log(printEveryNThElementFromAnArray(['1', '2','3', '4', '5'], 6));