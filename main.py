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
    menubar.add_command(label="Homepage", command=lambda: raise_frame(home_page, personal_details, contact,locations,summary))
    menubar.add_command(label="Personal details", command=lambda: raise_frame(personal_details, home_page, contact,locations,summary))
    menubar.add_command(label="Add a contact", command=lambda: raise_frame(contact, home_page, personal_details,locations,summary))
    menubar.add_command(label="Add contact locations", command= lambda: raise_frame(locations, contact, home_page, personal_details,summary))
    menubar.add_command(label="Contacts and locations", command= lambda: raise_frame(summary,contact,home_page,personal_details,locations))
    menubar.add_command(label="Exit", command=root.quit)
    root.config(menu=menubar)


def objDetails():
    # insert objects to obj by using array_details - (maybe done for now)
    obj = {
        lbl_full_name.cget("text"): array_details[0].get(),
        lbl_age.cget("text"): array_details[1].get(),
        lbl_city.cget("text"): array_details[2].get(),
        lbl_gender.cget("text"): array_details[3].get()
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
        messagebox.showinfo('Validation error', 'Please finish to fill in all your details')

def detailsValidation():
    for i in objDetails().values():
        if i == '':
            return False
    return True


def clearForm():
    for i in array_details:
        if i == var_rad:
            var_rad.set('')
        else:
            i.delete(0, END)

def objContacts():
    # insert objects to obj by using array_contacts - (maybe done for now)
    obj = {
        lbl_nameofcontact.cget("text"): array_contacts[0].get(),
        lbl_idofcontact.cget("text"): array_contacts[1].get(),
        lbl_phoneofcontact.cget("text"): array_contacts[2].get(),
    }
    return obj

def saveContacts():
    if contactsValidation():
    #if True:
        print(objContacts().values())
        print(type(objContacts().values()))
        with open("user_contacts.txt", "w") as file:
            file.write(str(objContacts()))
        # confirmation popup - let the user know the details saved
        sendCallBack()
    else:
        messagebox.showinfo('Validation error', 'Please finish to fill in all your details')

def contactsValidation():
    for i in objContacts().values():
        if i == '':
            return False
    return True

def objLocations():
    # insert objects to obj by using array_locations - (maybe done for now)
    obj = {
        lbl_newlocation.cget("text"): array_locations[0].get(),
        lbl_datefbeing.cget("text"): array_locations[1].get(),
    }
    return obj

def saveLocations():
    if locationsValidation():
        #if True:
        print(objLocations().values())
        print(type(objLocations().values()))
        with open("user_locations.txt", "w") as file:
            file.write(str(objLocations()))
        sendCallBack()
    else:
        messagebox.showinfo('Validation error', 'Please finish to fill in all your details')

def locationsValidation():
    for i in objLocations().values():
        if i == '':
            return False
    return True

def sendCallBack():
    messagebox.showinfo('confirmation', '{0}, your details saved successfully!'.format(txt_full_name.get()))

# Root is our main windoow (where we create frames)
root = Tk()
root.minsize(600, 300)
root.config(bg="lightgreen")
s= Style()
s.configure('TFrame',foreground='#000000',background='lightgreen')

# Home page - the main page of our program, from this page the user can navigate between the other pages
home_page = Frame(root,style='TFrame')
main_title_HP = Label(home_page,
                      text="Welcome!\nYour are now watching XXX's information.\nPlease select an option at the menu",
                      font=("Arial Bold", 14),foreground='#000000',background='lightgreen')
main_title_HP.grid(row=0, column=0)

# contacts - person's contacts list
contact = Frame(root)
lbl_contacts_title = Label(contact, font=("Arial Bold", 10), text="contacts list")
lbl_contacts_title.grid(row=0, column=0)
lbl_nameofcontact = Label(contact, font=("Arial Bold", 10), text="Contacts name:")
lbl_nameofcontact.grid(row=1,column=0)
txt_nameofcontact = Entry(contact, width=20)
txt_nameofcontact.grid(row=1, column=1)
lbl_idofcontact = Label(contact, font=("Arial Bold", 10), text="Contacts ID:")
lbl_idofcontact.grid(row=2,column=0)
txt_idofcontact = Entry(contact, width=20)
txt_idofcontact.grid(row=2, column=1)
lbl_phoneofcontact = Label(contact, font=("Arial Bold", 10), text="Contacts phone:")
lbl_phoneofcontact.grid(row=3,column=0)
txt_phoneofcontact = Entry(contact, width=20)
txt_phoneofcontact.grid(row=3, column=1)
btn_addcontact= Button(contact, text='Add Contact', command=saveContacts)
btn_addcontact.grid(row=4,column=0)

# locations - person's contact locations list
locations = Frame(root)
lbl_locations_title = Label(locations, font=("Arial Bold", 10), text="contact locations list")
lbl_locations_title.grid(row=0, column=0)
lbl_newlocation = Label(locations, font=("Arial Bold", 10), text="Full address:")
lbl_newlocation.grid(row=1,column=0)
txt_newlocation = Entry(locations, width=20)
txt_newlocation.grid(row=1, column=1)
lbl_datefbeing = Label(locations, font=("Arial Bold", 10), text="Date:")
lbl_datefbeing.grid(row=2,column=0)
txt_datefbeing = Entry(locations, width=20)
txt_datefbeing.grid(row=2, column=1)
btn_addlocation= Button(locations, text='Add Location', command=saveLocations)
btn_addlocation.grid(row=2,column=2)

# personal details
personal_details = Frame(root)

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
var_rad = StringVar()
lbl_gender = Label(personal_details, text='Gender')
strMale = "Male"
strFemale = "Female"
rad_male = Radiobutton(personal_details, text=strMale, variable=var_rad, value=strMale)
rad_female = Radiobutton(personal_details, text=strFemale, variable=var_rad, value=strFemale)

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

# Array of values from the forms
array_details = [txt_full_name, txt_age, combo_city, var_rad]
array_contacts = [txt_nameofcontact, txt_idofcontact, txt_phoneofcontact]
array_locations = [txt_newlocation, txt_datefbeing]

# summary
summary = Frame(root)
lbl_sumoflocations = Label(summary, text='Locations summary:')
lbl_sumoflocations.grid(row=0,column=0)
lbl_sumofcontacts = Label(summary, text='Contacts summary:')
lbl_sumofcontacts.grid(row=1,column=0)
btn_quarantine = Button(summary, text='Send all to quarantine')
btn_quarantine.grid(row=4,column=0)

setMenu(root)

raise_frame(home_page)
root.mainloop()
