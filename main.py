from tkinter import *
from tkinter.ttk import *


# Function
def clicked():
    full_name_val = txtName.get()
    print('Clicked! This is your text:', full_name_val)


root = Tk()
root.title("main page")
root.minsize(300, 300)
root.configure(bg='pink')

# creation
lbl1 = Label(root, text='Welcome', font=("Arial Bold", 14))
lbl2 = Label(root, text='Full Name:')
btn1 = Button(root, text='Click Here', command=clicked)
btn_exit = Button(root, text='Exit', command=exit)
txtName = Entry(root, width=10)
combo1 = Combobox(root)
combo1['values'] = ('none', 1, 2, 3)
combo1.current(0)       # Set default value
chk_state = BooleanVar()
chk_state.set(False)     # Set default state
chk = Checkbutton(root, text='choose', var=chk_state)
rad1 = Radiobutton(root, text='First', value=1)
rad2 = Radiobutton(root, text='Second', value=2)
rad3 = Radiobutton(root, text='Third', value=3)

# pack
lbl1.grid(row=0, column=0)
lbl2.grid(row=1, column=0)
btn1.grid(row=2, column=0)
btn_exit.grid(row=3, column=0)
txtName.grid(row=1, column=15)
combo1.grid(row=4, column=0)
chk.grid(row=5, column=0)
rad1.grid(row=6, column=0)
rad2.grid(row=6, column=5)
rad3.grid(row=6, column=15)

root.mainloop()


