def palindrom_filter(word):
    if word == word[::-1]:
        return word

words = input().split()
palindrome = input()
palindrome_list = [x for x in words if palindrom_filter(x)]
    
print(palindrome_list)
print(f"Found palindrome {palindrome_list.count(palindrome)} times")