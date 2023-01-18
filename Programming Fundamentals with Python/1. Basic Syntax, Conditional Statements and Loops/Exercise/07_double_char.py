# You will be given strings until you receive the command "End". 
# For each string given, you should print a string in which each character 
# (case-sensitive) is repeated twice. Note that if you receive the string "SoftUni", 
# you should NOT print it!

string = input()
while string != "End":
    new_str = ""
    if string != "SoftUni":
        for ch in string:
            new_str += ch * 2
        print(new_str)
    string = input()
        


