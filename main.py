from tkinter import *
import random
from data import data

BG = "#F0D9E7"
FONT_COLOR1 = "#A239EA"
FONT_COLOR2 = "#5C33F6"
FONT_COLOR3 = "#FF94CC"
SCORE = 0
name1 = ""
name2 = ""
#===================function=================
def random_compare():
    global name1,name2
    compare1 = random.choice(data)
    compare2 = random.choice(data)
    name1 = f"{compare1['name']}" 
    name2 = f"{compare2['name']}"
    first_compare.config(text=name1)
    second_compare.config(text=name2)
    folower_count1 = compare1['follower_count']
    folower_count2 = compare2['follower_count']
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
second_compare = Button(text="Second\nCompare", font=("ariel", 35, "bold"), bg=BG, command=compare)
second_compare.grid(row=1, column=2)

asking = Label(text="Who's\nmore famous?", font=("ariel", 35, "italic"), bg=BG, command=compare)
asking.grid(row=2, column=1)
# asking.config(pady=40)

random_compare()
window.mainloop()