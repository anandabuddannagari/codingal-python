#Import necessary Libraries
from tkinter import *

#Create window
root = Tk()
root.title('number pad')
root.geometry("250x300")

#Create a frame to organize elements better
#Frame = Frame(master = root, height = 2--, width = 360, bg = "#d0efff")

nums = [[9, 8, 7], [6, 5, 4], [3 ,2, 1], ['#', 0, '*']]

for i in range(4):
    #Configure rows and collumns to resize window
    root.columnconfigure(i, weight=1, minsize=75)
    root.rowconfigure(i, weight=1, minsize=50)
    for j in range(0, 3):
        frame = Frame(
            master = root,
            relief = SUNKEN,
            borderwidth=1
        )
        frame.grid(row=i, column=j,sticky="nsew")
        label = Label(master = frame, text = nums[i][j], bg='#d0efff')
        label.pack(padx=3, pady=3)

#Start the Gui event loop
root.mainloop()