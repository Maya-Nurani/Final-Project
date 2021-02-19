from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

def contact_page(root):
    contact = Frame(root)
    # contacts_list = Frame(root)
    lbl_contacts_title = Label(contact, font=("Arial Bold", 10), text="contacts list")
    lbl_contacts_title.pack(padx=100, pady=100)
    return contact

