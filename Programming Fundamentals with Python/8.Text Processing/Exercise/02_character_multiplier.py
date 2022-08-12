def character(short, long, total_sum):
    for i in range(0, len(short)):
        total_sum += ord(short[i]) * ord(long[i])
    for i in range(len(short), len(long)):
        total_sum += ord(long[i])
    return total_sum


first, second = input().split()

if len(first) > len(second):
    print(character(second, first, 0))
else:
    print(character(first, second, 0))    
    
