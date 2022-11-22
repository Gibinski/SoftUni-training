def concatenate(*args, **kwargs):
    word = "".join(args)
    for key, val in kwargs.items():
        word = word.replace(key, val)

    return word


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))