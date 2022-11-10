def sorting_cheeses(**kwargs):
    sorted_cheeses = sorted(kwargs.items(), key = lambda kvpt: (-len(kvpt[1]), kvpt[0]))
    result = ""
    for name, value in sorted_cheeses:
        result += name +"\n"
        sorted_value = sorted(value, reverse=True   )
        result += "\n".join(map(str, sorted_value))
        result += "\n"
    return result


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135], 
        Camembert=[100, 100, 105, 500, 430], 
        Mozzarella=[50, 125],
    )
)
print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)
