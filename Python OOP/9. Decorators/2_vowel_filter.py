def vowel_filter(func):
    def letters():
        return [ch for ch in func() if ch.lower() in "aeiouy"]
    return letters


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())