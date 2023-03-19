function passwordValidator(password) {
    const isValidlength = (pass) => 6 <= pass.length && pass.length <= 10;
    const hasOnlyLettersAndDigits = (pass) => /^[a-zA-Z0-9]+$/g.test(pass);
    const hasAtLeast2Digits = (pass) => [...pass.matchAll(/\d/g)].length >= 2;
    const isValid = isValidlength(password) && hasOnlyLettersAndDigits(password) && hasAtLeast2Digits(password);

    if (isValid) {
        console.log('Password is valid');
    } else {
        if (!isValidlength(password)) {
            console.log("Password must be between 6 and 10 characters");
        }
        if (!hasOnlyLettersAndDigits(password)) {
            console.log("Password must consist only of letters and digits");
        }
        if (!hasAtLeast2Digits(password)) {
            console.log("Password must have at least 2 digits");
        }
    }
}

passwordValidator('logIn');
passwordValidator('MyPass123');
passwordValidator('Pa$s$s');
 