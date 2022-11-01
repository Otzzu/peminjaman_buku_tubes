from ensurepip import bootstrap
from tkinter import *
from tkinter import messagebox
from turtle import update
import model.models as model
import view.views as view
from datetime import *

def renderMain():
    view.mainFrame(model.books)
    
def openBookFrame(bookName):
    [book] = list(filter(lambda x: x[1] == bookName, model.books))
    book_borrow = next(filter(lambda x: book[0] == x[1] and user[0] == x[0] and x[2] == "", model.book_borrowed), None)
    isBooked = next(filter(lambda x: book[0] == x[1] and user[0] == x[0] and x[2] == "", model.book_borrowed), None) is not None
    isQueued = next(filter(lambda x: book[0] == x[1] and user[0] == x[0] and x[2] == "queue", model.book_borrowed), None) is not None
    sinopsis = list(filter(lambda x: x[0] == book[0], model.book_sinopsis))
    comments = list(filter(lambda x: x[1] == book[0], model.comments))
    str_datetime = ""
    
    if len(sinopsis) == 0: sinopsis.append(["", ""])
    
    if isBooked:
        str_datetime = calcExpiredDate(book_borrow)
        
    view.bookView(book, comments, isBooked, isQueued, str_datetime, sinopsis[0][1])
    
def calcExpiredDate(book_borrow):
    datetime_now = datetime.now()
    expired_date = datetime.strptime(book_borrow[4], "%d-%m-%Y; %H:%M:%S")
        
    delta = expired_date - datetime_now
    if delta.days > 0: str_datetime = f"tersisa {delta.days} hari"
    else: str_datetime =f"tersisa {int(delta.total_seconds()/3600)} jam"
    return str_datetime
    
    
def checkBorrow():
    books_borrowed = list(filter(lambda x: x[0] == user[0] and x[2] == "", model.book_borrowed))
    
    datetime_now = datetime.now()
    for book in books_borrowed:
        expired_date = datetime.strptime(book[4], "%d-%m-%Y; %H:%M:%S")
        if datetime_now.timestamp() > expired_date.timestamp():
            [book2] = list(filter(lambda x: x[0] == book[1], model.books))
            returnBook(book2)
            messagebox.showinfo(message=f"buku '{book2[1]}' sudah habis masa peminjamannya dan akan dikembalikan secara otomatis")

def checkQueue():
    books_queue = list(filter(lambda x: x[0] == user[0] and x[2] == "queue", model.book_borrowed))
    
    for book in books_queue:
        [book2] = list(filter(lambda x: x[0] == book[1], model.books))
        if book2[3] > 0:
            answer = messagebox.askyesno(message=f"buku '{book2[1]}' sudah bisa dipinjam, apakah jadi meminjam?")
            if answer:
                cancelQueue(book2)
                borrow(book2)
            else:
                cancelQueue(book2)
            
             
    
def search(query, books):
    books2 = list(filter(lambda x: query in x[1] or query in x[2] or query in x[5] or query in x[6], books))
    return books2

def filterByCategory(query, books):
    if query == "All":
        return model.books
    
    books2 = list(filter(lambda x: query == x[6], books))
    return books2

def filterByStatus(query, books):
    if query == "borrow": query = ""
    book_borrow = list(filter(lambda x: x[0] == user[0] and x[2] == query, model.book_borrowed))
    books2 = []
    
    for book in book_borrow:
        book1 = next(filter(lambda x: x[0] == book[1], books), None)
        books2.append(book1) 
    return books2

def filterCombobox(query):
    books=[]
    values = ["All", "pendidikan", "non-pendidikan"]
    values2 = ["borrow", "queue"]
    isBookshelf = False
    if query in values: 
        books = filterByCategory(query, model.books)
        index = values.index(query)
    elif query in values2:
        books = filterByStatus(query, model.books)
        isBookshelf = True
        index = values2.index(query)
        
    
    view.updateMainFrame(books, isBookshelf, index)

def searchButton(query):
    books = search(query, model.books)
    
    view.updateMainFrame(books)
    
