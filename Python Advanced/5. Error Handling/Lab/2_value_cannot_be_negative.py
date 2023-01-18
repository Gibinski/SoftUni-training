class ValueCanotBeNegative(Exception):
    """Value can not be zero"""

n = int(input())
for i in range(n):
    number = int(input())
    if number < 0:
        raise ValueCanotBeNegative
