from tkinter import *
import random
from data import data

BG = "#B1DDC6"
FONT_COLOR1 = "#A239EA"
FONT_COLOR2 = "#5C33F6"
FONT_COLOR3 = "#FF94CC"
SCORE = 0
name1 = ""
name2 = ""
folower_count1 = ""
folower_count2  = ""
#===================function=================
def no_compare():
    global folower_count1, folower_count2
    first_compare.config(text=f"{folower_count1}M")
    second_compare.config(text=f"{folower_count2}M")
    if folower_count1 < folower_count2:
        asking.config(text="You right!!")
    else:
        asking.config(text="Incorrect answer\nyou lose")

def yes_compare():
    global folower_count1, folower_count2
    first_compare.config(text=f"{folower_count1}M")
    second_compare.config(text=f"{folower_count2}M")
    if folower_count1 > folower_count2 or folower_count1 == folower_count2:
        asking.config(text="You right!!")
    else:
        asking.config(text="Incorrect answer\nyou lose")
def random_compare():
    global name1, name2, folower_count1, folower_count2 
    first_compare.config(text=name1)
    second_compare.config(text=name2)
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
window.config(padx=100, pady=80, bg=BG)
# ========== all text ==============
A = Label(text="A", font=("ariel", 25, "italic"), bg=BG)
A.grid(row=0, column=0)
first_compare = D=Label(text="First\nCompare", font=("ariel", 35, "bold"), bg=BG)
first_compare.grid(row=1, column=0)

score = Label(text=SCORE, font=("ariel", 35), bg=BG)
score.grid(row=0, column=1)

vs = Label(text="VS", font=("ariel", 35, "italic"), bg=BG)
vs.grid(row=1, column=1)
vs.config(padx=40, pady=40)


B = Label(text="B", font=("ariel", 25, "italic"), bg=BG)
B.grid(row=0, column=2)
second_compare = Label(text="Second\nCompare", font=("ariel", 35, "bold"), bg=BG)
second_compare.grid(row=1, column=2)

asking = Label(text="Is A more\nfamous than B?", font=("ariel", 35, "italic"), bg=BG)
asking.grid(row=2, column=1)

# asking.config(pady=40)
#============== images =================
yes = PhotoImage(file="images/right.png")
yes_button = Button(image=yes, command=yes_compare)
yes_button.grid(row=3, column=2)
yes_button.config(highlightthickness=0)

no = PhotoImage(file="images/wrong.png")
no_button = Button(image=no, command=no_compare)
no_button.grid(row=3, column=0)
no_button.config(highlightthickness=0)

random_compare()
window.mainloop()