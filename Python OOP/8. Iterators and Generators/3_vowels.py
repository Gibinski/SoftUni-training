class vowels:
    VOWELS = {"a", "e", "i", "o", "u", "y"}
    def __init__(self, iter_obj) -> None:
        self.iter_obj = list(filter(lambda i: i.lower() in vowels.VOWELS, iter_obj))
        self.current_index = 0
    def __iter__(self):
        return self
    

    def __next__(self):
        if self.current_index < len(self.iter_obj):
            result = self.iter_obj[self.current_index]
            self.current_index += 1
            return result
        else:
            raise StopIteration
        
my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
