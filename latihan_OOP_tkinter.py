import tkinter

"""
Tkinter ini merupakan sebuah GUI yang digunakan oleh python secara build in yang artinya tidak perlu menginstall
tambahan yang lain atau bisa dikatakan jika tkinter ini sudah menjadi satu kesatuan dengan bahasa pemrograman python.
"""

main_window = tkinter.Tk()

# GUI dengan label tulisan
label1 = tkinter.Label(main_window, text = "Sigit wasis subekti")
label2 = tkinter.Label(main_window, text = "Dwi nur hamid")

# GUI dengan tombol
login = tkinter.Button(main_window, text = "Login")
register = tkinter.Button(main_window, text = "Register")

# method positioning
label1.pack()
label2.pack()
login.pack()
register.pack()

# method menampilkan GUI
main_window.mainloop()

# Jadi intinya tkinter ini memberi contoh bahwa di dalam package itu menggunakan OOP python
# seperti tkinter.TK memiliki object dan class

# Dan ingat di python di setiap class memakai huruf Besar seperti Label, Button
# jika menggunakan huruf kecil seperti pack, mainloop itu merupakan method atau fungsi
