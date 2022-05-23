from tkinter import *

root = Tk()
TEXT = "Contacts.txt"
root.title('Address Book')
root.resizable(width=FALSE, height=FALSE)

TEMP_NAME_VAR = StringVar()
TEMP_PHONE_VAR = StringVar()
TEMP_EMAIL_VAR = StringVar()

EDIT_NAME_VAR = StringVar()
EDIT_PHONE_VAR = StringVar()
EDIT_EMAIL_VAR = StringVar()
SEARCH_VAR = StringVar()


def display():
    try:
        with open(TEXT) as f:
            lines = f.read().split("\n")
            for i in range(len(lines)):
                contact = lines[i].split("¬")
                createLabel(contact[0], contact[1], contact[2], i)
    except:
        Label(root, text="Name").grid(row=1, column=0, sticky="W")
        Label(root, text="Phone").grid(row=1, column=1, sticky="W")
        Label(root, text="Email").grid(row=1, column=2, sticky="W")
        Button(root, text="QUIT", command=quit).grid(row=0, column=4, sticky="NESW")
        Button(root, text="Add New Person", command=add_window).grid(row=0, column=0, sticky="NESW")
        Button(root, text="Search",command = lambda:search(SEARCH_VAR)).grid(row=0, column=3, sticky="NESW")
        Entry(root, textvariable=SEARCH_VAR).grid(row=0, column=1, columnspan=2,sticky="NESW")


def createLabel(name, phone, email, i):
    Label(root, text=name).grid(row=i + 2, column=0, sticky="W")
    Label(root, text=phone).grid(row=i + 2, column=1, sticky="W")
    Label(root, text=email).grid(row=i + 2, column=2, sticky="W")
    Button(root, text="Edit", command=lambda: edit_person_window(i)).grid(row=i + 2, column=3, sticky="NESW")


def add_window():
    addwindow = Toplevel(root)
    addwindow.title('Add Person')
    root.resizable(width=FALSE, height=FALSE)
    Label(addwindow, text="Name").grid(row=0)
    Label(addwindow, text="Phone").grid(row=1)
    Label(addwindow, text="Email").grid(row=2)
    Entry(addwindow, textvariable=TEMP_NAME_VAR).grid(row=0, column=1,sticky="NESW")
    Entry(addwindow, textvariable=TEMP_PHONE_VAR).grid(row=1, column=1,sticky="NESW")
    Entry(addwindow, textvariable=TEMP_EMAIL_VAR).grid(row=2, column=1,sticky="NESW")
    Button(addwindow, text="Enter", command=enter_data).grid(row=4, column=1, sticky="NESW")
    Button(addwindow, text="Back", command=addwindow.destroy).grid(row=4, column=0, sticky="NESW")


def enter_data():
    if TEMP_NAME_VAR.get() == "" and TEMP_PHONE_VAR.get() == "" and TEMP_EMAIL_VAR.get() == "":
        return None
    try:
        with open(TEXT, "a") as file:
            file.write(TEMP_NAME_VAR.get() + "¬" + TEMP_PHONE_VAR.get() + "¬" + TEMP_EMAIL_VAR.get() + "\n")
    except:
        pass
    else:
        TEMP_NAME_VAR.set("")
        TEMP_PHONE_VAR.set("")
        TEMP_EMAIL_VAR.set("")
        clear()
        display()


def clear():
    liste = root.grid_slaves()
    for l in liste:
        l.destroy()


def search(qq):
    if len(qq) < 3:
        return None
    NAMES = []
    PHONES = []
    EMAILS = []
    with open(TEXT) as f:
        lines = f.read()
    person_list = lines.split("\n")
    try:
        for person in person_list:
            n,p,e = person.split("¬")
            NAMES.append(n)
            PHONES.append(p)
            EMAILS.append(e)
    except:
        print(NAMES)
        print(PHONES)
        print(EMAILS)





def edit_person_window(i):
    with open(TEXT) as f:
        lines = f.read()
    editwindow = Toplevel(root)
    editwindow.title('Edit Person')
    editwindow.resizable(width=FALSE, height=FALSE)
    person = lines.split("\n")
    person_i_want = person[i].split("¬")
    EDIT_NAME_VAR.set(person_i_want[0])
    EDIT_PHONE_VAR.set(person_i_want[1])
    EDIT_EMAIL_VAR.set(person_i_want[2])
    Label(editwindow, text="Name").grid(row=0, column=0, sticky="W")
    Label(editwindow, text="Phone").grid(row=1, column=0, sticky="W")
    Label(editwindow, text="Email").grid(row=2, column=0, sticky="W")
    Entry(editwindow, textvariable=EDIT_NAME_VAR).grid(row=0, column=1, columnspan=2)
    Entry(editwindow, textvariable=EDIT_PHONE_VAR).grid(row=1, column=1, columnspan=2)
    Entry(editwindow, textvariable=EDIT_EMAIL_VAR).grid(row=2, column=1, columnspan=2)
    Button(editwindow, text="Save", command=lambda: save(EDIT_NAME_VAR, EDIT_PHONE_VAR, EDIT_EMAIL_VAR, i, person, editwindow,"sav")).grid(row=4,column=1,sticky="NESW")
    Button(editwindow, text="Back", command=editwindow.destroy).grid(row=4, column=0, sticky="NESW")
    Button(editwindow, text="Del", command=lambda: save(EDIT_NAME_VAR, EDIT_PHONE_VAR, EDIT_EMAIL_VAR, i, person, editwindow,"del")).grid(row=4, column=2,sticky="NESW")


def save(name, phone, email, i, person, window,sav_or_del):
    if name.get() == "" and phone.get() == "" and email.get() == "":
        return None
    person.pop(i)
    if sav_or_del == "sav":
        person.insert(i, name.get() + "¬" + phone.get() + "¬" + email.get())
    file = open(TEXT,"w")
    for i in range(0,len(person)-1):
        file.write(person[i])
        file.write("\n")
    file.close()
    clear()
    display()
    window.destroy()


display()
mainloop()
