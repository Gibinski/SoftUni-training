deck = input().split()
n = int(input())
for _ in range(n):
    final_deck = []
    deck_left = deck[:len(deck) // 2]
    deck_right = deck[len(deck) // 2:len(deck)]
    for card in range(len(deck_left)):
        final_deck.append(deck_left[card])
        final_deck.append(deck_right[card])           
    deck = final_deck

print(deck)        