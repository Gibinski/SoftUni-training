from utils.fibonacci import *
from utils.command_parrsser import *

nums = []
while True:
    line = input()
    if line == "Stop":
        break

    command, arg = parrsse_line(line)
    if command == "Create":
        nums = creat(arg)
        print(*nums) 
    else:
        idx = locate(arg, nums)
        output = f"The number {arg} is not in sequence" if idx == - 1 else f"The number - {arg} is in index {idx}"
        print(output)
