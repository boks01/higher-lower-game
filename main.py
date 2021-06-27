from tkinter import *
import pandas as pd

BG = "#F0D9E7"
FONT_COLOR1 = "#A239EA"
FONT_COLOR2 = "#5C33F6"
FONT_COLOR3 = "#FF94CC"
SCORE = 0
# ==================working area===============
window = Tk()
window.title("higher lower")
window.minsize(width=800, height=400)
window.config(padx=100, pady=80, bg=BG)
# ========== all text ==============
A = Label(text="A", font=("ariel", 25, "italic"), bg=BG)
A.grid(row=0, column=0)
first_compare = Button(text="First\nCompare", font=("ariel", 35, "bold"), bg=BG)
first_compare.grid(row=1, column=0)

score = Label(text=SCORE, font=("ariel", 35, "bold"), bg=BG)

vs = Label(text="VS", font=("ariel", 35, "italic"), bg=BG)
vs.grid(row=1, column=1)
vs.config(padx=40, pady=40)


B = Label(text="B", font=("ariel", 25, "italic"), bg=BG)
B.grid(row=0, column=2)
second_compare = Button(text="Second\nCompare", font=("ariel", 35, "bold"), bg=BG)
second_compare.grid(row=1, column=2)

asking = Label(text="Who's\nmore famous?", font=("ariel", 35, "italic"), bg=BG)
asking.grid(row=2, column=1)
# asking.config(pady=40)

#=================images area=============
window.mainloop()