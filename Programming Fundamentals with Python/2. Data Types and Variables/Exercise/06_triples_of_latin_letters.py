num = int(input())
for i in range(num):
    for j in range(num):
        for k in range(num):
            print(chr(ord("a") + i), end="")
            print(chr(ord("a") + j), end="")
            print(chr(ord("a") + k))
    