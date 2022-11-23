import random
from colorama import Fore

class InvalidLevelError(Exception):
    pass

try:
    level = int(input(Fore.BLUE + "Select level: "))
except ValueError:
    raise InvalidLevelError(Fore.WHITE + "The level you select isn't valid!")

if level <= 0:
    raise InvalidLevelError(Fore.WHITE + "The level you select isn't valid!")

computer_number = random.randint(1, 10 * level)
play = True

while play:

    try:
        playar_number = int(input("Guess the nnumber: "))
    except ValueError:
        print(Fore.BLUE + "Enter a number!")
        continue

    if playar_number == computer_number:
        print(Fore.GREEN + "You guessed it!")
        if input(Fore.BLUE +"Do you want to play again? [y/n] ") != "y":
            play = False 
        else:
            level += 1
            computer_number = random.randint(1, 10 * level)
    elif playar_number < computer_number:
        print(Fore.RED + "Higher")
    else:
        print(Fore.CYAN + "Lower")
