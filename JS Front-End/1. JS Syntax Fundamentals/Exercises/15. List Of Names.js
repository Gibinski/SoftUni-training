function listOfNames(arr) {
    arr.sort((a, b) => {
        return a.localeCompare(b);
    });
    for (let index = 0; index < arr.length; index++) {
        console.log(`${index + 1}.${arr[index]} `);
    }
}

listOfNames(["John", "Bob", "Christina", "Ema"]);
 