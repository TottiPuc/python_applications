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
from backend import Database

database=Database("books.db")

#callback functions
#==========================================================================
class Window(object):

    def __init__(self,window):
        self.window = window
        self.window.wm_title("Paper Store")

        #agregando widgets
        #==========================================================================
        #row0
        label1 = Label(window,text="Title")
        label1.grid(row=0,column=0)

        label2 = Label(window, text="Author")
        label2.grid(row=0,column=2)   

        #row1
        label3 = Label(window,text="Year")
        label3.grid(row=1,column=0)    

        label4 = Label(window, text="ISBN")
        label4.grid(row=1,column=2)


        self.title_text = StringVar()
        self.entry1 = Entry(window,textvariable=self.title_text)
        self.entry1.grid(row=0,column=1)


        self.author_text=StringVar()
        self.entry2 = Entry(window,textvariable=self.author_text)
        self.entry2.grid(row=0,column=3)


        self.year_text=StringVar()
        self.entry3 = Entry(window,textvariable=self.year_text)
        self.entry3.grid(row=1,column=1)


        self.isbn_text=StringVar()
        self.entry4 = Entry(window,textvariable=self.isbn_text)
        self.entry4.grid(row=1,column=3)

        #row 3 a head

        self.lista1 = Listbox(window, height=6, width=35)
        self.lista1.grid(row=2,column=0, rowspan=6, columnspan=2)

        #configrar el scrollbar  para que sea quien controla la lista1

        sb1 = Scrollbar(window)
        sb1.grid(row=2,column=2,rowspan=6)

        self.lista1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.lista1.yview)

        self.lista1.bind('<<ListboxSelect>>', self.get_selected_row) # funcion que enlaza lo seleccionado con el evento del metodo delete del backend

        #configurando botones de entrada

        buton1=Button(window,text="View all",width=12,command=self.view_parameters)
        buton1.grid(row=2,column=3)

        buton2=Button(window,text="Search entry",width=12,command=self.search_parameters)
        buton2.grid(row=3,column=3)

        buton3=Button(window,text="Add entry",width=12,command=self.insert_parameter)
        buton3.grid(row=4,column=3)

        buton4=Button(window,text="Update",width=12,command=self.update_parameter)
        buton4.grid(row=5,column=3)

        buton5=Button(window,text="Delete",width=12,command=self.delet_parameter)
        buton5.grid(row=6,column=3)

        buton6=Button(window,text="Close",width=12,command=window.destroy)
        buton6.grid(row=7,column=3)


    def view_parameters(self):
        self.lista1.delete(0,END) # se blanquea el cuadro 
        for row in database.view():
            self.lista1.insert(END,row) # al elemento lista1 se le agregan las tuplas obtenidas de la funcion view del modulo database


    def search_parameters(self):
        self.lista1.delete(0,END)
        for row in database.search(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get()):
            self.lista1.insert(END,row)

    def insert_parameter(self):
        self.lista1.delete(0,END)
        database.insert(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get())
        self.lista1.insert(END,(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get()))

    def get_selected_row(self,event):
        #global selected_row # se hace global por el hecho del evento ser llamado dentro de la funcino delet_parameter
        try:
            index = self.lista1.curselection()[0] # con esto se obtiene el indice de la lista  de valores
            self.selected_row =self.lista1.get(index)  # con este se obtiene el indice de la base de datos 
            #colocar cada valor del item selecionado en las ventanas de entrada correspondientes
            self.entry1.delete(0,END)
            self.entry1.insert(END,self.selected_row[1])
            self.entry2.delete(0,END)
            self.entry2.insert(END,self.selected_row[2])
            self.entry3.delete(0,END)
            self.entry3.insert(END,self.selected_row[3])
            self.entry4.delete(0,END)
            self.entry4.insert(END,self.selected_row[4])

        except IndexError:
            pass

    def delet_parameter(self):
        database.delete(self.selected_row[0])
        self.entry1.delete(0,END)
        self.entry2.delete(0,END)
        self.entry3.delete(0,END)
        self.entry4.delete(0,END)
        self.view_parameters()

    def update_parameter(self):
        database.update(self.selected_row[0],self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get())
        self.view_parameters()
        self.entry1.delete(0,END)
        self.entry2.delete(0,END)
        self.entry3.delete(0,END)
        self.entry4.delete(0,END)


   

window = Tk()  # ventana principal
Window(window)
window.mainloop() # loop que mantiene la ventan abierta