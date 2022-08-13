import random
import time
import os
from tkinter import *

# DEFAULT VALUES

chips = 1000
deck = ["club_2","club_3","club_4","club_5","club_6","club_7","club_8","club_9","club_10","club_J","club_Q","club_K","club_A",
        "spade_2","spade_3","spade_4","spade_5","spade_6","spade_7","spade_8","spade_9","spade_10","spade_J","spade_Q","spade_K","spade_A",
        "diamond_2","diamond_3","diamond_4","diamond_5","diamond_6","diamond_7","diamond_8","diamond_9","diamond_10","diamond_J","diamond_Q","diamond_K","diamond_A",
        "heart_2","heart_3","heart_4","heart_5","heart_6","heart_7","heart_8","heart_9","heart_10","heart_J","heart_Q","heart_K","heart_A"]
deck_value = ["2","3","4","5","6","7","8","9","10","10","10","10","11"]*4
playerChards = []
dealerChards = []

# GUI

window = Tk()
Icon = PhotoImage(file="Icon.png")
window.geometry("800x600")
window.resizable(False, False)
window.iconphoto(True,Icon)
window.title("Blackjack")

# FUNCTIONS

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def givePlayerCard():
    random_card = random.randint(0,len(deck)-1)
    playerChards.append(deck[random_card])
    deck.remove(deck[random_card])
    deck_value.remove(deck_value[random_card])

def giveDealerCard():
    random_card = random.randint(0,len(deck)-1)
    dealerChards.append(deck[random_card])
    deck.remove(deck[random_card])
    deck_value.remove(deck_value[random_card])

def getPlayerValue():
    player_value = 0
    for i in playerChards:
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

    for i in playerChards:
        if i[-1] == "A" and player_value > 21:
            player_value -= 10
    
    return player_value

def getDealerValue():
    dealer_value = 0
    for i in dealerChards:
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
    for i in dealerChards:
        if i[-1] == "A" and dealer_value > 21:
            dealer_value -= 10
    return dealer_value


def checkWinner():
    global chips

    if getPlayerValue() > 21:
        chips = chips - bet
        print("You lost")
    elif getDealerValue() > 21:
        chips = chips + bet
        print("You won")
    elif getPlayerValue() == dealer_value:
        print("Draw")
    elif getPlayerValue() > dealer_value:
        chips = chips + bet
        print("You won")
    else:
        chips = chips - bet
        print("You lost")


cls()




window.mainloop()