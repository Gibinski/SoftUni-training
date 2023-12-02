def vowel_filter(func):
    def letters():
        result =  func()
        vowel = [ch for ch in result if ch.lower() in "aeiouy"]
        return vowel
    return letters


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())