function sameNumbers(number) {
    let numArr = number.toString().split("");
    let sum = 0;
    let isSame = numArr[0];

    for (num of numArr) {
        if (num != isSame) {
            isSame = "";
        }
        sum += Number(num);
    }

    console.log(Boolean(isSame));
    console.log(sum);
}

sameNumbers(2222222);
sameNumbers(1234);
