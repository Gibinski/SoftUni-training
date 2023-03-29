function cityTaxes(name, population, treasury) {
    let city = {
        name, 
        population, 
        treasury, 
        taxRate: 10,
        collectTaxes() {
            this.treasury += Math.trunc(this.population * this.taxRate) 
        },
        applyGrowth(percentage) {
            this.population += Math.trunc(this.population * percentage / 100)
        },
        applyRecession(percentage) {
            this.treasury -= Math.trunc(this.treasury * percentage / 100)
        }
    }
    return city
}

// Test
let city = cityTaxes(
    'Tortuga',
    7000,
    15000);
console.log(city);

console.log("");

city = cityTaxes(
    'Tortuga',
    7000,
    15000);
city.collectTaxes();
console.log(city.treasury);
city.applyGrowth(5);
console.log(city.population);
