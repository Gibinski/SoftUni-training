class reverse_iter:
    def __init__(self, my_iter) -> None:
        self.iter = my_iter

    def __iter__(self):
        return self
    
    def __next__(self): 
        if not self.iter:
            raise StopIteration
        return self.iter.pop()

reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)