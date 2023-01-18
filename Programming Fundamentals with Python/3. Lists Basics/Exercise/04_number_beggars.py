string_of_integers = input().split(", ")
count_of_beggars = int(input())
counter = 0
list_of_sum = [0] * count_of_beggars
for offer in string_of_integers:
    list_of_sum[counter] += int(offer)
    counter += 1
    if counter == count_of_beggars:
        counter = 0
print(list_of_sum)