def button(type, book):
    # print(type)
    if type == "Borrow":
        answer = messagebox.askyesno(message="Apakah anda yakin akan meminjam buku ini?")
        # print(answer)
        if answer:
            borrowButton(book)
    elif type == "Queue":
        answer = messagebox.askyesno(message="Apakah anda yakin akan mengantri buku ini?")
        if answer:
            queue(book)
    elif type == "Cancel Queue":
        answer = messagebox.askyesno(message="Apakah anda yakin akan membatalkan antrian?")
        if answer:
            cancelOueueButton(book)
        
def borrow(book):
    book[3] -= 1
    book[8] += 1
    
    delta = 0
    datetime_now = datetime.now().strftime("%d-%m-%Y; %H:%M:%S")
    if book[6] == "pendidikan":
        delta = 7
    else:
        delta = 3
        
    datetime_return = (datetime.now() + timedelta(days=delta)).strftime("%d-%m-%Y; %H:%M:%S")
    
    book_new = [user[0], book[0],"", datetime_now, datetime_return]
    
    model.book_borrowed.append(book_new)
    
    return book_new
    
def borrowButton(book):
    book_new = borrow(book)
    str_datetime = calcExpiredDate(book_new)
    # print(model.book_borrowed)
    sinopsis = list(filter(lambda x: x[0] == book[0], model.book_sinopsis))
    if len(sinopsis) == 0: sinopsis.append("")
    
    view.updateBookView(book, True, False, str_datetime,sinopsis[0])

def queue(book):
    book[9] += 1
    
    model.book_borrowed.append([user[0], book[0], "queue", "", ""])
    sinopsis = list(filter(lambda x: x[0] == book[0], model.book_sinopsis))
    if len(sinopsis) == 0: sinopsis.append("")
    
    view.updateBookView(book, False, True, "", sinopsis[0])
    
def login(NIM, password):
    global user
    for user1 in model.users:
        if user1[0] == NIM:
            if user1[1] == password:
                view.init()
                user = user1
                checkBorrow()
                checkQueue()
            else:
                messagebox.showinfo(message="password salah")
                view.nim_entry.delete(0, END)
                view.pass_entry.delete(0, END)
            return
    
    answer = messagebox.askyesno(message="NIM belum terdaftar, apakah anda mau mendaftarkannya?")
    if answer:
        view.loginRegisterPage(True)
        
def createComment(book, comment):
    model.comments.append([user[0], book[0], comment])
    # comments = list(filter(lambda x: x[1] == book[0], model.comments))
    # view.updateComment(comments)
    openBookFrame(book[1])
    

def bookShelf():
    books = filterByStatus("borrow", model.books) 
        
    view.updateMainFrame(books, True)
    
def returnBookButton(book):
    answer = messagebox.askyesno(message="Apakah ada yakin akan mengembalikan buku ini?")
    if not answer: return
    
    returnBook(book)
    
    view.updateBookView(book)

def returnBook(book):
    book[8] -= 1
    book[3] += 1
    
    print(model.book_borrowed[2][1])
    print(book[0])
    print(model.book_borrowed[2][0])
    print(user[0])
    print(model.book_borrowed[2][2])
    
    [book2] = list(filter(lambda x: x[1] == book[0] and x[0] == user[0] and x[2] == "", model.book_borrowed))
    # index = model.book_borrowed.index(book2)
    
    
    model.book_borrowed.remove(book2)
    print(model.book_borrowed)
    
def cancelQueue(book):
    book[9] -= 1
    [book_borrow] = list(filter(lambda x: x[0] == user[0] and x[1] == book[0] and x[2] == "queue", model.book_borrowed))
    model.book_borrowed.remove(book_borrow)
    
def cancelOueueButton(book):
    cancelQueue(book)
    view.updateBookView(book, False, False)
    
    
def createUser(NIM, password, cpassword):
    if password != cpassword:
        messagebox.showinfo(message="password dan confirm password harus sama")
        return
    
    NIMs = list(map(lambda x: x[0], model.users))
    
    if NIM in NIMs:
        messagebox.showinfo(message="NIM sudah terdaftar")
        view.loginRegisterPage(False)
        return
    
    model.users.append([NIM, password])
    
    messagebox.showinfo(message="Pendaftaran berhasil")
    view.loginRegisterPage(False)
    


    
    
    
