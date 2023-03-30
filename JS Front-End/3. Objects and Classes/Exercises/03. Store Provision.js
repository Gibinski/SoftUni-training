function storeProvision(firstArr, secondArr) {
    let store = {};
    for (let i = 0; i < firstArr.length; i+=2) {
        store[firstArr[i]] = Number(firstArr[i+1]);
    }
    for (let i = 0; i < secondArr.length; i+=2) {
        if (store[secondArr[i]] == undefined) {
            store[secondArr[i]] = Number(secondArr[i+1]);
        } else {
            store[secondArr[i]] += Number(secondArr[i+1]);
        }
    }
    for (const [product, quantity] of Object.entries(store)) {
        console.log(`${product} -> ${quantity}`)
    }
}

storeProvision(
    ['Chips', '5', 'CocaCola', '9', 'Bananas', '14', 'Pasta', '4', 'Beer', '2'],
    ['Flour', '44', 'Oil', '12', 'Pasta', '7', 'Tomatoes', '70', 'Bananas', '30']
);

console.log("");

storeProvision(
    ['Salt', '2', 'Fanta', '4', 'Apple', '14', 'Water', '4', 'Juice', '5'],
    ['Sugar', '44', 'Oil', '12', 'Apple', '7', 'Tomatoes', '7', 'Bananas', '30']
);