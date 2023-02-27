function solve (n, inputArr) {
    let output = '';
    for (let i = n-1; i>=0; i--) {
        output += ` ${inputArr[i]}`;
    }
    console.log(output)
}

solve(3, [10, 20, 30, 40, 50]);
solve(4, [-1, 20, 99, 5]);
solve(2, [66, 43, 75, 89, 47]);