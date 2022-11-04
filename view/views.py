from tkinter import *
from tkinter import ttk

from pip import main
import model.models as model
import controller.controllers as con

app = Tk()

def loginFrame():
    global login_frame, nim_entry, pass_entry
    login_frame = Frame(app)
    
    login_frame.columnconfigure(0, weight=1)
    login_frame.columnconfigure(1, weight=1)
    login_frame.columnconfigure(2, weight=1)
    login_frame.columnconfigure(3, weight=1)
    
    nim_label = Label(login_frame, text="NIM : ")
    pass_label = Label(login_frame, text="password : ")
    nim_entry = Entry(login_frame)
    pass_entry = Entry(login_frame, show="*")
    login_button = Button(login_frame, text="Login", command=lambda: con.login(nim_entry.get(), pass_entry.get()))
    exit_button = Button(login_frame, text="Exit", command=app.quit)
    signup_label = Label(login_frame, text="Sign up", fg="blue", font=("Times 10 underline"))
    
    signup_label.bind("<Button-1>", lambda e: loginRegisterPage(True))
    signup_label.bind("<Enter>", lambda e: e.widget.config(font=("Times 11 underline bold")))
    signup_label.bind("<Leave>", lambda e: e.widget.config(font=("Times 10 underline")))
    
    nim_label.grid(column=0, row=0)
    pass_label.grid(column=0, row=1)
    nim_entry.grid(column=1, row=0, columnspan=2)
    pass_entry.grid(column=1, row=1, columnspan=2)
    exit_button.grid(column=1, row=2)
    login_button.grid(column=2, row=2)
    signup_label.grid(column=0, row=3, columnspan=3)
    
def registerFrame():
    global register_frame, pass_entry, cpass_entry
    register_frame = Frame(app)
    
    register_frame.columnconfigure(0, weight=1)
    register_frame.columnconfigure(1, weight=1)
    register_frame.columnconfigure(2, weight=1)
    register_frame.columnconfigure(3, weight=1)
    
    nim_label = Label(register_frame, text="NIM : ")
    pass_label = Label(register_frame, text="password : ")
    cpass_label = Label(register_frame, text="confirm password : ")
    nim_entry = Entry(register_frame)
    pass_entry = Entry(register_frame, show="*")
    cpass_entry = Entry(register_frame, show="*")
    register_button = Button(register_frame, text="Register", command=lambda: con.createUser(nim_entry.get(), pass_entry.get(), cpass_entry.get()))
    exit_button = Button(register_frame, text="Exit", command=app.quit)
    signin_label = Label(register_frame, text="Sign in", fg="blue", font=("Times 10 underline"))
    
    signin_label.bind("<Button-1>", lambda e: loginRegisterPage(False))
    signin_label.bind("<Enter>", lambda e: e.widget.config(font=("Times 11 underline bold")))
    signin_label.bind("<Leave>", lambda e: e.widget.config(font=("Times 10 underline")))
    
    nim_label.grid(column=0, row=0)
    pass_label.grid(column=0, row=1)
    cpass_label.grid(column=0, row=2)
    nim_entry.grid(column=1, row=0, columnspan=2)
    pass_entry.grid(column=1, row=1, columnspan=2)
    cpass_entry.grid(column=1, row=2, columnspan=2)
    exit_button.grid(column=1, row=3)
    register_button.grid(column=2, row=3)
    signin_label.grid(column=0, row=4, columnspan=3)
    

def headerFrame():
    global header_frame
    header_frame = Frame(app, background="blue", pady=20, padx=15)
    
    header_frame.columnconfigure(2, weight=1)
    header_frame.columnconfigure(3, weight=1)
    header_frame.columnconfigure(4, weight=1)
    
    search_entry = Entry(header_frame, width=30)
    search_button = Button(header_frame, text="Search", command=lambda: con.searchButton(search_entry.get()))
    bookshelf_label = Label(header_frame, text="Bookshelf", font=("Times 15 bold"), fg="white", bg="blue")
    collection_label = Label(header_frame, text="Collections", font=("Times 15 bold"), fg="white", bg="blue")
    logout_label = Label(header_frame, text="Logout", font=("Times 15 bold"), fg="white", bg="blue")
    
    collection_label.bind("<Button-1>", lambda e: updateMainFrame(model.books))
    bookshelf_label.bind("<Button-1>", lambda e:con.bookShelf())
    logout_label.bind("<Button-1>", lambda e:con.logout())
    collection_label.bind("<Enter>", lambda e: e.widget.config(font=("Times 15 underline bold")))
    collection_label.bind("<Leave>", lambda e: e.widget.config(font=("Times 15 bold")))
    bookshelf_label.bind("<Enter>", lambda e: e.widget.config(font=("Times 15 underline bold")))
    bookshelf_label.bind("<Leave>", lambda e: e.widget.config(font=("Times 15 bold")))
    logout_label.bind("<Enter>", lambda e: e.widget.config(font=("Times 15 underline bold")))
    logout_label.bind("<Leave>", lambda e: e.widget.config(font=("Times 15 bold")))
    
    bookshelf_label.grid(column=3,row=0)
    collection_label.grid(column=2, row=0)
    logout_label.grid(column=4, row=0)
    search_entry.grid(column=0, row=0)
    search_button.grid(column=1, row=0)
    
