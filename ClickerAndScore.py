"""
Have a list of names. Be able to click a positive or negative button to increase or
decrease their scores.

create a Frame widget called frame, and grid it at row 1 and column 0.
Then, we grid all the other widgets inside this Frame. This should ensure that the widgets are grouped together and positioned correctly, without any extra space.
"""
import tkinter as tk
from PIL import Image, ImageTk #allows the use of an image/logo

#create window
#create window
root = tk.Tk()
root.title("Score Keeper v1.0")
root.geometry("500x300")

# create a frame to group the other widgets
frame = tk.Frame(root, padx=20, pady=20)
frame.grid(row=1, column=0)

#instructions
instructions = tk.Label(frame, text="Add a name then increase or decrease their points.")
instructions.grid(columnspan=2, column=1, row=0) #span over three columns. Middle alligned.

#Headingings and placement
"""
Creates four new label widgets inside the frame and sets their text to "NAME", "TOTAL SCORE", "POSITIVE POINT", and "NEGATIVE POINT" respectively. 
These labels are then placed in the first, second, third, and fourth columns of the second row of the grid.
"""
names = tk.Label(frame, text="NAME")
names.grid(column=0, row=1)

score = tk.Label(frame, text="TOTAL SCORE")
score.grid(column=1, row=1)

positive = tk.Label(frame, text="POSITIVE POINT")
positive.grid(column=2, row=1)

negative = tk.Label(frame, text="NEGATIVE POINT")
negative.grid(column=3, row=1)

#Names --> for loop for auto generation? --> aad button!?
"""
Creates five new label widgets inside the frame and sets their text to
"Student_1", "Student_2", "Student_3", "Student_4", and "Student_5" respectively. 
These labels are then placed in the first column of the third to seventh rows of the grid.
"""
n1 = tk.Label(frame, text="Student_1")
n1.grid(column=0, row=2)
n2 = tk.Label(frame, text="Student_2")
n2.grid(column=0, row=3)
n3 = tk.Label(frame, text="Student_3")
n3.grid(column=0, row=4)
n4 = tk.Label(frame, text="Student_4")
n4.grid(column=0, row=5)
n5 = tk.Label(frame, text="Student_5")
n5.grid(column=0, row=6)

#Total Score
"""
Creates a list called total_score_labels which holds the total score for each player. 
The list is initialized to hold five zeros. Then, for each player, a new label widget is created with the text "0" 
and placed in the second column of the corresponding row in the grid. These label widgets are then added to the total_score_labels list.
"""
total_score_labels = [] #hold score totals

for i in range(5): #generate a 0 starting score for each player and loop through each player
    total_score = tk.Label(frame, text="0") #create a label widget with initial score of 0
    total_score.grid(column=1, row=i+2) #add the label widget to the grid layout manager and set its position
    total_score_labels.append(total_score)  #add the label widget to the list of score labels for each player


#Positive point interactions
"""
Take the player's total score label as an argument. 
Do this by passing the label to the function using a lambda function in the command option of the button.
"""
def add_positive(total_score_label):
    """
    A function called add_positive that takes in one argument, total_score_label.
    This function is called when the positive button is clicked, passing in the label that displays the total score for that player
    """
    current_score = int(total_score_label["text"]) #the current score is extracted from the text property of the total_score_label using the dictionary-style indexing
    new_score = current_score + 1
    total_score_label["text"] = str(new_score)


# def add_negative(total_score_label):
#     current_score = int(total_score_label["text"])
#     if current_score > 0:
#         new_score = current_score - 1
#         total_score_label["text"] = str(new_score)

def add_negative(label):
    """
    Allows for negative numbers
    """
    current_score = int(label["text"]) # Get the current score from the label
    new_score = current_score - 1 # Subtract 1 from the current score
    label.config(text=str(new_score)) # Update the label with the new score

"""
total score label for each player is passed as an argument to the add_positive function using a lambda function. 
The lambda function takes the total score label as an argument and calls the add_positive function with that argument.

Inside the loop, a total_score_label is created and gridded at a specific location using grid(). 
The total_score_label variable is also appended to the total_score_labels list so that it can be accessed later.

A positive_button is then created using the Button widget. 
The textvariable parameter is set to positive_text, which means that the text displayed on the button will change whenever the positive_text variable is updated.

The command parameter is set to a lambda function that calls add_positive with the total_score_label passed in as an argument. 
This lambda function ensures that the correct total_score_label is passed to add_positive when the button is clicked.
"""

# Positive Button
positive_text = tk.StringVar()
positive_text.set("+")
for i in range(5):
    total_score_label = total_score_labels[i]  # Use the label object from the list
    positive_button = tk.Button(frame, textvariable=positive_text, command=lambda t=total_score_label: add_positive(t), font="Raleway", bg="green", fg="white", height=1, width=1)
    #textvariable=positive_text --> sets the text displayed on the button to the value of the positive_text variable.
    #command=lambda t=total_score_label: add_positive(t) --> sets the function to call when the button is clicked.
    # The lambda function takes the total_score_label variable as a default argument and passes it to the add_positive function.
    positive_button.grid(column=2, row=i+2)
    #places the button in the grid layout of the window. The button is placed in column 2 and row i+2.
    # The i+2 calculation ensures that each button is placed in a different row, starting with row 3

# Negative Button
negative_text = tk.StringVar()
negative_text.set("-")
for i in range(5):
    total_score_label = total_score_labels[i]  # Use the label object from the list
    negative_button = tk.Button(frame, textvariable=negative_text, command=lambda t=total_score_label: add_negative(t), font="Raleway", bg="red", fg="white", height=1, width=1 )
    negative_button.grid(column=3, row=i+2)

root.mainloop()

