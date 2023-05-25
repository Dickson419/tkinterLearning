import tkinter as tk
#from functions import *

def toggle_menu_display():
    def collapse_toggle_menu():
        toggle_menu_frame.destroy() #change icon
        toggle_button.configure(text="☰")
        toggle_button.configure(command=toggle_menu_display) #place original icon back
        #END INNTER FUNCTION

    #menu frame
    toggle_menu_frame = tk.Frame(root, bg="#158aff")
    window_height = root.winfo_height()
    toggle_menu_frame.place(x=0,y=50,height=window_height,width=200) #y=parent_frame.configure (head_frame)
    toggle_button.configure(text="X") #once menu is opened icon becomes a X
    toggle_button.configure(command=collapse_toggle_menu) #call nested function
    #buttons for menu options
    home_button = tk.Button(toggle_menu_frame, text="Home", bg="#158aff",fg="white", font=("bold",20),
                          bd=0, activebackground="#158aff", activeforeground="white")
    home_button.place(x=20, y=20)
    products_button = tk.Button(toggle_menu_frame, text="Products", bg="#158aff", fg="white", font=("bold", 20),
                            bd=0, activebackground="#158aff", activeforeground="white")
    products_button.place(x=20, y=80)
    feedback_button = tk.Button(toggle_menu_frame, text="Feedback", bg="#158aff", fg="white", font=("bold", 20),
                            bd=0, activebackground="#158aff", activeforeground="white")
    feedback_button.place(x=20, y=140)
    about_button = tk.Button(toggle_menu_frame, text="About", bg="#158aff", fg="white", font=("bold", 20),
                            bd=0, activebackground="#158aff", activeforeground="white")
    about_button.place(x=20, y=200)
    #END OUTER FUNCTION


"""Create main window"""
root = tk.Tk()
root.geometry("800x600")
root.title("Toggle Fun")

"""Create frame to appear at the top of the window. .pack and .configure and be edited to show frame left/right (LEFT/Y)(width)"""
head_frame = tk.Frame(root, bg="#158aff", #frame is given a blue background color
                      highlightbackground="white", highlightthickness=1) #frame is given a border colour
head_frame.pack(side=tk.TOP, fill=tk.X) #and is set to fill the X-axis
head_frame.pack_propagate(False) #frame will maintain its size even if widgets are added or removed
head_frame.configure(height=50) # frame will have a fixed height of 50 pixels, regardless of the size of its contents



"""Toggle button creation"""
toggle_button = tk.Button(head_frame, text="☰", bg="#158aff", fg="white", font=("bold",20),
                          bd=0, activebackground="#158aff", activeforeground="white",
                          command=toggle_menu_display) #bd = border width. 0 = no border
toggle_button.pack(side=tk.LEFT)

"""Title"""
title_label = tk.Label(head_frame, text="Toggle Fun",
                       bg="#158aff", fg="white", font=("bold", 20),
                       bd=0, activebackground="#158aff", activeforeground="white"
                       ) #match colour etc from the button details
title_label.pack(side=tk.LEFT)

"""Toggle Drop Down Menu - need to create a frame and then resize it"""

# place in function to see frame when toggle button clicked - toggle_menu_display() --> place in toggle_button, command=
#create an inner function to collapese the menu

"""Menu Buttons"""
#in display function

main_frame = tk.Frame(root,bg="light blue",highlightbackground="black", highlightthickness=1)
main_frame.pack(side=tk.RIGHT, fill=tk.BOTH,expand=True) #fill to see frame (border). Expand = fill screen
main_frame.pack_propagate(False)
main_frame.configure(height=800, width=600)

"""Change Pages"""
"""Pages frame variables"""
pages = [page_1, page_2, page_3, page_4]
count = 0

def move_next_page():
    global count
    if not count > len(pages)-2:
        for p in pages:
            p.pack_forget() #hides current page
        count += 1
        page = pages[count]
        page.pack(pady=10)

def move_back_page():
    global count
    if not count == 0:
        for p in pages:
            p.pack_forget()
        count -= 1
        page = pages[count]
        page.pack(pady=10)




root.mainloop()