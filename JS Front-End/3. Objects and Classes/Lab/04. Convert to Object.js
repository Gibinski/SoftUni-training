function convertToObject(jsonStr) {
    let person = JSON.parse(jsonStr);
    for (const key in person) {
        console.log(`${key}: ${person[key]}`);
    }
}

console.log(convertToObject('{"name": "George", "age": 40, "town": "Sofia"}'));
console.log(convertToObject('{"name": "Peter", "age": 35, "town": "Plovdiv"}'));