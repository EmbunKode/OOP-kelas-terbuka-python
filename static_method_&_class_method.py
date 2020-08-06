"""
STATIC METHOD DAN CLASS METHOD
"""
class Hero:

    __jumlah = 0

    def __init__(self, name):
        self.__name = name
        Hero.__jumlah += 1

    # method ini hanya berlaku untuk object tidak untuk class
    def getJumlah(self):
        return Hero.__jumlah

    # method ini hanya berlaku untuk class tidak untuk object
    def getJumlah1():
        return Hero.__jumlah

    # maka supaya keduanya bisa diakses baik diclass maupun di object maka gunakan statismethod
    # method static (decorator) nempel ke object dan class dia tidak butuh instance maupun attribut-attribut lain
    # dalam class-nya dan dia juga tidak diwajibkan menyertakan parameter khusus.
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah

    # method class diawali dengan decorator @classmethod dan wajib menyertakan cls pada parameternya,
    # dimana cls merujuk pada kelas itu sendiri.
    # namun class method masih dapat diakses melalui object tidak hanya melalui class saja
    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah

# object
rikimaru = Hero('rikimaru')
drowranger = Hero('drowranger')
sniper = Hero('sniper')

# tampilkan hanya dapat diakses oleh class
print(Hero.getJumlah1())
# tampilkan hanya dapat diakses oleh object
print(sniper.getJumlah())
# tampilkan static method dan dapat diakses melalui class dan object
print(Hero.getJumlah2())
print(sniper.getJumlah2())
# tampilkan class method dan masih dapat diakses melalui class dan object
print(rikimaru.getJumlah3())
print(Hero.getJumlah3())
