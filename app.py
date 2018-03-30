# Imports
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from random import choice
from tkinter import messagebox as msg

# Initial load variables
state = 0
totalCount = 0
totalCountU = 0
aACount = 0
aALongCount = 0
aSCount = 0
aSLongCount = 0
sSCount = 0
sSLongCount = 0
aASpacing = 1
aSSpacing = 1
sSSpacing = 1
aADefaultColor = "black"
aATriggeredColor = "black"
aSDefaultColor = "black"
aSTriggeredColor = "black"
sSDefaultColor = "black"
sSTriggeredColor = "black"
aAGenoFrequency = 0
aSGenoFrequency = 0
sSGenoFrequency = 0
aAlleleCount = 0
sAlleleCount = 0
aFrequency = 0
sFrequency = 0


# Create Instance
instance = tk.Tk()

# Add a Title
instance.title("Natural Selection Lab")

# Add the tabs
tabControl = ttk.Notebook(instance)

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text = "Allele Randomizer")
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text = "Simulation Customizer")
tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text = "Data")

tabControl.pack(expand=1, fill="both")

# Make Window Not resizable
instance.resizable(False, False)

# Add Label Frames
title = ttk.LabelFrame(tab1, text="Allele Picker")
title.grid(column = 0, row = 0, padx = 30, pady = 10)

# Add Labels

#
# Tab 1
#

# a
alleleALabel = ttk.Label(title, text="Allele A:")
alleleALabel.grid(column = 0, row = 1)
# s 
alleleSLabel = ttk.Label(title, text="Allele S:")
alleleSLabel.grid(column = 1, row = 1)
# answer
answer = ttk.Label(title, text="")
answer.grid(column = 0, row = 3)

# Count
counter = ttk.Label(title, text = '0')
counter.grid(column = 2, row = 3)


