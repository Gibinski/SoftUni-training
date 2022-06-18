from operator import index, indexOf
from textwrap import indent


l = ["A", "AA", "AB", "B", "BA", "BB", None ]
print(len(l))
print(l)
print()

del l[0]
print(len(l))
print(l)
print()

l[0] = None
print(len(l))
print(l)
print()

l.remove("BB")
print(len(l))
print(l)
print()

l.pop(l.index(l[1]))
print(len(l))
print(l)
