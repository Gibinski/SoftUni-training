class Stack:
    def __init__(self):
        self.data = []


    def push(self, element: str):
        self.data.append(element)


    def pop(self):
        return self.data.pop()


    def top(self):
        return self.data[-1]


    def is_empty(self):
        if len(self.data) == 0:
            return True
        
        return False
            

    def __str__(self):
        data_set = []
        for i in range(len(self.data) -1, -1, -1):
            data_set.append(self.data[i])
        result = ", ".join(data_set)

        return f"[{result}]"
