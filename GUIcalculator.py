import tkinter as tk

#calculation string variable
calculation = ""


def add_to_claculation(symbol):
    """Take input and use it as part of the calculation. All converted to a string"""
    global calculation #global to maniplulate the variable(above) inside of the function
    calculation += str(symbol) #everything, including ints, converted to strings

    #delete the content of the text result field
    text_result.delete(1.0, "end") #start and end. Start has to be 1.0
    text_result.insert(1.0, calculation)


def evaluate_calculation():
    global calculation
    #acount for errors in calculations
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")


def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


#window setup
root = tk.Tk()
root.geometry("300x275")

text_result = tk.Text(root, height=2, width=16, font=('Arial', 24))
text_result.grid(columnspan=5)

#button setup
btn1 = tk.Button(root, text="1", command=lambda : add_to_claculation(1), width=5, font=("Arial", 14)) #lambda so function does not run immediately
btn1.grid(row=2, column=1)

btn2 = tk.Button(root, text="2", command=lambda : add_to_claculation(2), width=5, font=("Arial", 14)) #lambda so function does not run immediately
btn2.grid(row=2, column=2)

btn3 = tk.Button(root, text="3", command=lambda : add_to_claculation(2), width=5, font=("Arial", 14)) #lambda so function does not run immediately
btn3.grid(row=2, column=3)

btn4 = tk.Button(root, text="4", command=lambda : add_to_claculation(4), width=5, font=("Arial", 14)) #lambda so function does not run immediately
btn4.grid(row=3, column=1)

btn5 = tk.Button(root, text="5", command=lambda : add_to_claculation(5), width=5, font=("Arial", 14)) #lambda so function does not run immediately
btn5.grid(row=3, column=2)

btn6 = tk.Button(root, text="6", command=lambda : add_to_claculation(6), width=5, font=("Arial", 14)) #lambda so function does not run immediately
btn6.grid(row=3, column=3)

btn7 = tk.Button(root, text="7", command=lambda : add_to_claculation(7), width=5, font=("Arial", 14)) #lambda so function does not run immediately
btn7.grid(row=4, column=1)

btn8 = tk.Button(root, text="8", command=lambda : add_to_claculation(8), width=5, font=("Arial", 14)) #lambda so function does not run immediately
btn8.grid(row=4, column=2)

btn9 = tk.Button(root, text="9", command=lambda : add_to_claculation(9), width=5, font=("Arial", 14)) #lambda so function does not run immediately
btn9.grid(row=4, column=3)

btn0 = tk.Button(root, text="0", command=lambda : add_to_claculation(0), width=5, font=("Arial", 14)) #lambda so function does not run immediately
btn0.grid(row=5, column=2)

btn_plus = tk.Button(root, text="+", command=lambda : add_to_claculation("+"), width=5, font=("Arial", 14)) #lambda so function does not run immediately
btn_plus.grid(row=2, column=4)

btn_sub = tk.Button(root, text="-", command=lambda : add_to_claculation("-"), width=5, font=("Arial", 14)) #lambda so function does not run immediately
btn_sub.grid(row=3, column=4)

btn_mul = tk.Button(root, text="*", command=lambda : add_to_claculation("*"), width=5, font=("Arial", 14)) #lambda so function does not run immediately
btn_mul.grid(row=4, column=4)

btn_div = tk.Button(root, text="/", command=lambda : add_to_claculation("/"), width=5, font=("Arial", 14)) #lambda so function does not run immediately
btn_div.grid(row=5, column=4)

btn_open = tk.Button(root, text="(", command=lambda : add_to_claculation("("), width=5, font=("Arial", 14)) #lambda so function does not run immediately
btn_open.grid(row=5, column=1)

btn_close = tk.Button(root, text=")", command=lambda : add_to_claculation(")"), width=5, font=("Arial", 14)) #lambda so function does not run immediately
btn_close.grid(row=5, column=2)

btn_equals = tk.Button(root, text="=", command= evaluate_calculation, width=12, font=("Arial", 14)) #lambda so function does not run immediately
btn_equals.grid(row=6, column=1, columnspan=2)#evaluate_calculation NO paraenthesis as we do not want to call it...

btn_clear = tk.Button(root, text="C", command=clear_field, width=12, font=("Arial", 14))
btn_clear.grid(row=6, column=3, columnspan=2) #clear_field NO paraenthesis as we do not want to call it...




#run mainloop/display screen
root.mainloop()
