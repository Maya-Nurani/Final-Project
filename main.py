from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

import tkinter.filedialog as FD


# פונקציה אשר מציגה את הframe הנבחר בתפריט ומסתירה את האחרים
def raise_frame(frame_show, *frames_hide):
    for frame_to_hide in frames_hide:
        frame_to_hide.grid_forget()
    frame_show.grid()
    frame_show.tkraise()


def clicked():
    full_name_val = txt_full_name.get()
    print('Clicked! This is your text:', full_name_val)


# תפריט אשר עובד באמצעות הצגה והסתרה של frameים
def setMenu(page):
    menubar = Menu(page)
    menubar.add_command(label="Homepage", command=lambda: raise_frame(home_page, personal_details, contact))
    menubar.add_command(label="Personal details", command=lambda: raise_frame(personal_details, home_page, contact))
    menubar.add_command(label="Contacts", command=lambda: raise_frame(contact, home_page, personal_details))
    menubar.add_command(label="Contact locations", command=clicked())
    menubar.add_command(label="Exit", command=root.quit)
    root.config(menu=menubar)


def objDetails():
    # insert objects to obj by using array_details - (maybe done for now)
    obj = {
        lbl_full_name.cget("text"): array_details[0].get(),
        lbl_age.cget("text"): array_details[1].get(),
        lbl_city.cget("text"): array_details[2].get()

    }
    return obj


def saveDetails():
    if detailsValidation():
    #if True:
        print(objDetails().values())
        print(type(objDetails().values()))
        with open("users_personalDetails.txt", "w") as file:
            file.write(str(objDetails()))

        # confirmation popup - let the user know the details saved
        sendCallBack()
        # TODO: maybe we can close details page after the message :)
    else:
        messagebox.showinfo('Validation error', 'Please fill in all details please')


def detailsValidation():
    for i in objDetails().values():
        if i == '':
            return False
    return True


def clearForm():
    for i in array_details:
        i.delete(0, END)


def sendCallBack():
    messagebox.showinfo('confirmation', '{0}, your details saved successfully!'.format(txt_full_name.get()))


# Root is our main windoow (where we create frames)
root = Tk()
root.minsize(400, 200)

# Home page - the main page of our program, from this page the user can navigate between the other pages
home_page = Frame(root)

# contacts - person's contacts list
contact = Frame(root)
lbl_contacts_title = Label(contact, font=("Arial Bold", 10), text="contacts list")
lbl_contacts_title.grid(row=0, column=0)

# personal details
personal_details = Frame(root)
main_title_HP = Label(home_page,
                      text="Welcome!\nYour are now watching XXX's information.\nPlease select an option at the menu",
                      font=("Arial Bold", 14))
main_title_HP.grid(row=0, column=0)

# creation
# TODO: change label location and text
main_title_PD = Label(personal_details,
                      text='Personal Details:\n Please fill in the following details according to the format',
                      font=("Arial Bold", 10))
main_title_PD.grid(row=0, column=0)

# TODO: add 'Back' button in each page

# TODO: 'Click Here' or actually - 'save' button - will save the data into file (text file?)
btn_send = Button(personal_details, text='Send', command=saveDetails)
btn_clear = Button(personal_details, text='Clear', command=clearForm)

# Full Name field
lbl_full_name = Label(personal_details, text='Full Name')
txt_full_name = Entry(personal_details, width=20)

# Age (Can be as 'date of birth' and split by Year-Month-Day)
lbl_age = Label(personal_details, text='Age')
txt_age = Entry(personal_details, width=4)
# numeric_age = int(txt_age.get())

# City field
cities_obj = {
    0: '',
    1: None,
    2: 'Tel-Aviv',
    3: 'Jerusalem',
    4: 'Yavne',
    5: 'Ramat-Gan',
    6: 'Haifa'
}
lbl_city = Label(personal_details, text='City')
combo_city = Combobox(personal_details, values=list(cities_obj.values()))
#combo_city['values'] = (None, 'Tel-Aviv', 'Jerusalem', 'Ramat-Gan', 'Haifa', 'Yavne')
combo_city.current(0)  # Set default value

# chk_state = BooleanVar()
# chk_state.set(False)  # Set default state
# chk = Checkbutton(personal_details, text='choose', var=chk_state)

# Gender
lbl_gender = Label(personal_details, text='Gender')
rad_male = Radiobutton(personal_details, text='Male', value=1)
rad_female = Radiobutton(personal_details, text='Female', value=2)

# pack
lbl_full_name.grid(row=1, column=0)
txt_full_name.grid(row=1, column=10)
lbl_age.grid(row=2, column=0)
txt_age.grid(row=2, column=10)
lbl_city.grid(row=4, column=0)

btn_send.grid(row=12, column=0)
btn_clear.grid(row=13, column=15)

combo_city.grid(row=4, column=10)
# chk.grid(row=5, column=0)

lbl_gender.grid(row=6, column=0)
rad_male.grid(row=6, column=8)
rad_female.grid(row=6, column=10)

# Array of values from personal details form
array_details = [txt_full_name, txt_age, combo_city]

setMenu(root)

raise_frame(home_page)
root.mainloop()
