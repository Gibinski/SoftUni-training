function addressBook(data) {
    let book = {};
    for (const line of data) {
        let [name, address] = line.split(":");
        book[name] = address;
    }
    let sortedBook = Object.keys(book)
        .sort((nameA, nameB) => nameA.localeCompare(nameB));
    for (const name of sortedBook) {
        console.log(`${name} -> ${book[name]}`);
    }
}

addressBook(['Tim:Doe Crossing',
 'Bill:Nelson Place',
 'Peter:Carlyle Ave',
 'Bill:Ornery Rd']);

 console.log("");

addressBook(['Bob:Huxley Rd',
'John:Milwaukee Crossing',
'Peter:Fordem Ave',
'Bob:Redwing Ave',
'George:Mesta Crossing',
'Ted:Gateway Way',
'Bill:Gateway Way',
'John:Grover Rd',
'Peter:Huxley Rd',
'Jeff:Gateway Way',
'Jeff:Huxley Rd']);