function inventory(input) {
    let heroes = [];
    for (const line of input) {
        [name, level, itemsStr] = line.split(" / ");
        items = itemsStr.split(", ");
        heroes.push({name, level: Number(level), items})
    }
    // sorting heroes by level and name
    let sortedHeroes = heroes.sort((heroA, heroB) => {
        let result = heroA.level - heroB.level;
        if (result === 0) {
            return heroA.name.localeCompare(heroB.name)
        }
        return result
    });
    // print heroes
    for (const hero of sortedHeroes) {
        console.log(`Hero: ${hero.name}`);
        console.log(`level => ${hero.level}`);
        console.log(`items => ${hero.items.join(", ")}`);
    }
}

inventory([
    'Isacc / 25 / Apple, GravityGun',
    'Derek / 12 / BarrelVest, DestructionSword',
    'Hes / 1 / Desolator, Sentinel, Antara'
    ]);
console.log("")
inventory([
    'Batman / 2 / Banana, Gun',
    'Superman / 18 / Sword',
    'Poppy / 28 / Sentinel, Antara'
    ]);