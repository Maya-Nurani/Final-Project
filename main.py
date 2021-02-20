from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import itertools

import tkinter.filedialog as FD


def initial_files(file_name):
   try:
        with open("{0}.txt".format(file_name), "w") as file:
            file.write("")
   except:
        print("No founded file with this name:", file_name)



# פונקציה אשר מציגה את הframe הנבחר בתפריט ומסתירה את האחרים
def raise_frame(frame_show, *frames_hide):
    for frame_to_hide in frames_hide:
        frame_to_hide.grid_forget()
    frame_show.grid(padx=50, pady=50)
    frame_show.tkraise()


# תפריט אשר עובד באמצעות הצגה והסתרה של frameים
def setMenu(page):
    menubar = Menu(page)
    menubar.add_command(label="Homepage",
                        command=lambda: raise_frame(home_page, personal_details, contact, locations, summary))
    menubar.add_command(label="Personal details",
                        command=lambda: raise_frame(personal_details, home_page, contact, locations, summary))
    menubar.add_command(label="Add a contact",
                        command=lambda: raise_frame(contact, home_page, personal_details, locations, summary))
    menubar.add_command(label="Add contact locations",
                        command=lambda: raise_frame(locations, contact, home_page, personal_details, summary))
    menubar.add_command(label="Contacts and locations",
                        command=lambda: raise_frame(summary, contact, home_page, personal_details, locations))
    menubar.add_command(label="Exit", command=root.quit)
    root.config(menu=menubar)


def objData(arr_keys, arr_val):
    obj = {}
    for x, y in zip(arr_keys, arr_val):
        obj[x.cget("text")] = y.get()

    return obj


def saveFormData(form_data, file_name, stat):
    if detailsValidation(form_data):
        try:
            with open("{0}.txt".format(file_name), "{0}".format(stat)) as file:
                str_current_form_data = str(list(form_data.values()))
                file.write(str_current_form_data + "\n")
        except:
            print("No founded file with this name:", file_name)

        # Confirmation popup - let the user know the details saved
        sendCallBack()
    else:
        messagebox.showinfo('Validation error', 'Please finish to fill in all fields')


def detailsValidation(form_data):
    for i in form_data.values():
        if i == '':
            return False
    return True


def clearForm():
    for i in array_details_values:
        if i == var_rad:
            var_rad.set('')
        else:
            i.delete(0, END)


def sendCallBack():
    user_name = txt_full_name.get()
    messagebox.showinfo('Confirmation', '{0}\nYour details saved successfully!'.format(user_name))


def updateContactsLocations():
    try:
        with open("users_locations.txt", "r") as locationfile:
            locations_list = locationfile.read()
        for index, item in enumerate(array_location_keys, start= 1):
            lbl_locations_labels = Label(summary, text=item.cget("text"))
            lbl_locations_labels.grid(row=1, column=index)
        lbl_locations_list = Label(summary, text=locations_list)
        lbl_locations_list.grid(row=2, column=1)

    except:
        print("No founded file")

    try:
        with open("contactsFile.txt", "r") as file:
            contactList = file.readlines()

        for index, item in enumerate(array_contacts_keys, start= 1):
            lbl_locations_labels = Label(summary, text=item.cget("text"))
            lbl_locations_labels.grid(row=3, column=index)
        lbl_contacts_list = Label(summary, text=contactList)
        lbl_contacts_list.grid(row=4, column=0)
    except:
        print("No founded file")


initial_files("contactsFile")
initial_files("users_locations")

# Root is our main window (where we create frames)
root = Tk()
root.minsize(600, 250)
root.config(bg="lightgreen")
s = Style()
s.configure('TFrame', foreground='#000000', background='lightgreen')

# Home page - the main page of our program, from this page the user can navigate between the other pages
home_page = Frame(root)
main_title_HP = Label(home_page,
                      text="COV-19\nEpidemiological Investigation System",
                      font=("Arial Bold", 16))
main_title_HP.grid(row=0, column=0, padx=50, pady=50)
lbl_startinvestigation = Label(home_page, text="to start, select an option from the menu.", font=("Arial Bold", 14))
lbl_startinvestigation.grid(row=1, column=0)

