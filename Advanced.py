"""Program to demonstrate the use of OOP in GUI designs"""
from tkinter import *

def main():
    root = Tk()
    window1 = Window(root, "Window 1", "640x400", "Hello this is a window!")
    return None

"""
Arguments for class could be anything... i.e title, size etc
Make sure root, or top level window is passed into the init method
"""
class Window:
    n = 0 #a button will be created and increment this by 1 each time it is pressed
    def __init__(self, root, title, size, message):
        self.root = root #the instance for everthing in this window i.e use self.root if needed again!
        self.root.title(title)
        self.root.geometry(size) #input as string "size x size"
        self.label = Label(self.root, text=message)
        self.label.pack()

        b1 = ButtonWidget(root,'This is a button!', self.increment)
        self.root.mainloop()

    def increment(self):
        self.n += 1
        self.label.config(text="Count: " + str(self.n))

class ButtonWidget:
    def __init__(self, root, text, command):
        self.root = root
        self.button = Button(self.root, text=text, command=command)
        self.button.pack()


main()