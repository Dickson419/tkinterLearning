import tkinter as tk

# create a window
root = tk.Tk()

#size the window. geometry(x, y)
root.geometry("800x500")

#set the title
root.title("GUI")

#add labels
#1st parameter is the main window, root, 2nd what we want to display, 3rd tuple for fonts etc
label = tk.Label(root, text="Hello", font=('Arial', 18))
#place label in window
label.pack(padx=20, pady=20)

#text box
textbox = tk.Text(root, height=2, width=80, font=('Arial', 14))
textbox.pack(padx=10)

#button - funtionality added later
button = tk.Button(root, text="Click Me!", font=('Arial', 14))
button.pack(padx=10, pady=10)


#grid layout
buttonframe = tk.Frame(root) #part of root
#configure columns
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text="1")
btn1.grid(row=0, column=0, sticky=tk.W+tk.E) #sticky gives even spacing

btn2 = tk.Button(buttonframe, text="2")
btn2.grid(row=0, column=1, sticky=tk.W+tk.E) #sticky gives even spacing

btn3 = tk.Button(buttonframe, text="3")
btn3.grid(row=0, column=2, sticky=tk.W+tk.E) #sticky gives even spacing

#row 2
btn4 = tk.Button(buttonframe, text="4")
btn4.grid(row=1, column=0, sticky=tk.W+tk.E) #sticky gives even spacing
btn5 = tk.Button(buttonframe, text="5")
btn5.grid(row=1, column=1, sticky=tk.W+tk.E) #sticky gives even spacing
btn6 = tk.Button(buttonframe, text="6")
btn6.grid(row=1, column=2, sticky=tk.W+tk.E) #sticky gives even spacing

buttonframe.pack(fill="x") #fill = stretch into the x dimention

#entry - passwords/usernames
# myentry = tk.Entry(root)
# myentry.pack(padx=10, pady=10)



#display the window
root.mainloop()
