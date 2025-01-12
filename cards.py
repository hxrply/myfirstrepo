import random
Suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
Num = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

#deck = []
#CardNumber = 1
#for Suit in Suits:
        #for Rank in Num:
            #Card = f"{CardNumber} {Rank} of {Suit}"
            #deck.append(Card)
            #CardNumber += 1

#for Card in deck:
    #print(Card)

#def drawc():
while True:
    drawn = input("Do you want to draw a card? ")
    if drawn == "yes":
        random_Suits = (random.choice(Suits))
        random_Num = (random.choice(Num))
        print("The card is ", random_Num, " of ", random_Suits)
    elif drawn == "no":
        print("thanks for being here!")
        break
    else:
        print("This wont work please type yes or no")

