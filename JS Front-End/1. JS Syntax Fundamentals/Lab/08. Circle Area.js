function solve (text) {
    let textType = typeof text
    if (textType === 'number') {
        let result = Math.pow(text, 2) * Math.PI;
        console.log(result.toFixed(2));
    } else {
        console.log(`We can not calculate the circle area, because we receive a ${textType}.`);
    }
}

solve('asd')
solve(5)
