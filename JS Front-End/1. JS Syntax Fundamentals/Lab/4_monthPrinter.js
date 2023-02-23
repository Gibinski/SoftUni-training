function solve (num) {
    let months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
    
    if (num >= 1 && num <= 12) {
        console.log(months[num - 1])
    } else {
        console.log("Error!")
    }
}    

// Test
solve(-1)
solve(12)
solve(0)
solve(13)