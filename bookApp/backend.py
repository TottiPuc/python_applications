import sqlite3

def connect():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

def insert(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("books.db")
    cur= conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * fROM book WHERE title ='{}' OR author ='{}' OR year ='{}' OR isbn='{}'".format(title,author,year,isbn) )
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=? ",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title='{}', author='{}', year='{}',isbn='{}' WHERE id = '{}'".format(title,author,year,isbn,id))
    conn.commit()
    conn.close()

connect() # para que la funcion de crear se llame simpere que se ejecute el frontend
""" insert("image","andrew",2020,98765652)
delete(9)
print(view())
print(search(year="2020"))
update(1,"processing","XIan",2019,00000)
print(view()) """
