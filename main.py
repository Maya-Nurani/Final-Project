from tkinter import *


# Function
def clicked():
    print('Clicked!')


root = Tk()
root.title("main page")
root.minsize(300, 300)
root.configure(bg='pink')

# creation
lbl1 = Label(root, text='Welcome')
lbl2 = Label(root, text='choose page:')
btn1 = Button(root, text='insert form', command=clicked)
btn_exit = Button(root, text='Exit', command=exit)

# pack
lbl1.grid(row=0, column=0)
lbl2.grid(row=1, column=0)
btn1.grid(row=2, column=0)
btn_exit.grid(row=3, column=0)

root.mainloop()
