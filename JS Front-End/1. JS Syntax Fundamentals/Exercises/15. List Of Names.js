function listOfNames(arr) {
    arr.sort();
    for (let index = 0; index < arr.length; index++) {
        if (arr) {
            console.log(`${index + 1}.${arr[index]} `);
        }
    }
}

listOfNames(["John", "Bob", "Christina", "Ema"]);
 