# Button Click Event
def onclick():
    # Get Allele Counts
    aCount = alleleACount.get()
    sCount = alleleSCount.get()

    # Make Sure That Both aCount and bCount are integers
    if isinstance(aCount, int) and isinstance(sCount, int):

        # Make Sure that both A and S are greater than or equal to one
        if aCount >= 1 and sCount >= 1:
            
            # Increase the total count (used in the third page)
            global totalCount
            global totalCountU
            totalCount += 1
            totalCountU += 1
            counter.configure(text=totalCount)
            # Create a blank array (representing parent population)
            alleleOdds=[]

            # Adds the number of A alleles specified in the field to the array
            for x in range(0, alleleACount.get()):
                alleleOdds.append('A')

            # Adds the number of S alleles specified in the field to the array
            for x in range(0, alleleSCount.get()):
                alleleOdds.append('S')
            
            # Randomly picks from the parent population (alleleOdds)
            choiceA = choice(alleleOdds)

            # Removes an allele for the one picked (so it can't be chosen for choiceB)
            for x in choiceA:
                if x == "A":
                    alleleOdds.pop(0)
                else:
                    alleleOdds.pop(alleleACount.get())

            # Randomly picks from the parent population (alleleodds)
            choiceB = choice(alleleOdds)

            # Orders the alleles properly (to look nice)
            if choiceA == "S":
                # Adds the alleles to the answer field (used to be empty)
                answer.configure(text='Answer: ' + choiceB + choiceA)
            else:
                # Adds the alleles to the answer field (used to be empty)
                answer.configure(text="Answer: " + choiceA + choiceB)

            # Parses to discover which colour should be used for the foreground (not going to explain this bit)
            if "{}{}".format(choiceA, choiceB) == "AA":
                if aASpacing != 0:
                    global aACount
                    aACount = aACount+1
                    if aACount == aASpacing:
                        aACount = 0
                        answer.configure(foreground = aATriggeredColor)
                        global aALongCount
                        aALongCount += 1
                    else:
                        answer.configure(foreground = aADefaultColor)
                        totalCount -= 1
                        counter.configure(text=totalCount)
                else:
                    answer.configure(foreground = aADefaultColor)
                    totalCount -= 1
                    counter.configure(text=totalCount)

            elif "{}{}".format(choiceA, choiceB) == "SS":
                if sSSpacing != 0:
                    global sSCount
                    sSCount += 1
                    if sSCount == sSSpacing:
                        sSCount = 0
                        answer.configure(foreground = sSTriggeredColor)
                        global sSLongCount
                        sSLongCount += 1
                    else:
                        answer.configure(foreground = sSDefaultColor)
                        totalCount -= 1
                        counter.configure(text=totalCount)
                else:
                    answer.configure(foreground = sSDefaultColor)
                    totalCount -= 1
                    counter.configure(text=totalCount)

            elif "{}{}".format(choiceA, choiceB) == "AS" or "{}{}".format(choiceA, choiceB) =="SA":
                if aSSpacing != 0:
                    global aSCount
                    aSCount += 1
                    if aSCount == aSSpacing:
                        aSCount = 0
                        answer.configure(foreground = aSTriggeredColor)
                        global aSLongCount
                        aSLongCount += 1
                    else:
                        answer.configure(foreground = aSDefaultColor)
                        totalCount -= 1
                        counter.configure(text=totalCount)
                else:
                    answer.configure(foreground = aSDefaultColor)
                    totalCount -= 1
                    counter.configure(text=totalCount)
            global aAGenoFrequency
            global aSGenoFrequency
            global sSGenoFrequency
            global aAlleleCount
            global sAlleleCount
            global aFrequency
            global sFrequency

            aAlleleCount = (aALongCount * 2) + aSLongCount
            sAlleleCount = (sSLongCount * 2) + aSLongCount

            aFrequency = aAlleleCount / (aAlleleCount + sAlleleCount)
            sFrequency = sAlleleCount / (aAlleleCount + sAlleleCount)

            aAGenoFrequency = aALongCount / totalCount
            aSGenoFrequency = aSLongCount / totalCount
            sSGenoFrequency = sSLongCount / totalCount

            print(aAGenoFrequency)
            print(aSGenoFrequency)
            print(sSGenoFrequency)

            totalCountLabel.configure(text = "{}".format(totalCountU))
            totalValidCountLabel.configure(text = "{}".format(totalCount))

            aACountLabel.configure(text = "{}".format(aALongCount))
            aSCountLabel.configure(text = "{}".format(aSLongCount))
            sSCountLabel.configure(text = "{}".format(sSLongCount))

            aAFrequencyData.configure(text = "{:0.2f}".format(aAGenoFrequency))
            aSFrequencyData.configure(text = "{:0.2f}".format(aSGenoFrequency))
            sSFrequencyData.configure(text = "{:0.2f}".format(sSGenoFrequency))

            aAlleleCountLabel.configure(text = "{}".format(aAlleleCount))
            sAlleleCountLabel.configure(text = "{}".format(sAlleleCount))

            aFrequencyLabel.configure(text = "{:0.2f}".format(aFrequency))
            sFrequencyLabel.configure(text = "{:0.2f}".format(sFrequency))


        # Errors if integers are less than 1
        else:
            error = "All integers must be greater than zero."
            answer.configure(text='Error: ' + error)
    # Errors if anything isnt an integer (not currently working)
    else:
        error = "All fields must be integers."
        answer.configure(text="Error: " + error)


# Adding a button
button = ttk.Button(title, text="Scramble!", command=onclick)
button.grid(column = 2, row=2)

# Adding Text Boxes
# a
alleleACount = tk.IntVar()
alleleAField = ttk.Entry(title, width = 12, textvariable = alleleACount)
alleleAField.grid(column = 0, row = 2, padx = 10)
alleleAField.focus()
# b
alleleSCount = tk.IntVar()
alleleSField = ttk.Entry(title, width = 12,  textvariable = alleleSCount)
alleleSField.grid(column = 1, row = 2, padx = 5)

# Tab Control 2 refactoring  ---------------------------------------------------------
# We are creating a container frame to hold all other widgets -- Tab2
tab2Title = ttk.LabelFrame(tab2, text='Simulation Customizer')
tab2Title.grid(column=0, row=0, padx = 30, pady=4)

aAFrequencyLabel = ttk.Label(tab2Title, text = "AA Kept Frequency (-1 if never):")
aAFrequencyLabel.grid(column = 0, row = 1, padx = 0)

aSFrequencyLabel = ttk.Label(tab2Title, text = "AS Kept Frequency (-1 if never):")
aSFrequencyLabel.grid(column = 0, row = 2, padx = 0)

sSFrequencyLabel = ttk.Label(tab2Title, text = "SS Kept Frequency (-1 if never):")
sSFrequencyLabel.grid(column = 0, row = 3, padx = 0)

aAColorLabel = ttk.Label(tab2Title, text = "AA Normal Color (g. color names):")
aAColorLabel.grid(column = 0, row = 4, padx = 0)

aSColorLabel = ttk.Label(tab2Title, text = "AS Normal Color (g. color names):")
aSColorLabel.grid(column = 0, row = 5, padx = 0)

