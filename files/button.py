#import tkinter as tk
from tkinter import *
root = Tk()

root.geometry("1080x720")
btn = Button(root,text="click me",command=print("clicked"))
btn.pack()
# text - keyword for what to show in the button
# command - keyword to what should be happened when the button is clicked
# pack - method for adding the button to the root frame
root.mainloop()