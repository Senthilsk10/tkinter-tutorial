from tkinter import *

root = Tk()

root.title("example app")
root.geometry("480x480")

Label(root,text="label 1",bg="lightblue").pack(side="top")# expand =True occupies space
Label(root,text="label 2").pack(side="left")
Label(root,text="label 3").pack(side="right")
Button(root,text="label 4").pack(side="bottom",fill='x')# gets full width on specified cordinate - x,y,both 
Button(root,text="label 5").pack(side="top")
# we can stack the widgets one by one one top of it - if top selected element added on th etop , bottom then bottom

root.mainloop()