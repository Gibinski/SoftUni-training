elements = [int(x) for x in input().split()]
removed_elements = []
while elements != []:
    new_elemets = []
    index = int(input())
    if index < 0:
        elements[0] = elements[-1]
        new_elemets = elements
    elif index >= len(elements):
        elements[-1] = elements[0]
        value = elements[0]
        new_elemets = [x + value for x in elements]
    else:
        value = elements.pop(index)
        for element in elements:
            if value >= element:
                new_elemets.append(element + value)
            else:
                new_elemets.append(element - value)
    removed_elements.append(value)
    elements = new_elemets
result = sum(removed_elements)
print(result)