# contacts - person's contacts list
contact = Frame(root)
lbl_contacts_title = Label(contact, font=("Arial Bold", 10), text="contacts list")
lbl_contacts_title.grid(row=0, column=0)
lbl_contact_name = Label(contact, font=("Arial Bold", 10), text="Contact's name:")
lbl_contact_name.grid(row=1, column=0)
txt_contact_name = Entry(contact, width=20)
txt_contact_name.grid(row=1, column=1)
lbl_contact_id = Label(contact, font=("Arial Bold", 10), text="Contact's ID:")
lbl_contact_id.grid(row=2, column=0)
txt_contact_id = Entry(contact, width=20)
txt_contact_id.grid(row=2, column=1)
lbl_contact_phone = Label(contact, font=("Arial Bold", 10), text="Contact's phone:")
lbl_contact_phone.grid(row=3, column=0)
txt_contact_phone = Entry(contact, width=20)
txt_contact_phone.grid(row=3, column=1)
btn_add_contact = Button(contact, text='Add Contact',
                         command=lambda: saveFormData(objData(array_contacts_keys, array_contacts_values),
                                                      'contactsFile', "a"))
btn_add_contact.grid(row=4, column=0)

# locations - person's contact locations list
locations = Frame(root)
lbl_locations_title = Label(locations, font=("Arial Bold", 10), text="contact locations list")
lbl_locations_title.grid(row=0, columnspan=20)
lbl_newlocation = Label(locations, font=("Arial Bold", 10), text="Full address:")
lbl_newlocation.grid(row=1, column=0)
txt_newlocation = Entry(locations, width=20)
txt_newlocation.grid(row=1, column=1)
lbl_datefbeing = Label(locations, font=("Arial Bold", 10), text="Date:")
lbl_datefbeing.grid(row=2, column=0)
txt_datefbeing = Entry(locations, width=20)
txt_datefbeing.grid(row=2, column=1)
btn_add_location = Button(locations, text='Add Location',
                          command=lambda: saveFormData(objData(array_location_keys, array_location_values),
                                                       'users_locations', "a"))
btn_add_location.grid(row=3, column=1)

# personal details
personal_details = Frame(root)

# creation
main_title_PD = Label(personal_details,
                      text='Personal Details:\n Please fill in the following details, according to the format',
                      font=("Arial Bold", 10))
main_title_PD.grid(row=0, columnspan=20)

btn_send = Button(personal_details, text='Send',
                  command=lambda: saveFormData(objData(array_details_keys, array_details_values),
                                               'users_personalDetails', "w"))
btn_clear = Button(personal_details, text='Clear', command=clearForm)
# TODO : add clear button also to other pages?

# Full Name field
lbl_full_name = Label(personal_details, text='Full Name')
txt_full_name = Entry(personal_details, width=20)

# Age (Can be as 'date of birth' and split by Year-Month-Day)
# TODO : check for date format
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
txt_full_name.grid(row=1, column=1)
lbl_age.grid(row=2, column=0)
txt_age.grid(row=2, column=1)
lbl_city.grid(row=3, column=0)

btn_send.grid(row=6, column=0)
btn_clear.grid(row=6, column=1)

combo_city.grid(row=3, column=1)
# chk.grid(row=5, column=0)

lbl_gender.grid(row=5, column=0)
rad_male.grid(row=5, column=1)
rad_female.grid(row=5, column=2)

# Array of values from the forms
array_details_keys = [lbl_full_name, lbl_age, lbl_city, lbl_gender]
array_details_values = [txt_full_name, txt_age, combo_city, var_rad]
array_contacts_keys = [lbl_contact_name, lbl_contact_id, lbl_contact_phone]
array_contacts_values = [txt_contact_name, txt_contact_id, txt_contact_phone]
array_location_keys = [lbl_newlocation, lbl_datefbeing]
array_location_values = [txt_newlocation, txt_datefbeing]

# summary
summary = Frame(root)
btn_refresh = Button(summary, text="Refresh", command=lambda: updateContactsLocations())
btn_refresh.grid(row=5, column=0)
lbl_sumoflocations = Label(summary, text='Locations summary:')
lbl_sumoflocations.grid(row=1, column=0)
lbl_sumofcontacts = Label(summary, text='Contacts summary:')
lbl_sumofcontacts.grid(row=3, column=0)
btn_quarantine = Button(summary, text='Send all to quarantine')
btn_quarantine.grid(row=5, column=1)

setMenu(root)

raise_frame(home_page)
root.mainloop()
