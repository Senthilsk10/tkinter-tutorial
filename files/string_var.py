from tkinter import *
root = Tk()

root.title("example app")
root.geometry("720x480")

result = StringVar()
x = StringVar()
y = StringVar()

def calculate(*args):
    op1 = int(x.get())
    op2 = int(y.get())
    result.set(op1+op2)
    

operand1 = Entry(root,textvariable=x).pack()
operand2 = Entry(root,textvariable=y).pack()
btn = Button(root,text = "calculate",command=calculate).pack()
lb = Label(root,textvariable=result).pack()
root.mainloop()