sSColorLabel = ttk.Label(tab2Title, text = "SS Normal Color (g. color names):")
sSColorLabel.grid(column = 0, row = 6, padx = 0)

aAActiveColorLabel = ttk.Label(tab2Title, text = "AA Active Color (g. color names):")
aAActiveColorLabel.grid(column = 0, row = 7, padx = 0)

aSActiveColorLabel = ttk.Label(tab2Title, text = "AS Active Color (g. color names):")
aSActiveColorLabel.grid(column = 0, row = 8, padx = 0)

sSActiveColorLabel = ttk.Label(tab2Title, text = "SS Active Color (g. color names):")
sSActiveColorLabel.grid(column = 0, row = 9, padx = 0)





#Textboxes

aAFrequency = tk.IntVar()
aAFrequencyField = ttk.Entry(tab2Title, width = 12, textvariable = aAFrequency)
aAFrequencyField.grid(column = 2, row = 1)

aSFrequency = tk.IntVar()
aSFrequencyField = ttk.Entry(tab2Title, width = 12, textvariable = aSFrequency)
aSFrequencyField.grid(column = 2, row = 2)

sSFrequency = tk.IntVar()
sSFrequencyField = ttk.Entry(tab2Title, width = 12, textvariable = sSFrequency)
sSFrequencyField.grid(column = 2, row = 3)

aAColor = tk.StringVar()
aAColorField = ttk.Entry(tab2Title, width = 12, textvariable = aAColor)
aAColorField.grid(column = 2, row = 4)

aSColor = tk.StringVar()
aSColorField = ttk.Entry(tab2Title, width = 12, textvariable = aSColor)
aSColorField.grid(column = 2, row = 5)

sSColor = tk.StringVar()
sSColorField = ttk.Entry(tab2Title, width = 12, textvariable = sSColor)
sSColorField.grid(column = 2, row = 6)

aAActiveColor = tk.StringVar()
aAActiveColorField = ttk.Entry(tab2Title, width = 12, textvariable = aAActiveColor)
aAActiveColorField.grid(column = 2, row = 7)

aSActiveColor = tk.StringVar()
aSActiveColorField = ttk.Entry(tab2Title, width = 12, textvariable = aSActiveColor)
aSActiveColorField.grid(column = 2, row = 8)

sSActiveColor = tk.StringVar()
sSActiveColorField = ttk.Entry(tab2Title, width = 12, textvariable = sSActiveColor)
sSActiveColorField.grid(column = 2, row = 9)

# Button
def confirmsc():
    answer = msg.askyesno('Change Simulation Settings?', 'Are you sure you wish to change simulation settings? You will not be able to revert to your current settings again unless you know them.')
    if answer == True:
        global aASpacing
        global aSSpacing
        global sSSpacing
        global aADefaultColor
        global aATriggeredColor
        global aSDefaultColor
        global aSTriggeredColor
        global sSDefaultColor
        global sSTriggeredColor

        aASpacing = aAFrequency.get()
        aSSpacing = aSFrequency.get()
        sSSpacing = sSFrequency.get()

        aADefaultColor = aAColor.get()
        aSDefaultColor = aSColor.get()
        sSDefaultColor = sSColor.get()

        aATriggeredColor = aAActiveColor.get()
        aSTriggeredColor = aSActiveColor.get()
        sSTriggeredColor = sSActiveColor.get()

button2 = ttk.Button(tab2Title, text="Confirm.", command=confirmsc)
button2.grid(column=2, row = 10)

tab3Title = ttk.LabelFrame(tab3, text = "Data")
tab3Title.grid(column=0, row=0, padx = 8, pady=4)

totalCountFrame = ttk.LabelFrame(tab3Title, text = "Total Count")
totalCountFrame.grid(column=0, row=0)

totalValidCountFrame = ttk.LabelFrame(tab3Title, text = "Total Valid Count")
totalValidCountFrame.grid(column = 2, row = 0)

aACountFrame = ttk.LabelFrame(tab3Title, text = "AA Count")
aACountFrame.grid(column = 0, row = 1)

aSCountFrame = ttk.LabelFrame(tab3Title, text = "AS Count")
aSCountFrame.grid(column = 1, row = 1)

sSCountFrame = ttk.LabelFrame(tab3Title, text = "SS Count")
sSCountFrame.grid(column = 2, row = 1)

aAFrequencyFrame = ttk.LabelFrame(tab3Title, text = "AA Frequency")
aAFrequencyFrame.grid(column = 0, row = 2)

