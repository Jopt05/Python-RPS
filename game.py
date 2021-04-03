import random
import os
import sys
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def resource_path(relative_path):
     if hasattr(sys, '_MEIPASS'):
         return os.path.join(sys._MEIPASS, relative_path)
     return os.path.join(os.path.abspath("."), relative_path)

plays = {
    1 : "Rock",
    2 : "Paper",
    3 : "Scissors"
}

score = 0

# Functions
def play(optionSelected):
    word = ''
    aiSelection = random.randint(1,3)
    aiFrame.config(image=playsImages.get(aiSelection))
    userFrame.config(image=playsImages.get(optionSelected))
    if optionSelected == aiSelection:
        word = "Same!"
    elif (optionSelected == 1 and aiSelection == 3) or (optionSelected == 3 and aiSelection == 2) or (optionSelected == 2 and aiSelection == 1):
        word = "You won!"
        global score
        score += 1
    else:
        word = "You lose!"
    titleLabel.config(text=word)
    scoreLabel.config(text="Your score is: {}".format(score))
    
    

main = tk.Tk()
main.resizable(False, False)
main.geometry("400x450")
main.title("Rock, Papper & Scissors")

test = Image.open(resource_path("sc.png"))
test = test.resize((100,100), Image.ANTIALIAS)
Scissors = ImageTk.PhotoImage(test)

test = Image.open(resource_path("rock.png"))
test = test.resize((100,100), Image.ANTIALIAS)
Rock = ImageTk.PhotoImage(test)

test = Image.open(resource_path("paper.png"))
test = test.resize((100,100), Image.ANTIALIAS)
Paper = ImageTk.PhotoImage(test)

test = Image.open(resource_path("vs.png"))
test = test.resize((100,100), Image.ANTIALIAS)
vs = ImageTk.PhotoImage(test)

playsImages = {
    1 : Rock,
    2 : Paper,
    3 : Scissors
}

main.columnconfigure(0, weight=1)
main.columnconfigure(1, weight=1)
main.columnconfigure(2, weight=1)
main.rowconfigure(0, weight=1)
main.rowconfigure(1, weight=2)
main.rowconfigure(2, weight=1)

titleFrame = tk.Frame(main)
titleFrame.grid(row=0, column=0, sticky="nsew", columnspan=3)

userFrame = tk.Label(main, image=Scissors)
userFrame.grid(row=1, column=0, sticky="nsew")

vsFrame = tk.Label(main, image=vs)
vsFrame.grid(row=1, column=1, sticky="nsew")

aiFrame = tk.Label(main, image=Rock)
aiFrame.grid(row=1, column=2, sticky="nsew")

buttonsFrame = tk.Frame(main)
buttonsFrame.grid(row=2, column=0, sticky="nsew", columnspan=3)

titleLabel = tk.Label(titleFrame, text="Welcome to my game!", font=("Arial", 15))
titleLabel.pack(expand="yes")

rockButton = tk.Button(buttonsFrame, text="Rock", width="20", command=lambda: play(1), font=("Arial", 12))
rockButton.pack(anchor="center", pady=10)

papperButton = tk.Button(buttonsFrame, text="Paper", width="20", command=lambda: play(2), font=("Arial", 12))
papperButton.pack(anchor="center", pady=10)

scissorsButton = tk.Button(buttonsFrame, text="Scissors", width="20", command=lambda: play(3), font=("Arial", 12))
scissorsButton.pack(anchor="center", pady=10)

scoreLabel = tk.Label(buttonsFrame, text="Your score is: {}".format(score), font=("Arial", 15))
scoreLabel.pack(anchor="center", pady=10)

main.mainloop()