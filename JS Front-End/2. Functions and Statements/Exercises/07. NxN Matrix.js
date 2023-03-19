function nexNMatrix(n) {

    return new Array(n).fill(new Array(n).fill(n)).forEach(row => console.log(row.join(" ")));
}

console.log(nexNMatrix(3));
console.log(nexNMatrix(7));
nexNMatrix(11);