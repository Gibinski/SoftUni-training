text = input()
vowels = ['a', 'o', 'u', 'e', 'i']
no_vowels = "".join([ch for ch in text if ch.lower() not in vowels])
print(no_vowels)