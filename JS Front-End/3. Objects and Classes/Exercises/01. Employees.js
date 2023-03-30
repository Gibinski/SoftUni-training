function employees(input) {
    for (const name of input) {
        let [employeeName, personalNum] = [name, name.length]
        console.log(`Name: ${employeeName} -- Personal Number: ${personalNum}`);
    }
}

employees([
    'Silas Butler',
    'Adnaan Buckley',
    'Juan Peterson',
    'Brendan Villarreal'
]);
console.log("");
employees([
    'Samuel Jackson',
    'Will Smith',
    'Bruce Willis',
    'Tom Holland'
]);