def filled_shells(num, shells):
    shell = 2 * (len(shells) + 1)** 2
    if shell < num:
        num -= shell
        shells.append(shell)
        filled_shells(num, shells)
    else:
        shells.append(num)
        return print(shells)

electrons = int(input())
filled_shells(electrons, [])
