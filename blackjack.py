import random
import time
import os
from tkinter import *

# DEFAULT VALUES

chips = 1000
deck = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]*4
deck_value = ["2","3","4","5","6","7","8","9","10","10","10","10","11"]*4
playerChards = []
dealerChards = []

# GUI

window = Tk()
Icon = PhotoImage(file="icon.png")

window.geometry("800x600")
window.resizable(False, False)
window.iconphoto(True,Icon)
window.title("Blackjack")

# FUNCTIONS

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

os.system("cls")

givePlayerCard()
givePlayerCard()

window.mainloop()