"""
This is a program that store this papers information:
Title, Autor
Year, ISBN

User can:

View all records
Search an entry
add entry
Update entry
Delete
close
"""
from tkinter import *
import backend

window = Tk()  # ventana principal

#callback functions
#==========================================================================
def view_parameters():
    lista1.delete(0,END) # se blanquea el cuadro 
    for row in backend.view():
        lista1.insert(END,row) # al elemento lista1 se le agregan las tuplas obtenidas de la funcion view del modulo backend


def search_parameters():
    lista1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        lista1.insert(END,row)

def insert_parameter():
    lista1.delete(0,END)
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    lista1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

def get_selected_row(event):
    index = lista1.curselection()[0]
    print (index)


#agregando widgets
#==========================================================================
#row0
label1 = Label(window,text="Title")
label1.grid(row=0,column=0)

title_text = StringVar()
entry1 = Entry(window,textvariable=title_text)
entry1.grid(row=0,column=1)

label2 = Label(window, text="Author")
label2.grid(row=0,column=2)

author_text=StringVar()
entry2 = Entry(window,textvariable=author_text)
entry2.grid(row=0,column=3)

#row1
label1 = Label(window,text="Year")
label1.grid(row=1,column=0)

year_text=StringVar()
entry1 = Entry(window,textvariable=year_text)
entry1.grid(row=1,column=1)

label2 = Label(window, text="ISBN")
label2.grid(row=1,column=2)

isbn_text=StringVar()
entry2 = Entry(window,textvariable=isbn_text)
entry2.grid(row=1,column=3)

#row 3 a head

lista1 = Listbox(window, height=6, width=35)
lista1.grid(row=2,column=0, rowspan=6, columnspan=2)

#configrar el scrollbar  para que sea quien controla la lista1

sb1 = Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

lista1.configure(yscrollcommand=sb1.set)
sb1.configure(command=lista1.yview)

lista1.bind('<<ListboxSelect>>', get_selected_row) # funcion que enlaza lo seleccionado con el evento del metodo delete del backend

#configurando botones de entrada

buton1=Button(window,text="View all",width=12,command=view_parameters)
buton1.grid(row=2,column=3)

buton2=Button(window,text="Search entry",width=12,command=search_parameters)
buton2.grid(row=3,column=3)

buton3=Button(window,text="Add entry",width=12,command=insert_parameter)
buton3.grid(row=4,column=3)

buton4=Button(window,text="Update",width=12)
buton4.grid(row=5,column=3)

buton5=Button(window,text="Delete",width=12)
buton5.grid(row=6,column=3)

buton6=Button(window,text="Close",width=12)
buton6.grid(row=7,column=3)


window.mainloop() # loop que mantiene la ventan abierta