def get_info(**kwar):
    return f"This is {kwar.get('name')} from {kwar.get('town') } and he is {kwar.get('age')} years old"


print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))