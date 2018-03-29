# Imports
import tkinter as tk
from tkinter import ttk
from random import choice

# Initial load variables
state = 0
acounting = 0

# Create Instance
instance = tk.Tk()

# Add a Title
instance.title("Bio Lab Virtualified")

# Make Window Not resizable
instance.resizable(False, False)

# Add Labels
# title
title = ttk.Label(instance, text="Bio Allele Picker")
title.grid(column=0, row=0)
# a
alleleALabel = ttk.Label(instance, text="Allele A:")
alleleALabel.grid(column = 0, row = 1)
# s 
alleleSLabel = ttk.Label(instance, text="Allele S:")
alleleSLabel.grid(column = 1, row = 1)
# answer
answer = ttk.Label(instance, text="")
answer.grid(column = 0, row = 4)

# Button Click Event
def onclick():
    aCount = alleleACount.get()
    bCount = alleleSCount.get()
    if isinstance(aCount, int) and isinstance(bCount, int):
        global acounting
        if aCount >= 1 and bCount >= 1:
            alleleOdds=[]
            for x in range(0, alleleACount.get()):
                alleleOdds.append('A')
            for x in range(0, alleleSCount.get()):
                alleleOdds.append('S')
            choiceA = choice(alleleOdds)
            for x in choiceA:
                if x == "A":
                    alleleOdds.pop(0)
                else:
                    alleleOdds.pop(alleleACount.get())
            choiceB = choice(alleleOdds)
            answer.configure(foreground = "black")
            if choiceA == "S":
                answer.configure(text='Answer: ' + choiceB + choiceA)
            else:
                answer.configure(text="Answer: " + choiceA + choiceB)
            if "{}{}".format(choiceA, choiceB) == "AA":
                acounting = acounting + 1
                if acounting == 2:
                    acounting = 0
                    answer.configure(foreground = "green")
                else:
                    answer.configure(foreground = "red")
        else:
            error = "All integers must be greater than zero."
            answer.configure(text='Error: ' + error)
    else:
        error = "All fields must be integers."
        answer.configure(text="Error: " + error)


# Adding a button
button = ttk.Button(instance, text="Scramble!", command=onclick)
button.grid(column = 2, row=2)

# Adding Text Boxes
# a
alleleACount = tk.IntVar()
alleleAField = ttk.Entry(instance, width = 12, textvariable = alleleACount)
alleleAField.grid(column = 0, row = 2)
alleleAField.focus()
# b
alleleSCount = tk.IntVar()
alleleSField = ttk.Entry(instance, width = 12,  textvariable = alleleSCount)
alleleSField.grid(column = 1, row = 2)

# Start the GUI
instance.mainloop()