def updateMainFrame(books, isBookshelf = False, current = 0):
    for widget in app.winfo_children():
        if widget == header_frame: continue
        widget.destroy()
    
    mainFrame(books, isBookshelf, current)
    main_frame.pack(expand=YES, fill=BOTH)
    
def mainFrame(books, isBookshelf = False, current = 0):
    global main_frame, book_category, scrollbar
    main_frame = Frame(app)
    canvas = Canvas(main_frame)
    scrollbar = ttk.Scrollbar(app, orient="vertical", command=canvas.yview)
    
    # category = StringVar()
    values = []
    if isBookshelf: 
        values = ["borrow", "queue"]
        # category.set("borrow")
    else: 
        values=["All", "pendidikan", "non-pendidikan"]
        # category.set("All")
    book_category = ttk.Combobox(main_frame, values=values, width=800)
    book_category.current(current)
    book_category.bind("<<ComboboxSelected>>", lambda e: con.filterCombobox(e.widget.get()))
    
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    
    container = Frame(canvas)
    canvas.create_window((0,0), window=container, anchor="nw")
    
    book_category.pack(side=TOP, fill=Y)
    canvas.pack(expand=YES, fill=BOTH)
    scrollbar.pack(side=RIGHT, fill=Y)
    # container.bind("<Motion>", lambda e: print(e))
    
    for i in range(5):
        # container.rowconfigure(i, weight=1)
        for j in range(4):
            if i*4 + j >= len(books): break
            
            bg = PhotoImage(file=f"asset/{books[i*4 + j][4]}", width=190, height=270)
            # container.columnconfigure(j, weight=1)
            
            book_frame = Frame(container, highlightbackground="black", highlightthickness=3, width=50, height=50, border=1)
            book_frame.grid(column=j, row=i, padx=3, pady=3)
            
            book_label = Label(book_frame, image=bg)
            title_label = Label(book_frame, text=f"{books[i*4 + j][1]}", compound=TOP, font=("Helvetica 12"))
            author_label = Label(book_frame, text=f"{books[i*4 + j][2]}", fg="blue", font=("Helvetica 10"))
            
            title_label.bind("<Enter>", lambda e: e.widget.config(font=("Helvetica 12 underline")))
            title_label.bind("<Leave>", lambda e: e.widget.config(font=("Helvetica 12")))
            
            # author_label.bind("<Enter>", lambda e: e.widget.config(font=("Helvetica 10 underline")))
            # author_label.bind("<Leave>", lambda e: e.widget.config(font=("Helvetica 10")))
            
            title_label.bind("<Button-1>", lambda e: con.openBookFrame(e.widget.cget("text")))
            author_label.bind("<Button-1>", lambda e: print(e.x_root, e.y_root))
            
            book_label.pack()
            title_label.pack()
            author_label.pack()
            book_label.image = bg
            
def bookView(book, comments, isBooked=False, isQueued = False, str_datetime = "", sinopsis =""):
    for widget in app.winfo_children():
        if widget == header_frame: continue
        widget.destroy()
    
    bookFrame(book, comments)
    updateBookView(book, isBooked, isQueued, str_datetime, sinopsis)
    book_frame.pack(side=LEFT, fill=Y, expand=NO)

def updateBookView(book, isBooked = False, isQueued = False, str_datetime = "", sinopsis =""):
    if isBooked: 
        button_var.set("Read")
        return_button.pack(fill=X,side=BOTTOM)
        expired_date_label.pack(fill=X,side=BOTTOM)
    elif isQueued: button_var.set("Cancel Queue")
    elif book[3] == 0 and not isQueued:button_var.set("Queue") 
    else: 
        button_var.set("Borrow")
        return_button.pack_forget()
        expired_date_label.pack_forget()
    sinopsis_text.insert(END, sinopsis)
    sinopsis_text.config(state=DISABLED)
    date_var.set(str_datetime)
    readers_var.set(book[8])
    queue_var.set(book[9])
    copy_var.set(f"{book[3]} COPY")
    
