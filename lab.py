import customtkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import database

# App properties
app = customtkinter.CTk()
app.title("Employment Mangment")
app.geometry("900x420")
app.config(bg="#161C25")
app.resizable(False,False)
# Fonts
font1 = ("Arial",20,"bold")
font2 = ("Arial",12,"bold")

# funcs

def add_to_treeview():
    emps = database.fetch()
    tree.delete(*tree.get_children())
    for emp in emps:
        tree.insert("",END,values=emp) 


def insert():
    idd = id_e.get()
    name = name_e.get()
    jop = jop_e.get()
    gender = v1.get()
    status = v2.get()
    if not(idd and name and jop and gender and status):
        messagebox.showerror("Error","Enter All Fields.")
    elif database.id_exist(idd):
        messagebox.showerror("Error","ID already Exists.")
    else:
        database.insert(idd,name,jop,gender,status)
        add_to_treeview()
        messagebox.showinfo("Success","Data Has Been Inserted")


def clear(*clicked):
    if clicked:
        tree.selection_remove(tree.focus())
        tree.focus("")
    id_e.delete(0,END)
    name_e.delete(0,END)
    jop_e.delete(0,END)
    v1.set("Male")
    v2.set("Active")


def display_data(event):
    selected_item = tree.focus()
    if selected_item:
        row = tree.item(selected_item)["values"]
        clear()
        id_e.insert(0,row[0])
        name_e.insert(0,row[1])
        jop_e.insert(0,row[2])
        v1.set(row[3])
        v2.set(row[4])
    else:
        pass
def delete():
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showerror("Error","Choose an Employee to Delete.")
    else:
        id_ee = id_e.get()
        database.delete(id_ee)
        add_to_treeview()
        clear()
        messagebox.showinfo("Success","Employee Has Been Deleted.")
        
        
def Update():
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showerror("Error","Choose an Employee to Update.")
    else:
        id = id_e.get()
        name = name_e.get()
        jop = jop_e.get()
        gender = v1.get()
        status = v2.get()
        database.update(name,jop,gender,status,id)
        add_to_treeview()
        clear()
        messagebox.showinfo("Success","Data Has Been Updated.")






# Labels & Entry Boxes & Combo Box


id_l = customtkinter.CTkLabel(app,font=font1,text="ID:" ,text_color="#fff",bg_color="#161C25")
id_l.place(x=20,y=20)
id_e = customtkinter.CTkEntry(app,font=font1,text_color="#000",border_width=2,bg_color="#161C25",fg_color="#fff",border_color="#0C9295",width=180)
id_e.place(x=100,y=20)


name_l = customtkinter.CTkLabel(app,font=font1,text="Name:" ,text_color="#fff",bg_color="#161C25")
name_l.place(x=20,y=80)
name_e = customtkinter.CTkEntry(app,font=font1,text_color="#000",border_width=2,bg_color="#161C25",fg_color="#fff",border_color="#0C9295",width=180)
name_e.place(x=100,y=80)


jop_l = customtkinter.CTkLabel(app,font=font1,text="Jop:" ,text_color="#fff",bg_color="#161C25")
jop_l.place(x=20,y=140)
jop_e = customtkinter.CTkEntry(app,font=font1,text_color="#000",border_width=2,bg_color="#161C25",fg_color="#fff",border_color="#0C9295",width=180)
jop_e.place(x=100,y=140)

gender_l = customtkinter.CTkLabel(app,font=font1,text="Gender:" ,text_color="#fff",bg_color="#161C25")
gender_l.place(x=20,y=200)


options = ["Male","Female"]
v1 = StringVar()


Gender_e = customtkinter.CTkComboBox(app,font=font1,text_color="#000",fg_color="#fff",bg_color="#161C25",dropdown_hover_color="#0C9295",button_color="#0C9295",button_hover_color="#0C9295",border_color="#0C9295",width=180,variable=v1,values=options,state="readonly")
Gender_e.set("Male")
Gender_e.place(x=100,y=200)


status_l = customtkinter.CTkLabel(app,font=font1,text="Status:" ,text_color="#fff",bg_color="#161C25")
status_l.place(x=20,y=260)

options2 = ["Active","Not Active","Vacation","On Leave"]
v2 = StringVar()


status_e = customtkinter.CTkComboBox(app,font=font1,text_color="#000",fg_color="#fff",bg_color="#161C25",dropdown_hover_color="#0C9295",button_color="#0C9295",button_hover_color="#0C9295",border_color="#0C9295",width=180,variable=v2,values=options2,state="readonly")
status_e.set("Active")
status_e.place(x=100,y=260)


# Buttons


addB = customtkinter.CTkButton(app,command=insert,font=font1,text_color="#fff",text="Add Employee",fg_color="#05A312",hover_color="#00850B",cursor = "hand2",corner_radius=15,width=260,bg_color="#161C25",)
addB.place(x=20,y=310)


clearB = customtkinter.CTkButton(app,command=lambda:clear(True),font=font1,text_color="#fff",text="New Employee",border_color="#F15704",fg_color="#161C25",hover_color="#FF5002",cursor = "hand2",corner_radius=15,width=260,bg_color="#161C25",border_width=2)
clearB.place(x=20,y=360)


updateB = customtkinter.CTkButton(app,command=Update,font=font1,text_color="#fff",text="Update Employee",border_color="#F15704",fg_color="#161C25",hover_color="#FF5002",cursor = "hand2",corner_radius=15,width=260,bg_color="#161C25",border_width=2)
updateB.place(x=300,y=360)

delB = customtkinter.CTkButton(app,command=delete,font=font1,text_color="#fff",text="Delete Employee",fg_color="#E40404",hover_color="#AE0000",cursor = "hand2",corner_radius=15,width=260,bg_color="#161C25",)
delB.place(x=580,y=360)



# Style & TreeView


style = ttk.Style(app)
style.theme_use("clam")
style.configure("Treeview",font=font2,foreground = "#fff",background="#000",fieldbackground="#313837")
style.map("Treeview",background=[("selected","#1A8F2D")])


tree = ttk.Treeview(app,height=15)
tree["columns"] = ("ID","Name","Jop","Gender","Status")

tree.column("#0",width=0,stretch=tk.NO)
tree.column("ID",anchor=tk.CENTER,width=120)
tree.column("Name",anchor=tk.CENTER,width=120)
tree.column("Jop",anchor=tk.CENTER,width=120)
tree.column("Gender",anchor=tk.CENTER,width=100)
tree.column("Status",anchor=tk.CENTER,width=120)


tree.heading("ID",text="ID")
tree.heading("Name",text="Name")
tree.heading("Jop",text="Jop")
tree.heading("Gender",text="Gender")
tree.heading("Status",text="Status")


tree.place(x=300,y=20)


tree.bind("<ButtonRelease>",display_data)



add_to_treeview()   


# Run App
app.mainloop()