function convertToJSON(name, lastName, hairColor) {
    const obj = {
        name,
        lastName,
        hairColor
    }
    return JSON.stringify(obj);
}

console.log(convertToJSON('George', 'Jones', 'Brown'));
console.log(convertToJSON('Peter', 'Smith', 'Blond'));
