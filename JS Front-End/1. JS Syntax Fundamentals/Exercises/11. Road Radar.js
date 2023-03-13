function roadRadar(speed, area) {
    let speedLimit;
    let status;

    switch (area) {
        case "motorway":
            speedLimit = 130;
            break;
        case "interstate":
            speedLimit = 90;
            break;
        case "city":
            speedLimit = 50;
            break;
        case "residential":
            speedLimit = 20;
            break;
    }
    let speeding = speed - speedLimit;

    if (speeding <= 20) {
        status = "speeding";
    } else if (speeding <= 40) {
        status = "excessive speeding";
    } else {
        status = "reckless driving";
    }

    if (speeding <= 0) {
        console.log(`Driving ${speed} km/h in a ${speedLimit} zone`);
    } else {
        console.log(`The speed is ${speeding} km/h faster than the allowed speed of ${speedLimit} - ${status}`);
    }
}

roadRadar("40", 'city');
roadRadar(21, 'residential');
roadRadar(120, 'interstate');
roadRadar(200, 'motorway');