function sumTable() {
    const numbers = document.querySelectorAll("td:nth-child(even)");
    const sum = document.getElementById("sum");
    let arr = []
    for (const td of numbers) {
        arr.push(td.textContent);
    }
    arr.pop();
    sum.textContent = arr.reduce((a, b) => Number(a) + Number(b), 0)
}