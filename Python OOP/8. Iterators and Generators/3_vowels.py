class vowels:
    VOWELS = {"A", "a", "E", "e", "I", "i", "O", "o", "U", "u", "Y", "y"}
    def __init__(self, iter_obj) -> None:
        self.iter_obj = list(filter(lambda i: i in vowels.VOWELS, iter_obj))
        self.counter = 0
    def __iter__(self):
        return self
    

    def __next__(self):
        if self.counter < len(self.iter_obj):
            result = self.iter_obj[self.counter]
            self.counter += 1
            return result
        else:
            raise StopIteration
        
my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
