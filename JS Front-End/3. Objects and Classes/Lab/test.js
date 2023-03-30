let arr = [3, 5, 7];
arr.foo = "hello";
    
for (let key in arr) {
  console.log(key); // logs "0", "1", "2", "foo"
  console.log(arr[key]); // logs "0", "1", "2", "foo"
}
    
console.log(""); // logs "3", "5", "7"
for (let value of arr) {
  console.log(value); // logs "3", "5", "7"
  // it doesn't log "3", "5", "7", "hello"
}