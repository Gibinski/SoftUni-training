"""
Peter is a programming enthusiast who wants to create a chat where people will send 
messages via number codes. He starts by creating a program for only four messages. 
Create a program that receives the n number of messages sent. 
On the following n lines, it will receive integer numbers. 
For each number, the program should print a different message:
If the number is 88 - "Hello"
If the number is 86 - "How are you?"
If the number is not 88 nor 86, and it is below 88 - "GREAT!"
If the number is over 88 - "Bye."
"""

lines = int(input())

for i in range(lines):
    message = int(input())
    if message == 88:
        print("Hello")
    elif message == 86:
        print("How are you?")
    elif message < 88:
        print("GREAT!")
    else:
        print("Bye.")
