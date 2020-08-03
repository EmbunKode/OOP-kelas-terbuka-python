"""
_single_leading_underscore
Aturan ini dipakai untuk mendeklarasikan variabel, fungsi, method, atau kelas private di sebuah module.

single_trailingunderscore
Aturan ini dipakai bisanya untuk menhindari konflik penamaan dengan keyword Python atau perintah yang lain.

__double_leading_underscore
Double underscore dipakai untuk menghindari konflik nama atribute antar kelas.

__double_leading_and_trailingunderscore_\
Aturan penulis ini dipakai untuk variabel atau method khusus (yang disebut juga "magic methods")
seperti __init__ dan __len__.
"""

class Hero:

    # class variabel
    jumlah = 0
    __private_jumlah = 10

    def __init__(self, name, health):
        self.name = name
        self.health = health

        # variable instance private
        self.__private = "private"
        # variable instance protected
        self._protected = "protected"

lina = Hero("Lina", 100)

print(lina.__dict__)
# private variabel di dalam method atau object
print(lina.__private)
# _protected masih sama halnya dengan variabel public
print(lina._protected)
# private variabel di dalam class
print(Hero.__private_jumlah)