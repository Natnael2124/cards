import random
cards =["jack","queen","king"]

def main():
    card = random.choices(cards,k=2)
    print(card)


main()