def bookFrame(book, comments):
    global return_button, book_frame, button_var, readers_var, queue_var, copy_var, borrow_button, left_container, date_var, expired_date_label, sinopsis_text, comment2_container, comment_container, right_container
    book_frame = Frame(app)
    
    left_container = Frame(book_frame, borderwidth=2, relief="solid")
    left_container.rowconfigure(0, weight=1)
    left_container.rowconfigure(1, weight=1)
    left_container.rowconfigure(2, weight=1)
    left_container.rowconfigure(3, weight=1)
    left_container.rowconfigure(4, weight=1)
    left_container.rowconfigure(5, weight=1)
    left_container.rowconfigure(6, weight=1)

    bg = PhotoImage(file=f"asset/{book[4]}", width=190, height=270)
    book_image = Label(left_container, image=bg)
    copy_label = Label(left_container, text="Copy Number", font=("Helvetica 8"), fg="gray")
    back_label = Label(left_container, text="<", font=("Times 20 bold"), fg="gray")
    back_label.bind("<Button-1>", lambda e: updateMainFrame(model.books))
    back_label.bind("<Enter>", lambda e: e.widget.config(fg="black"))
    back_label.bind("<Leave>", lambda e: e.widget.config(fg="gray"))
    
    copy_var = StringVar()
    copy_count_label = Label(left_container, font=("Helveltica 15"), fg="blue", textvariable=copy_var)
    
    title_label = Label(left_container, text=f"{book[1]}", compound=TOP, font=("Helvetica 12"))
    book_image.image = bg
    
    information = f"""
    Genre    : {book[6]}
    Author   : {book[2]}
    Penerbit : {book[5]}
    Tahun    : {book[7]}
    Id       : {book[0]}
    """
    
    information_label = Label(left_container, text=information, fg="gray", font=("Helvetica 9"))
    container = Frame(left_container)
    readers_label = Label(container, text=f"readers", font=("Helvetica 8"), fg="gray")
    queue_label = Label(container, text=f"queue", font=("Helvetica 8"), fg="gray")
    
    readers_var = IntVar()
    many_readers_label = Label(container, font=("Helvetica 12"), textvariable=readers_var)
    
    queue_var = IntVar()
    many_queue_label = Label(container, font=("Helvetica 12"), textvariable=queue_var)
    
    button_var = StringVar()
    borrow_button = Button(left_container, textvariable=button_var, command=lambda: con.button(button_var.get(), book))
    return_button = Button(left_container, text="Return", command=lambda: con.returnBookButton(book))
    
    date_var = StringVar()
    expired_date_label = Label(left_container, textvariable=date_var, font=("Helvetica 8"), fg="gray")
    
    container.columnconfigure(0, weight=1)
    container.columnconfigure(1, weight=1)
    
    right_container = Frame(app)
    
    sinopsis_container = Frame(right_container, height=400)
    sinopsis_container.pack_propagate(False)
    sinopsis_text = Text(sinopsis_container, font="Times 12")
    sinopsis_label = Label(sinopsis_container, text="Sinopsis/Keterangan", font=("Times 15 bold"))
    
    comment_container = Frame(right_container, height=150)
    comment_container.pack_propagate(False)
    entry_container = Frame(right_container)
    comment_entry = Entry(entry_container, width=100)
    comment_button = Button(entry_container, text=">", font="Helvatica 12 bold", command=lambda: con.createComment(book, comment_entry.get()))
    comment_label = Label(right_container, text="Comment", font=("Times 15 bold"))
    canvas = Canvas(comment_container)
    canvas.pack(side=LEFT, expand=YES, fill=BOTH)
    scrollbar = ttk.Scrollbar(comment_container, orient="vertical", command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    comment2_container = Frame(canvas)
    
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0,0), window=comment2_container, anchor="nw", width=600)
    
    for comment in comments:
        comment_frame = Frame(comment2_container)
        user_label = Label(comment_frame, text=comment[0], font="Times 10 underline bold", anchor="w")
        comment2_label = Label(comment_frame, text=comment[2], anchor="w")
        user_label.pack(anchor="w")
        delete_label = Label(comment_frame, text="delete", fg="gray", font="Times 9", anchor="e")
    
        if comment[0] == con.user[0]: delete_label.pack(side=RIGHT, anchor="ne")
        delete_label.bind("<Button-1>", lambda e: con.deleteComment(e.widget.winfo_parent(), book))
        delete_label.bind("<Enter>", lambda e: e.widget.config(fg="black"))
        delete_label.bind("<Leave>", lambda e: e.widget.config(fg="gray"))
        comment2_label.pack(anchor="w")
        
        comment_frame.pack(anchor="w", fill=X)
        ttk.Separator(comment2_container, orient='horizontal').pack(fill=X)
        
    back_label.pack(fill=X, anchor=W)
    ttk.Separator(left_container, orient='horizontal').pack(fill=X)
    book_image.pack(fill=X)
    title_label.pack(fill=X)
    ttk.Separator(left_container, orient='horizontal').pack(fill=X)
    copy_label.pack()
    copy_count_label.pack()
    ttk.Separator(left_container, orient='horizontal').pack(fill=X)
    information_label.pack()
    ttk.Separator(left_container, orient='horizontal').pack(fill=X)
    many_readers_label.grid(column=0, row=0)
    many_queue_label.grid(column=1, row=0)
    readers_label.grid(column=0, row=1)
    queue_label.grid(column=1, row=1)
    container.pack(fill=X, pady=5)
    borrow_button.pack(fill=X,side=BOTTOM)
    
    sinopsis_label.pack(side=TOP, fill=X, expand=NO)
    sinopsis_text.pack(expand=YES, fill=BOTH, side=BOTTOM)
    
    comment_entry.grid(column=0, row=0)
    comment_button.grid(column=1, row=0)
    
    sinopsis_container.pack(fill=X, expand=NO)
    comment_label.pack(fill=X)
    ttk.Separator(right_container, orient='horizontal').pack(fill=X)
    comment_container.pack(fill=X, expand=NO)
    ttk.Separator(right_container, orient='horizontal').pack(fill=X)
    entry_container.pack(fill=X, side=BOTTOM, pady=3)
    
    left_container.pack(side=LEFT, fill=Y, expand=YES)    
    right_container.pack(side=RIGHT, expand=YES, padx=5)
    
