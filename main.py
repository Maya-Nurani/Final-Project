from tkinter import *
from tkinter.ttk import *
import tkinter.filedialog as FD

#פונקציה אשר מציגה את הframe הנבחר בתפריט ומסתירה את האחרים
def raise_frame(frame_show, *frames_hide):
    for frame_to_hide in frames_hide:
        frame_to_hide.grid_forget()
    frame_show.grid()
    frame_show.tkraise()

def clicked():
    full_name_val = txt_full_name.get()
    print('Clicked! This is your text:', full_name_val)

#תפריט אשר עובד באמצעות הצגה והסתרה של frameים
def setMenu(page):
    menubar = Menu(page)
    menubar.add_command(label="Homepage", command=lambda: raise_frame(home_page,personal_details))
    menubar.add_command(label="Personal Details", command=lambda: raise_frame(personal_details,home_page))
    menubar.add_command(label="Contacts", command=clicked())
    menubar.add_command(label="Contact Locations", command=clicked())
    root.config(menu=menubar)

root = Tk()
# Home page - the main page of our program, from this page the user can navigate between the other pages
home_page = Frame(root)
# home_page.pack()
# home_page.title("Home Page")
root.minsize(400, 200)

main_title_HP = Label(home_page, text="Welcome!\nYour are now watching XXX's information.\nPlease select an option at the menu", font=("Arial Bold", 14))
main_title_HP.pack(pady=100, padx=200)


personal_details = Frame(root)
personal_details.grid_forget()

# creation
# TODO: change label location and text
main_title_PD = Label(personal_details,
                      text='Personal Details:\n Please fill in the following details according to the format',
                      font=("Arial Bold", 10))


# TODO: add 'Back' button in each page
btn_exit = Button(personal_details, text='Exit', command=exit)
btn_close = Button(home_page, text="Exit", command=exit)

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

# chk_state = BooleanVar()
# chk_state.set(False)  # Set default state
# chk = Checkbutton(personal_details, text='choose', var=chk_state)

# Gender
lbl_gender = Label(personal_details, text='Gender')
rad_male = Radiobutton(personal_details, text='Male', value=1)
rad_female = Radiobutton(personal_details, text='Female', value=2)

# TODO: 'Click Here' or actually - 'save' button - will save the data into file (text file?)
btn1 = Button(personal_details, text='Save details', command=clicked)
# btn_to_personal_details = Button(home, text='Personal Details', command=clicked())

# pack
# main_title_HP.grid(row=0, column=0)
main_title_HP.pack()
main_title_PD.grid(row=0, column=0)
lbl_full_name.grid(row=1, column=0)
txt_full_name.grid(row=1, column=15)
lbl_age.grid(row=2, column=0)
txt_age.grid(row=2, column=15)

btn1.grid(row=3, column=0)
# btn_to_personal_details.grid(row=3, column=0)

btn_exit.grid(row=10, column=0)

# btn_close.grid(row=50, column=0)
btn_close.pack()
combo_city.grid(row=4, column=0)
# chk.grid(row=5, column=0)

lbl_gender.grid(row=6, column=0)
rad_male.grid(row=6, column=5)
rad_female.grid(row=6, column=15)

setMenu(root)

raise_frame(home_page)
root.mainloop()
# personal_details.mainloop()
