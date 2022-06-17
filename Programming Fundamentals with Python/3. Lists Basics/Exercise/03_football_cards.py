notebook = input().split()
a_team = 11
b_team = 11
cards = set()
for card in notebook:
    if card not in cards:
        cards.add(card)
        if card[0] == "A":
            a_team -= 1
        else:
            b_team -= 1
        if a_team < 7 or b_team < 7 :
            print(f"Team A - {a_team}; Team B - {b_team}")
            print("Game was terminated")
            break
else:
    print(f"Team A - {a_team}; Team B - {b_team}")