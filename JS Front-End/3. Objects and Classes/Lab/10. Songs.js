function solve(input) {
    class Song {
        constructor(type, name, time) {
            this.type = type
            this.name = name
            this.time = time
        }
    }

    let songs = [];
    let numberOfSong = input.shift();
    let typeOfSong = input.pop();

    for (let i = 0; i < numberOfSong; i++) {
        let [type, name, time] = input[i].split("_");
        songs.push(new Song(type, name, time));
    }
    
    if (typeOfSong !== "all") {
        songs = songs.filter((song) => typeOfSong === song.type);
    } 
    songs.forEach((song) => console.log(song.name)); 
}

solve([3,
    'favourite_DownTown_3:14',
    'favourite_Kiss_4:16',
    'favourite_Smooth Criminal_4:01',
    'favourite']);
console.log("")
solve([4,
    'favourite_DownTown_3:14',
    'listenLater_Andalouse_3:24',
    'favourite_In To The Night_3:58',
    'favourite_Live It Up_3:48',
    'listenLater']);
console.log("")
solve([2,
    'like_Replay_3:15',
    'ban_Photoshop_3:48',
    'all']);