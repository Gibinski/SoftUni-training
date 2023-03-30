function employees(input) {
    Object.entries(input.reduce(
        (data, employee) => {
            data[employee] = employee.length;
            return data
    }, {})).forEach(([name, number]) => console.log(
        `Name: ${name} -- Personal Number: ${number}`))
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