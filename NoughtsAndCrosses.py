from tkinter import *
import random

#functions
from typing import List


def next_turn(row, column):
    """Determine whos turn it is to go and if the game has been won or drawn"""
    global player #access to player
    #check if position/button is empty. Third operator to access text of a button
    #--> if the text of a button that we click is equal to...
    if buttons[row][column]["text"] == "" and check_winner() is False:
        #IF these conditions are true fill button/boz with players symbol
        if player == players[0]:
            buttons[row][column]["text"] = player #place text of player i.e O or X
            #IF no winner switch players
            if check_winner() is False:
                player = players[1]
                label.configure(text=(players[1]+" turn")) #label updated to show current player

            elif check_winner() is True:
                label.configure(text=(players[0] + " IS VICTORIOUS! Glory to Rome"))  # label updated to show current player

            elif check_winner() == "tie":
                label.configure(text=("Tie, I see TWO losers!"))  # label updated to show current player
        else:
            # IF these conditions are true fill button/boz with players symbol
            buttons[row][column]["text"] = player  # place text of player i.e O or X
            # IF no winner switch players
            if check_winner() is False:
                player = players[0]
                label.configure(text=(players[0] + " turn"))  # label updated to show current player

            elif check_winner() is True:
                label.configure(
                    text=(players[1] + " IS VICTORIOUS!"))  # label updated to show current player

            elif check_winner() == "tie":
                label.configure(text=("Tie, I see TWO losers!"))  # label updated to show current player

def check_winner():
    """Check all different win conditions: horizontal, vertical, diagonal..."""
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            return True

    for column in range(3):
        if buttons[0][column]["text"] == buttons[1][column]["text"] == buttons[2][column]["text"] != "":
            return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    elif buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True

    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"
    else:
        return False


def empty_spaces():
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]["text"] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True


def new_game():
    global player
    player = random.choice(players)
    label.config(text=player + " turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="")

#create window
window = Tk()
window.title("Noughts & Crosses") #name window

players = ["x", "o"]

#select a random player to begin
player = random.choice(players)

#2d list to hold board
buttons = [[0,0,0,],
           [0,0,0,],
           [0,0,0,]]

#label for whos turn it is
label = Label(text=player + "'s Turn", font=("Raleway", 40))
label.pack(side="top")

"""
----- Pack -----
pack() method places a widget in a block or side-by-side manner. 
You can use the side parameter to specify whether the widget should be packed
to the left (LEFT), right (RIGHT), top (TOP), or bottom (BOTTOM) of its parent widget. 
The fill parameter specifies how the widget should expand to fill the available space, 
and the expand parameter indicates whether the widget should expand when the parent widget is resized.
"""

#reset button
reset_button = Button(text="Restart", font=("Raleway", 20), command=new_game)
reset_button.pack(side="top")

#Frame to organise other widgets
frame = Frame(window) #frame is being added to the window
frame.pack()

#generate board with nested loops
for row in range(3): #make the row
    for column in range(3): #label and make columns with buttons
        # add button to the frame, text, font, width, height
        buttons[row][column] = Button(frame, text="", font=("Raleway", 30), width=5, height=2, command=lambda row=row, column=column: next_turn(row,column))
        # lambda --> function on the fly. Take something and return a result
        # lambda arguments: expression
        buttons[row][column].grid(row=row, column=column) #add buttons to frame




window.mainloop()
