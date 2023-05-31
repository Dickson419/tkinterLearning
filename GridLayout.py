"""Program to demonstrate the grid layout design"""
import tkinter as tk
from tkinter import ttk


root = tk.Tk()

#--------------------- Styling
s = ttk.Style()
s.configure("mainFrame.TFrame", background='#9DB2BF') #use colourhunt.com. Include the # at the start or it will be black
s2 = ttk.Style()
s2.configure("frame2.TFrame", background='#F2BED1')
s3 = ttk.Style()
s3.configure("frame3.TFrame", background='#E8AA42')
s4 = ttk.Style()
s4.configure("frame4.TFrame", background='#F266AB')

s.configure("horizontal.TFrame", background='#0C134F')
s.configure("vertical.TFrame", background='#1D267D')


#--------------------- Widgets
"""
sticky takes a string of letters 'nesw'. Adjust up/down/left/right. Each side of grid is nesw.
Using ew can expand a widget to the whole space!
ColumnSpan allows for one widget to take up multiple columns instead of just making a single column wider

"""
mainFrame = ttk.Frame(root, width=250, height=250, style='mainFrame.TFrame') #bue
mainFrame.grid(row=0,column=0,sticky='nesw')

frame2 = ttk.Frame(root, width=200,height=200, style='frame2.TFrame') #light pink
frame2.grid(row=1,column=0,sticky='nesw') #rows and columns fit to size they are not set

frame3 = ttk.Frame(root, width=250,height=250, style='frame3.TFrame') #orange
frame3.grid(row=0,column=1,sticky='nesw')

frame4 = ttk.Frame(root, width=150,height=100, style='frame4.TFrame') #bright pink
frame4.grid(row=1,column=1, sticky='nesw') #rows and columns fit to size they are not set

horizontal = ttk.Frame(root, width=500,height=100,style='horizontal.TFrame')
horizontal.grid(row=2, column=0, columnspan=2,sticky='ew')

vertical = ttk.Frame(root, width=100,height=450,style='vertical.TFrame')
vertical.grid(row=0, column=0, rowspan=2,sticky='nsw')





#--------------------- Grid configure
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)





#root.resizable(width=False,height=False) #if false user cannot resize
root.mainloop()