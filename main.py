import view.views as v
import model.models as m


# v.init()
m.loadBooks()
m.loadBorrows()
print(m.book_borrowed)
m.loadComments()
m.loadSinopsis()
m.loadUsers()
v.firstRun()
m.saveBooks()
m.saveBorrows()
m.saveComments()
m.saveUsers()