aSFrequencyFrame = ttk.LabelFrame(tab3Title, text = "AS Frequency")
aSFrequencyFrame.grid(column = 1, row = 2)

sSFrequencyFrame = ttk.LabelFrame(tab3Title, text = "SS Frequency")
sSFrequencyFrame.grid(column = 2, row = 2)

aAlleleCountFrame = ttk.LabelFrame(tab3Title, text = "A Allele Count")
aAlleleCountFrame.grid(column = 0, row = 3)

sAlleleCountFrame = ttk.LabelFrame(tab3Title, text = "S Allele Count")
sAlleleCountFrame.grid(column = 2, row = 3)

aFrequencyFrame = ttk.LabelFrame(tab3Title, text = "A Allele Frequency")
aFrequencyFrame.grid(column = 0, row = 4)

sFrequencyFrame = ttk.LabelFrame(tab3Title, text = "S Allele Frequency")
sFrequencyFrame.grid(column = 2, row = 4)

totalCountLabel = ttk.Label(totalCountFrame, text = "0")
totalCountLabel.grid()

totalValidCountLabel = ttk.Label(totalValidCountFrame, text = "0")
totalValidCountLabel.grid()

aACountLabel = ttk.Label(aACountFrame, text = "0")
aACountLabel.grid()

aSCountLabel = ttk.Label(aSCountFrame, text = "0")
aSCountLabel.grid()

sSCountLabel = ttk.Label(sSCountFrame, text = "0")
sSCountLabel.grid()

aAFrequencyData = ttk.Label(aAFrequencyFrame, text = "0")
aAFrequencyData.grid()

aSFrequencyData = ttk.Label(aSFrequencyFrame, text = "0")
aSFrequencyData.grid()

sSFrequencyData = ttk.Label(sSFrequencyFrame, text = "0")
sSFrequencyData.grid()

aAlleleCountLabel = ttk.Label(aAlleleCountFrame, text = "0")
aAlleleCountLabel.grid()

sAlleleCountLabel = ttk.Label(sAlleleCountFrame, text = "0")
sAlleleCountLabel.grid()

aFrequencyLabel = ttk.Label(aFrequencyFrame, text = "0")
aFrequencyLabel.grid()

sFrequencyLabel = ttk.Label(sFrequencyFrame, text = "0")
sFrequencyLabel.grid()

def warning():
    answer = msg.askyesno('Are you sure you would like to move on to the next generation?', 'Doing so will clear your current generation\'s data, and there will be no way to recover it.')
    if answer == True:
        global aAGenoFrequency
        global aSGenoFrequency
        global sSGenoFrequency
        global aAlleleCount
        global sAlleleCount
        global aFrequency
        global sFrequency
        global aALongCount
        global aSLongCount
        global sSLongCount
        global aACount
        global aSCount
        global sSCount
        global totalCount
        global totalCountU

        aAGenoFrequency = 0
        aSGenoFrequency = 0
        sSGenoFrequency = 0

        aAlleleCount = 0
        sAlleleCount = 0

        aFrequency = 0
        sFrequency = 0

        aALongCount = 0
        aSLongCount = 0
        sSLongCount = 0

        aACount = 0
        aSCount = 0
        sSCount = 0

        totalCount = 0
        totalCountU = 0

        totalCountLabel.configure(text = "{}".format(totalCountU))
        totalValidCountLabel.configure(text = "{}".format(totalCount))

        aACountLabel.configure(text = "{}".format(aALongCount))
        aSCountLabel.configure(text = "{}".format(aSLongCount))
        sSCountLabel.configure(text = "{}".format(sSLongCount))

        aAFrequencyData.configure(text = "{:0.2f}".format(aAGenoFrequency))
        aSFrequencyData.configure(text = "{:0.2f}".format(aSGenoFrequency))
        sSFrequencyData.configure(text = "{:0.2f}".format(sSGenoFrequency))

        aAlleleCountLabel.configure(text = "{}".format(aAlleleCount))
        sAlleleCountLabel.configure(text = "{}".format(sAlleleCount))

        aFrequencyLabel.configure(text = "{:0.2f}".format(aFrequency))
        sFrequencyLabel.configure(text = "{:0.2f}".format(sFrequency))

        counter.configure(text = totalCount)

rButton = ttk.Button(tab3Title, text = 'Next Generation', command = warning)
rButton.grid(column = 2, row = 5)

# Start the GUI
instance.mainloop()