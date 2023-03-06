#Import libraries
from tkinter import *
from tkinter import messagebox


#Window initialization and properties
root = Tk()
root.geometry('700x550')
root.config(bg = '#f4e3b6')
root.title('Personal Contacts Directory')
root.resizable(0,0)
contactlist = [
    ['Chimamnda Adichie','54687842551'],
    ['Christie Essien Igbokwe', '254687354137'],
    ['Agbani Darego', '98468435243'],
    ['Dora Akunyili', '45758682214'],
    ['Fumilayo Ransome-Kuti', '8287646975'],
    ['Ngozi Okonjo-Iweala', '73365647892'],
    ['Omawumi Megbele', '658889685320'],
    ['Ireti Doyle', '38564788695'],
    ['Aisha Yesufu','15967478112'],
    ['Aisha Yesufu','15967478112'],
    ['Ameyo Adadevoh','75654278112'],
    ['Bimbo Odukoya','45365478112']
    ]


#window_icon
window_icon = PhotoImage(file="icon.png")
root.iconphoto(False, window_icon)

logo = PhotoImage(file='logo.png')
Label(root, image=logo, bg='#f4e3b6').place(x=10, y=430)

Name = StringVar()
Number = StringVar()


#Create frames
view_frame = Frame(root)
view_frame.pack(side = RIGHT)

scroll = Scrollbar(view_frame, orient=VERTICAL)
select = Listbox(view_frame, yscrollcommand=scroll.set,font=('Raleway',16),bg="#f0fffc",width=20,height=20,borderwidth=3,relief="groove")
scroll.config (command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT,  fill=BOTH, expand=1)



def Selected():
	print("hello",len(select.curselection()))
	if len(select.curselection())==0:
		messagebox.showerror("Error", "Please Select Name")
	else:
		return int(select.curselection()[0])
    
#Add contact function 
def AddContact():
    if Name.get()!="" and Number.get()!="":
        contactlist.append([Name.get() ,Number.get()])
        print(contactlist)
        Select_set()
        EntryReset()
        messagebox.showinfo("Success!", "New Contact Added")

    else:
        messagebox.showerror("Error","Please fill required field")


#Edit existing contact function 

def UpdateDetail():
	if Name.get() and Number.get():
		contactlist[Selected()] = [Name.get(), Number.get()]
    

		messagebox.showinfo("Success!", "Contact Updated")
		EntryReset()
		Select_set()

	elif not(Name.get()) and not(Number.get()) and not(len(select.curselection())==0):
		messagebox.showerror("Error", "Please fill required field")

	else:
		if len(select.curselection())==0:
			messagebox.showerror("Error", "Please Select the Name and \n press View button")
		else:
			message1 = """To Load the all information of \n 
						  selected row press the View button\n.
						  """   
			messagebox.showerror("Error", message1)

def EntryReset():
	Name.set('')
	Number.set('')

#Delete selected contact function

def Delete_Entry():
    if len(select.curselection())!=0:
        result=messagebox.askyesno('Confirmation','You Are About to Delete \n')
        if result==True:
            del contactlist[Selected()]
            Select_set()
    else:
        messagebox.showerror("Error", 'Please select a Contact')

   
#View contact function 
def VIEW():
    NAME, PHONE = contactlist[Selected()]
    Name.set(NAME)
    Number.set(PHONE)
        

#Exit function
def EXIT():
    root.destroy()


def Select_set() :
    contactlist.sort()
    select.delete(0,END)
    for name,phone in contactlist :
        select.insert (END, name)
Select_set()


#labels, entries and buttons
nameLabel = Label(root, text = 'Name', font=("Raleway",14, 'italic'), bg = '#f4e3b6').place(x= 30, y=20)
nameEntry = Entry(root, textvariable = Name, font=("Raleway",12), width=31).place(x= 90, y=25)
contactLabel = Label(root, text = 'Phone', font=("Raleway",14, 'italic'),bg = '#f4e3b6').place(x= 30, y=70)
contactEntry = Entry(root, textvariable = Number, font=("Raleway",12), width=31).place(x= 90, y=75)

addButton = Button(root,text=" ADD", font='Raleway 18',bg='#9dc09a', width=7, command = AddContact, padx=20). place(x= 50, y=140)
editButton = Button(root,text="EDIT", font='Raleway 18',bg='#9dc09a', width=7, command = UpdateDetail, padx=20).place(x= 250, y=140)
deleteButton = Button(root,text="DELETE", font='Raleway 18',bg='#e4956a', width=7, command = Delete_Entry, padx=20).place(x= 250, y=260)
viewButton = Button(root,text="VIEW", font='Raleway 18',bg='#e8c1c7', width=10, command = VIEW).place(x= 50, y=260)
clearButton = Button(root,text="CLEAR", font='Raleway 18',bg='#d8b54d', width=10, command = EntryReset).place(x= 50, y=390)
exitButton = Button(root,text="EXIT", font='Raleway 18',bg='tomato', width=10, command = EXIT).place(x= 250, y=390)

root.mainloop()
  
