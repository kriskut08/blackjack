import random
import time
import os
from tkinter import *

# DEFAULT VALUES UWU

chips = 1000
deck = ["club_2","club_3","club_4","club_5","club_6","club_7","club_8","club_9","club_10","club_J","club_Q","club_K","club_A",
        "spade_2","spade_3","spade_4","spade_5","spade_6","spade_7","spade_8","spade_9","spade_10","spade_J","spade_Q","spade_K","spade_A",
        "diamond_2","diamond_3","diamond_4","diamond_5","diamond_6","diamond_7","diamond_8","diamond_9","diamond_10","diamond_J","diamond_Q","diamond_K","diamond_A",
        "heart_2","heart_3","heart_4","heart_5","heart_6","heart_7","heart_8","heart_9","heart_10","heart_J","heart_Q","heart_K","heart_A"]
currentDeck = []
playerCards = []
dealerCards = []
player_value = 0
dealer_value = 0
bet = 0

# GUI UWU

#window = Tk()
#Icon = PhotoImage(file="Icon.png")
#window.geometry("800x600")
#window.resizable(False, False)
#window.iconphoto(True,Icon)
#window.title("Blackjack")

# FUNCTIONS UWU

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def givePlayerCard():
    random_card = random.randint(0,len(deck)-1)
    playerCards.append(deck[random_card])
    deck.remove(deck[random_card])
    updatePlayerValue()

def giveDealerCard():
    random_card = random.randint(0,len(deck)-1)
    dealerCards.append(deck[random_card])
    deck.remove(deck[random_card])
    updateDealerValue()

def updatePlayerValue():
    global player_value

    player_value = 0
    for i in playerCards:
        if i[-1] == "A":
            player_value += 11
        elif i[-1] == "J":
            player_value += 10
        elif i[-1] == "Q":
            player_value += 10
        elif i[-1] == "K":
            player_value += 10
        elif i[-1] == "0":
            player_value += 10
        else:
            player_value += int(i[-1])

    for i in playerCards:
        if i[-1] == "A" and player_value > 21:
            player_value -= 10

def updateDealerValue():
    global dealer_value

    dealer_value = 0
    for i in dealerCards:
        if i[-1] == "A":
            dealer_value += 11
        elif i[-1] == "J":
            dealer_value += 10
        elif i[-1] == "Q":
            dealer_value += 10
        elif i[-1] == "K":
            dealer_value += 10
        elif i[-1] == "0":
            dealer_value += 10
        else:
            dealer_value += int(i[-1])

    for i in dealerCards:
        if i[-1] == "A" and dealer_value > 21:
            dealer_value -= 10

def checkWinner():
    global chips
    global bet
    global dealer_value
    global player_value


    if player_value == dealer_value:
        chips = chips + bet
        print("Draw")
    
    elif player_value > 21:
        print("You busted")

    elif player_value == 21 and len(playerCards) == 2:
        chips = chips + bet*3
        print("Blackjack")

    elif player_value > dealer_value:
        chips = chips + bet*2
        print("You won")

    else:
        print("You lost")

def Game():
    global bet
    global chips #nom nom nom :D UWU
    global playerCards
    global player_value
    global dealerCards
    global dealer_value
    global deck
    global currentDeck

    currentDeck = deck
    playerCards = []
    dealerCards = []

    if chips > 0:
        bet = int(input("How much do u want to bet? -> "))
    else:
        print("U RAN OUT OF CHIPS LOL")
        quit()
    chips -= bet

    cls()

    print("Bet: " + str(bet))
    print("Chips: " + str(chips))

    #give the player 2 cards, who would have guessed? UWU
    for i in range(2):
        givePlayerCard()
    
    #give the dealer 2 cards, who would have guessed? UWU
    for i in range(2):
        giveDealerCard()

    print("Player: " + str(playerCards))
    print("Dealer: " + str(dealerCards))

    #detect blackjacks UWU
    if player_value == 21 and len(playerCards) == 2:
        checkWinner()
        return
        
    elif dealer_value == 21 and len(dealerCards) == 2:
        checkWinner()
        return
    
    # main loop UWU
    while True:
        wantNewCard = input("Want a new card? (Y/N) -> ")
        if wantNewCard == "Y":
            cls()
            givePlayerCard()
            print("Player: " + str(playerCards))

            if player_value > 21:
                checkWinner()
                Game()
        
        elif wantNewCard == "N":
            while dealer_value < 17:
                cls()
                giveDealerCard()
                print("Dealer: " + str(dealerCards))
            else:
                checkWinner()
                Game()


cls()

Game()

#window.mainloop()