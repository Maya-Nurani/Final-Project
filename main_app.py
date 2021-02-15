from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

import tkinter.filedialog as FD


def setMenu(page):
    # TODO : Make the menu function (it has only labels for now)
    menubar = Menu(home_page)
    menubar.add_command(label="Homepage")
    menubar.add_command(label="Personal Details", command=open_details_page)
    menubar.add_command(label="Contacts", command=clicked())
    menubar.add_command(label="Contact Locations", command=clicked())
    menubar.add_command(label="Close", command=home_page.quit())

    home_page.config(menu=menubar)

def sendCallBack():
    messagebox.showinfo('confirmation','Action success')
    # TODO: maybe we can close details page after the message :)



def open_details_page():
    #personal_details = Toplevel(home_page)
    # Personal details
    personal_details = Tk()
    personal_details.title("Personal Details")
    personal_details.minsize(300, 300)
    personal_details.configure(bg='white')
    main_title_PD = Label(personal_details,
                          text='Personal Details:\n Please fill in the following details according to the format',
                          font=("Arial Bold", 10))

    btn_exit = Button(personal_details, text='Exit', command=exit)

    # Full Name field
    lbl_full_name = Label(personal_details, text='Full Name:')
    txt_full_name = Entry(personal_details, width=10)

    # Age (Can be as 'date of birth' and split by Year-Month-Day)
    lbl_age = Label(personal_details, text='Age')
    txt_age = Entry(personal_details, width=5)
    # numeric_age = int(txt_age.get())

    # City field
    combo_city = Combobox(personal_details)
    combo_city['values'] = (None, 'Tel-Aviv', 'Jerusalem', 'Ramat-Gan', 'Haifa', 'Yavne')
    combo_city.current(0)  # Set default value

    # Gender
    lbl_gender = Label(personal_details, text='Gender')
    rad_male = Radiobutton(personal_details, text='Male', value=1)
    rad_female = Radiobutton(personal_details, text='Female', value=2)

    # TODO: 'Click Here' or actually - 'save' button - will save the data into file (text file?)
    btn_send = Button(personal_details, text='Send', command=sendCallBack)

    main_title_PD.grid(row=0, column=0)
    lbl_full_name.grid(row=1, column=0)
    txt_full_name.grid(row=1, column=15)
    lbl_age.grid(row=2, column=0)
    txt_age.grid(row=2, column=15)

    btn_send.grid(row=3, column=0)

    btn_exit.grid(row=10, column=0)

    combo_city.grid(row=4, column=0)

    lbl_gender.grid(row=6, column=0)
    rad_male.grid(row=6, column=5)
    rad_female.grid(row=6, column=15)

    #personal_details.mainloop()


def clicked():
    # full_name_val = txt_full_name.get()
    print('Clicked!')


# Home page - our main page, from this page the user can navigate between pages
home_page = Tk()
home_page.title("Home Page")
home_page.minsize(300, 300)
home_page.configure(bg='white')

# creation
# TODO: change label location and text
main_title_HP = Label(home_page, text='Welcome!\n Here are your options:', font=("Arial Bold", 14))

# TODO: add 'Back' button in each page
btn_close = Button(home_page, text="Exit", command=exit)

# chk_state = BooleanVar()
# chk_state.set(False)  # Set default state
# chk = Checkbutton(personal_details, text='choose', var=chk_state)


# pack
main_title_HP.grid(row=0, column=0)

btn_close.grid(row=50, column=0)


setMenu(home_page)
home_page.mainloop()
