from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title("Display Graphs and Charts")
root.geometry("400x200")

def plot():
    price = np.random.normal(20000, 25000, 50000)
    plt.hist(price, 50)
    plt.show()

"""Button to press to generate graph"""
my_button = Button(root, text="Graph", command=plot)
my_button.pack()


root.mainloop()
