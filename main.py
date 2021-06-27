from tkinter import *
from tkinter import messagebox
import random
from data import data

BG = "#B1DDC6"
FONT_COLOR1 = "#A239EA"
FONT_COLOR2 = "#5C33F6"
FONT_COLOR3 = "#FF94CC"
name1 = "name"
name2 = "name"
follower_count1 = "Follower"
follower_count2 = "Follower"
score = 0
# ===================function=================
def no_compare():
    global follower_count1, follower_count2, score
    canvas.itemconfig(first_compare, text=f"{follower_count1}M")
    canvas.itemconfig(second_compare, text=f"{follower_count2}M")
    if follower_count1 < follower_count2:
        canvas.itemconfig(asking, text="You right!!")
        score += 1
        canvas.itemconfig(highscore, text=score)
        window.after(2000, func=random_compare)
    else:
        canvas.itemconfig(asking, text="Incorrect answer you lose")
        score = 0
        canvas.itemconfig(highscore, text=score)
        window.after(2000, func=random_compare)

def yes_compare():
    global follower_count1, follower_count2, score
    canvas.itemconfig(first_compare, text=f"{follower_count1}M")
    canvas.itemconfig(second_compare, text=f"{follower_count2}M")
    if follower_count1 > follower_count2 or follower_count1 == follower_count2:
        canvas.itemconfig(asking, text="You right!!")
        score += 1
        canvas.itemconfig(highscore, text=score)
        window.after(2000, func=random_compare)
    else:
        canvas.itemconfig(asking, text="Incorrect answer you lose")
        score = 0
        window.after(2000, func=random_compare)
        

def random_compare():
    global name1, name2, follower_count1, follower_count2
    canvas.itemconfig(asking, text="Is A more famous than B?")
    compare1 = random.choice(data)
    compare2 = random.choice(data)
    name1 = f"{compare1['name']}"
    name2 = f"{compare2['name']}"
    canvas.itemconfig(first_compare, text=name1)
    canvas.itemconfig(second_compare, text=name2)
    follower_count1 = compare1['follower_count']
    follower_count2 = compare2['follower_count']


# ==================working area===============
window = Tk()
window.title("higher lower")
window.config(bg=BG, padx=20, pady=20)
# ========== all text ==============
canvas = Canvas(width=800, height=526, bg=BG, highlightthickness=0)
A = canvas.create_text(200, 150, text="A", font=("ariel", 30, "italic"))
B = canvas.create_text(600, 150, text="B", font=("ariel", 30, "italic"))
first_compare = canvas.create_text(200, 260, text="Word1", font=("ariel", 30, "bold"))
second_compare = canvas.create_text(600, 260, text="Word2", font=("ariel", 30, "bold"))
highscore = canvas.create_text(400, 150, text=score, font=("ariel", 30, "bold"))
vs = canvas.create_text(400, 250, text="VS", font=("ariel", 30, "italic"))
logo = canvas.create_text(400, 50, text="Higher lower", font=("ariel", 30, "bold"))
asking = canvas.create_text(400, 420, text="Is A more famous than B?", font=("ariel", 30, "italic"))
canvas.grid(column=0, row=0, columnspan=2, sticky="EW")

# ============== images =================
yes = PhotoImage(file="images/right.png")
yes_button = Button(image=yes, command=yes_compare)
yes_button.grid(row=1, column=1)
yes_button.config(highlightthickness=0)

no = PhotoImage(file="images/wrong.png")
no_button = Button(image=no, command=no_compare)
no_button.grid(row=1, column=0)
no_button.config(highlightthickness=0)

random_compare()
window.mainloop()
