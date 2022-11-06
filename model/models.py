# Gambaran data dalam bentuk matrix setelah diambil dari file

# books = [[
#     "1", "phiwiki", "budi", 1, "phiwiki.png", "erlangga", "pendidikan", "2004", 0, 1
# ],[
#     "2","mathco", "joko", 14, "phiwiki.png", "ITB", "pendidikan", "2010", 1, 0
# ],[
#     "3","halliday", "siti", 9, "phiwiki.png", "Gramedia", "pendidikan", "2008", 0, 0
# ],[
#     "4","ttki", "aswan", 9, "phiwiki.png", "Tim Bahasa Indonesia", "pendidikan", "2010", 1, 0
# ],[
#     "5","naruto eps 100", "maki", 0, "phiwiki.png", "Japan Co", "non-pendidikan", "2003", 0, 0
# ], [
#     "6", "phiwiki 2022", "budi", 10, "phiwiki.png", "erlangga", "pendidikan", "2004", 0, 0
# ],[
#     "7","mathco 2022", "joko", 14, "phiwiki.png", "ITB", "pendidikan", "2010", 0, 0
# ],[
#     "8","halliday edisi 12", "siti", 1, "phiwiki.png", "Gramedia", "pendidikan", "2008", 0, 0
# ],[
#     "9","ttki 2022", "aswan", 9, "phiwiki.png", "Tim Bahasa Indonesia", "pendidikan", "2010", 0, 0
# ],[
#     "10","naruto eps 273", "maki", 9, "phiwiki.png", "Japan Co", "non-pendidikan", "2003", 0, 0
# ]]

# users = [
#     ["19622193", "1234"],
#     ["19622194", "1234"]
# ]

# book_borrowed = [
#     ["19622193", "1", "queue", "", ""],
#     ["19622194", "2", "", "01-11-2022; 04:59:31", "20-11-2022; 04:59:31"],
#     ["19622193", "4", "", "01-11-2022; 04:59:31", "30-11-2022; 04:59:31"]   
# ]

# book_sinopsis = [
#     ["1", "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."],
#     ["2", "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of \"de Finibus Bonorum et Malorum\" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, \"Lorem ipsum dolor sit amet..\", comes from a line in section 1.10.32."]
# ]

# comments = [
#     ["19622193", "1", "Sangat bagus"],
#     ["19622194", "1", "Sangat bagus sekali"],
#     ["19622194", "1", "Sangat bagus sekali"],
#     ["19622194", "1", "Sangat bagus sekali"]
# ]


# data-data yang diperlukan program
books = [] #data buku, penjelasan data apa saja yang ada di satu buku: [id buku, judul buku, penulis, jumlah buku, file foto sampul buku, penerbit, tipe buku/genre/kategori, tahun terbit, jumlah pembaca, jumlah yang sedang mengantri]

users = [] #data user yang terdaftar, penjelasan data apa saja pada satu user: [NIM, password]

book_borrowed = [] #data buku apa aja yang lagi dipinjam atau sedang mengantri, penjelasan data: [NIM peminjam/pengantri, id buku yang sedang dipinjam atau id buku yang sedang mengantri, penjelasan buku dipinjam atau mengantri, tanggal peminjaman, tanggal habis masa peminjaman]

book_sinopsis = [] #data sinopsis atau keterangan buku, penjelasan data: [id buku,  sinopsis atau keterangan buku]

comments = []#data komentar atau ulasan, penjelasan data: [NIM pemberi komentar, id buku dimana komentar diberikan, isi komentar]

# penyimpanan ke sebuah file dilakukan agar data bersifat kekal tidak sementara

# kumpulan fungsi untuk mengambil data dari file lalu diubah dalam bentuk matrix
def loadUsers():
    file = open("data/users.data", "r")
    
    for line in file:
        line = line.strip()
        user =  line.split(",")
        users.append(user)
    file.close()

def loadComments():
    file = open("data/comments.data", "r")
    
    for line in file:
        line = line.strip()
        comment =  line.split(",")
       
        comments.append(comment)
    file.close()
    

def loadSinopsis():
    file = open("data/sinopsis.data", "r")
    
    for line in file:
        line = line.strip()
        sinopsis =  line.split(";")
        book_sinopsis.append(sinopsis)
    file.close()
    
       
def loadBorrows():
    file = open("data/borrows.data", "r")
    
    for line in file:
        line = line.strip()
        borrow =  line.split(",")
        book_borrowed.append(borrow)
    file.close()
    
       
def loadBooks():
    file = open("data/books.data", "r")
    
    for line in file:
        line = line.strip()
        book =  line.split(",")
        book[3] = int(book[3])
        book[8] = int(book[8])
        book[9] = int(book[9])
        books.append(book)
    print("test")
    file.close()
    
 
# kumpulan fungsi untuk menyimpan data matrix ke sebuah file  
def saveUsers():
    file = open("data/users.data", "w")
    
    users2 = list(map(lambda x: ",".join(x), users))
    str = "\n".join(users2)
    file.writelines(str)
    file.close()
    
def saveComments():
    file = open("data/comments.data", "w")
    
    comments2 = list(map(lambda x: ",".join(x), comments))
    str = "\n".join(comments2)
    file.writelines(str) 
    file.close()
    
def saveBorrows():
    file = open("data/borrows.data", "w")
    
    borrows = list(map(lambda x: ",".join(x), book_borrowed))
    str = "\n".join(borrows)
    file.writelines(str) 
    file.close()
    
def saveBooks():
    file = open("data/books.data", "w")
    
    
    for book in books:
        book[3] = str(book[3])
        book[8] = str(book[8])
        book[9] = str(book[9])
        
    book2 = list(map(lambda x: ",".join(x), books))
    str2 = "\n".join(book2)
    file.writelines(str2) 
    file.close()