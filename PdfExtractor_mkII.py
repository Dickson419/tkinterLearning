from tkinter import *
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
from functions import display_logo, display_textbox, extract_images, display_icon

#IMPROVE: all functions in separate py file
#globals
page_contents = [] #store content of each page extracted
all_images = []
img_index = [0] #used to save only one image. Start with first image
displayed_image = []

#more functons
def resize_image(img):
    width, height = int(img.size[0]), int(img.size[1])
    # acount for landscape, portrate ans square
    if width > height:
        height = int(300 / width * height)
        width = 300
    elif height > width:
        width = int(250 / height * width)
        height = 250
    else:
        width, height = 250, 250
    img = img.resize((width, height))
    return img


def display_image(img):
    img = resize_image(img)
    img = ImageTk.PhotoImage(img)
    img_label = Label(image=img, bg="white")
    img_label.image = img
    img_label.grid(row=4, column=2, rowspan=2)
    return img_label


def copy_text(content):
    root.clipboard_clear() #make sure clipboard is empty
    root.clipboard_append(content[-1]) #add content

def save_all(images): #IMPROVE: can this save to a specific file?
    counter = 1 #reperensts index of each image
    for i in images:
        if i.mode != "RBG":
            i = i.convert("RGB")
        i.save("img" + str(counter) + ".png", format("png")) #png only works with cmyk -> convert to RBG for it to work universally
        counter += 1

def save_image(img): #similar to one above
    if img.mode != "RBG":
        img = img.convert("RGB")
    img.save("img.png", format("png"))  # png only works with cmyk -> convert to RBG for it to work universally

#take in a list of images and the current image
def right_arrow(all_images, current_img):
    #restrict number of button clicks to available images
    if img_index[-1] < len(all_images)-1:
        #create new index
        new_index = img_index[-1] +1
        img_index.pop()
        img_index.append(new_index)
        if displayed_image:
            displayed_image[-1].grid_forget() #mostg recent image
            displayed_image.pop()
    #create/add new image
    new_image = all_images[img_index[-1]]
    current_img = display_image(new_image)
    displayed_image.append(current_img)



root = Tk()
root.geometry('+%d+%d'%(350,10)) #place GUI at x=350, y=10

#header area - logo & browse button
header = Frame(root, width=800, height=175, bg="white")
header.grid(columnspan=3, rowspan=2, row=0)

#Header - Save
save_img = Frame(root, width=800, height=175, bg="#c8c8c8")
save_img.grid(columnspan=3, rowspan=1, row=3)

#Header - Image menu (display integer of image)
img_menu = Frame(root, width=800, height=60) #size of it
img_menu.grid(columnspan=3, rowspan=1, row=2) #size
what_img = Label(root, text="Image 1 of 5", font=("shanti", 10)) #what it says
what_img.grid(row=2, column=1) #where it goes





#main content area - text and image extraction
main_content = Frame(root, width=800, height=250, bg="#20bebe")
main_content.grid(columnspan=3, rowspan=2, row=4)

def open_file():
    browse_text.set("loading...")
    file = askopenfile(parent=root, mode='rb', filetypes=[("Pdf file", "*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfReader(file)
        page = read_pdf.pages[0]  # get the first page
        page_content = page.extract_text()
        #page_content = page_content.encode('cp1252')
        page_content = page_content.replace('\u2122', "'")
        page_contents.append(page_content)

        #extract image
        images = extract_images(page) #assign function to a variable, after text extraction!

        #extract all images into an array
        for i in images:
            all_images.append(i)

        img = images[img_index[-1]] #first image in array --> function is an array of all images in PDF

        #show current images
        current_image = display_image(img)
        displayed_image.append(current_image)

        # bring in the icons --> LEFT and RIGHT arrow images
        display_icon('arrow_l.png', 2, 0, stick=E)
        display_icon('arrow_r.png', 2, 2, stick=W)


        # Copy text, save all and save button
        copyText_btn = Button(root, text="Copy Text", command=lambda: copy_text(page_contents), font=("shanti", 10),
                              height=1, width=15)
        saveAll_btn = Button(root, text="Save All Images", command=lambda: save_all(all_images), font=("shanti", 10),
                             height=1, width=15)
        save_btn = Button(root, text="Save Image", command=lambda: save_image(all_images[img_index[-1]]),
                          font=("shanti", 10), height=1, width=15)

        # place buttons using .grid
        copyText_btn.grid(row=3, column=0)
        saveAll_btn.grid(row=3, column=1)
        save_btn.grid(row=3, column=2)


        #show text box on row 4 col 0
        display_textbox(page_content, 4, 0, root)

        #reset the button text back to Browse
        browse_text.set("Browse")

display_logo('logo.png', 0, 0)

#instructions
instructions = Label(root, text="Select a PDF file", font=("Raleway", 10), bg="white")
instructions.grid(column=2, row=0, sticky=SE, padx=75, pady=5)

#browse button
browse_text = StringVar()
browse_btn = Button(root, textvariable=browse_text, command=lambda:open_file(), font=("Raleway",12), bg="#20bebe", fg="white", height=1, width=15)
browse_text.set("Browse")
browse_btn.grid(column=2, row=1, sticky=NE, padx=50)

root.mainloop()