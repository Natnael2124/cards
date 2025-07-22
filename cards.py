import random
cards =["jack","queen","king"]

def main():
    random.seed(2)
    card = random.choices(cards,weights=[50,25,25],k=2)
    print(card)


main()