function modernTimesOfHashTag(text) {
    let words = text.split(" ");

    for (const word of words) {
        let pattern = /\#[A-za-z]+$/;
        if (pattern.test(word)) {            
            let chars = word.slice(1);
            console.log(chars);
        }
    }
}

modernTimesOfHashTag('Nowadays everyone uses # to tag a #special word in #socialMedia');
modernTimesOfHashTag('The symbol # is known #variously in English-speaking #regions as the #number sign');
