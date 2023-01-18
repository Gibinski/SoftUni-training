def palindrome_integers(nums):
    for num in nums:
        print(num == num[::-1])


numbers = input().split(", ")
palindrome_integers(numbers)