def kwargs_length(**d):
    return len(d)


dictionary = {'name': 'Peter', 'age': 25}
print(kwargs_length(**dictionary))

dictionary = {}
print(kwargs_length(**dictionary))
