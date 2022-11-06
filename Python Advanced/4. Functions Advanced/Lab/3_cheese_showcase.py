def sorting_cheeses(**kwargs):
    kwargs = sorted(kwargs.items())
    for key, value in kwargs.items():
        print(key)
        pieces = sorted(value, reverse=True)
        for el in pieces:
            print(el)


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
