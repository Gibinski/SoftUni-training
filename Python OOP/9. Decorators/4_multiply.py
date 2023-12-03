def multiply(num):
    def decorator(func):
        def wrapper(number):
            return func(number) * num
        return wrapper
    return decorator


@multiply(3)
def add_ten(number):
    return number + 10

print(add_ten(3))


@multiply(5)
def add_ten(number):
    return number + 10

print(add_ten(6))
