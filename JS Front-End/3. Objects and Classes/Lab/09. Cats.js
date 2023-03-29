function solve(arr) {
    let cats = [];
    class Cat {
        constructor(name, age) {
            this.name = name;
            this.age = age;
        }
        meow() {
            console.log(`${this.name}, age ${this.age} says Meow`);
        }
    }

    for (let i = 0; i < arr.length; i++) {
        let [name, age] = arr[i].split(" ")
        cats.push(new Cat(name, age));
    }
    for (const cat of cats) {
        cat.meow();
    }
}

solve(['Mellow 2', 'Tom 5']);
console.log("");
solve(['Candy 1', 'Poppy 3', 'Nyx 2']);