def firstRun():
    loginFrame()
    login_frame.pack(expand=YES)
    app.geometry("850x780")
    app.resizable(False, False)
    app.mainloop()

def init():
    login_frame.destroy()
    headerFrame()
    mainFrame(model.books)
    header_frame.pack(side=TOP, expand=NO, fill=X, ipady=40)
    main_frame.pack(expand=YES, fill=BOTH)
    
def loginRegisterPage(isLogin, isLogout=False):
    if isLogin:
        login_frame.destroy()
        registerFrame()
        register_frame.pack(expand=YES)
    elif not isLogin and not isLogout:
        register_frame.destroy()
        loginFrame()
        login_frame.pack(expand=YES)
    elif isLogout:
        for widget in app.winfo_children():
            widget.destroy()
        loginFrame()
        login_frame.pack(expand=YES)
            
    
def openReadFrame(book):
    for widget in right_container.winfo_children():
        widget.destroy()
    
    right_container.pack_forget()
    readFrame(book)
    scrollbar2.pack(side=RIGHT, fill=Y)
    back_label2.pack(side=TOP)
    canvas2.pack(expand=YES)
    
    right_container.pack(fill=BOTH, expand=YES)
 
def readFrame(book):
    global back_label2, canvas2, scrollbar2
    back_label2 = Label(right_container, text="<", font="Times 14", fg="gray", width=600)
    back_label2.pack_propagate(False)
    # 
    canvas2 = Canvas(right_container, width=600, height=700)
    # canvas2.pack_propagate(False)
    scrollbar2 = ttk.Scrollbar(right_container, orient="vertical", command=canvas2.yview)
    
    container2 = Frame(canvas2)
    canvas2.configure(yscrollcommand=scrollbar2.set)
    canvas2.bind("<Configure>", lambda e: canvas2.configure(scrollregion=canvas2.bbox("all")))
    canvas2.create_window((0,0), window=container2, anchor="nw")
    
    bg1 = PhotoImage(file="asset/page2.png")
    bg2 = PhotoImage(file="asset/page1.png")
    bg3 = PhotoImage(file="asset/page3.png")
    bg4 = PhotoImage(file="asset/page4.png")
    read_label1 = Label(container2, image=bg1)
    read_label2 = Label(container2, image=bg2)
    read_label3 = Label(container2, image=bg3)
    read_label4 = Label(container2, image=bg4)
    read_label1.image = bg1
    read_label2.image = bg2
    read_label3.image = bg3
    read_label4.image = bg4
    
    
    read_label1.pack(fill=X, expand=YES)
    read_label2.pack(fill=X, expand=YES)
    read_label3.pack(fill=X, expand=YES)
    read_label4.pack(fill=X, expand=YES)
    
    # for i in range(10):
    #     Button(container2, text="Tobol").pack(fill=BOTH, expand=YES)
    
    back_label2.bind("<Button-1>", lambda e: con.openBookFrame(book[1]))
    back_label2.bind("<Enter>", lambda e: e.widget.config(fg="black"))
    back_label2.bind("<Leave>", lambda e: e.widget.config(fg="gray"))
    
    
    
   
