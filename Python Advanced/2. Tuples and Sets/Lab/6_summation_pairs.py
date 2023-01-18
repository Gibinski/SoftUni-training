numbers = [int(n) for n in input().split()]
target = int(input())

while numbers:
    num1 = numbers.pop()
    if num1 < target:
        for num2 in numbers:
            if num2 < target:
                if num1 + num2 == target:
                    print(f"{num2} + {num1} = {target}")
                    numbers.remove(num2)
                    break
            else:
                numbers.remove(num2)
                    
    


