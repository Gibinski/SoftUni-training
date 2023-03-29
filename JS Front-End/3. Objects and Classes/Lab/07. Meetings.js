function meetings(arr) {
    let meetingsList = {};
    for (const line of arr) {
        let [day, name] = line.split(" ");
        if (meetingsList.hasOwnProperty(day)) {
            console.log(`Conflict on ${day}!`);
        } else {
            console.log(`Scheduled for ${day}`);
            meetingsList[day] = name
        }
    }
    for (const day in meetingsList) {
        console.log(`${day} -> ${meetingsList[day]}`);
    }
}

meetings(['Monday Peter',
 'Wednesday Bill',
 'Monday Tim',
 'Friday Tim']);

console.log("");

meetings(['Friday Bob',
'Saturday Ted',
'Monday Bill',
'Monday John',
'Wednesday George']);