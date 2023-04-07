function piccolo(input) {
    let parkingLot = [];
    for (const line of input) {
        let [command, carNum] = line.split(", ");
        if (command === 'IN' && !parkingLot.includes(carNum)) {
            parkingLot.push(carNum)
        } else if (command === 'OUT' && parkingLot.includes(carNum)) {
            let index = parkingLot.indexOf(carNum);
            parkingLot.splice(index, 1);
        }
    }
    if (parkingLot.length !== 0) {
        let sortedParkingLot = parkingLot.sort((carA, carB) => carA.localeCompare(carB));
        sortedParkingLot.forEach((c) => console.log(c))
    } else {
        console.log("Parking Lot is Empty");
    }
}

piccolo(['IN, CA2844AA',
'IN, CA1234TA',
'OUT, CA2844AA',
'IN, CA9999TT',
'IN, CA2866HI',
'OUT, CA1234TA',
'IN, CA2844AA',
'OUT, CA2866HI',
'IN, CA9876HH',
'IN, CA2822UU']);
console.log("");
piccolo(['IN, CA2844AA',
'IN, CA1234TA',
'OUT, CA2844AA',
'OUT, CA1234TA']);
