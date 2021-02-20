from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import itertools

import tkinter.filedialog as FD


# פונקציה אשר מציגה את הframe הנבחר בתפריט ומסתירה את האחרים
def raise_frame(frame_show, *frames_hide):
    for frame_to_hide in frames_hide:
        frame_to_hide.grid_forget()
    frame_show.grid()
    frame_show.tkraise()


# תפריט אשר עובד באמצעות הצגה והסתרה של frameים
def setMenu(page):
    menubar = Menu(page)
    menubar.add_command(label="Homepage", command=lambda: raise_frame(home_page, personal_details, contact, locations))
    menubar.add_command(label="Personal details",
                        command=lambda: raise_frame(personal_details, home_page, contact, locations))
    menubar.add_command(label="Contacts", command=lambda: raise_frame(contact, home_page, personal_details, locations))
    menubar.add_command(label="Contact locations",
                        command=lambda: raise_frame(locations, contact, home_page, personal_details))
    menubar.add_command(label="Exit", command=root.quit)
    root.config(menu=menubar)


def objData(arr_keys, arr_val):
    # insert objects to obj by using array_details - (maybe done for now)
    obj = {}
    for x, y in zip(arr_keys, arr_val):
        obj[x.cget("text")] = y.get()

    print(obj)
    return obj


def saveFormData(form_data, file_name):
    if detailsValidation(form_data):
        print(form_data.values())
        print(type(form_data.values()))
        with open("{0}.txt".format(file_name), "w") as file:
            file.write(str(form_data))

        # Confirmation popup - let the user know the details saved
        sendCallBack()
        # TODO: maybe we can close details page after the message :)
    else:
        messagebox.showinfo('Validation error', 'Please finish to fill in all your details')


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
    messagebox.showinfo('confirmation', '{0}, your details saved successfully!'.format(txt_full_name.get()))


# Root is our main windoow (where we create frames)
root = Tk()
root.minsize(400, 200)
root.config(bg="lightgreen")
s = Style()
s.configure('TFrame', foreground='#000000', background='lightgreen')

# Home page - the main page of our program, from this page the user can navigate between the other pages
home_page = Frame(root, style='TFrame')
main_title_HP = Label(home_page,
                      text="Welcome!\nYour are now watching XXX's information.\nPlease select an option at the menu",
                      font=("Arial Bold", 14), foreground='#000000', background='lightgreen')
main_title_HP.grid(row=0, column=0)

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
                                                      'contactsFile'))
btn_add_contact.grid(row=4, column=0)

# locations - person's contact locations list
locations = Frame(root)
lbl_locations_title = Label(locations, font=("Arial Bold", 10), text="contact locations list")
lbl_locations_title.grid(row=0, column=0)
lbl_newlocation = Label(locations, font=("Arial Bold", 10), text="Contact's phone:")
lbl_newlocation.grid(row=1, column=0)
txt_newlocation = Entry(locations, width=20)
txt_newlocation.grid(row=1, column=1)
btn_add_contact = Button(locations, text='Add Location')
btn_add_contact.grid(row=1, column=2)

# personal details
personal_details = Frame(root)

# creation
# TODO: change label location and text
main_title_PD = Label(personal_details,
                      text='Personal Details:\n Please fill in the following details according to the format',
                      font=("Arial Bold", 10))
main_title_PD.grid(row=0, column=0)

# TODO: add 'Back' button in each page

btn_send = Button(personal_details, text='Send',
                  command=lambda: saveFormData(objData(array_details_keys, array_details_values),
                                               'users_personalDetails'))
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
# combo_city['values'] = (None, 'Tel-Aviv', 'Jerusalem', 'Ramat-Gan', 'Haifa', 'Yavne')
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

btn_send.grid(row=15, column=10)
btn_clear.grid(row=15, column=0)

combo_city.grid(row=4, column=10)
# chk.grid(row=5, column=0)

lbl_gender.grid(row=6, column=0)
rad_male.grid(row=6, column=8)
rad_female.grid(row=6, column=10)

# Arrays:
array_details_keys = [lbl_full_name, lbl_age, lbl_city, lbl_gender]
array_details_values = [txt_full_name, txt_age, combo_city, var_rad]

array_contacts_keys = [lbl_contact_name, lbl_contact_id, lbl_contact_phone]
array_contacts_values = [txt_contact_name, txt_contact_id, txt_contact_phone]

setMenu(root)

raise_frame(home_page)
root.mainloop()
