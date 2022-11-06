# file yang harus di run untuk memulai menjalankan program
import view.views as v
import model.models as m


# persiapan data sebelum tampilan app/program muncul
m.loadBooks()
m.loadBorrows()
m.loadComments()
m.loadSinopsis()
m.loadUsers()

# memunculkan tampilan app/program
v.firstRun()

# penyimpanan data sebelum app/program dimatikan sepenuhnya
m.saveBooks()
m.saveBorrows()
m.saveComments()
m.saveUsers()

