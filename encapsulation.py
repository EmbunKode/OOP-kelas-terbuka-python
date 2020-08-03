"""
Encapsulation
- buat semua variabel menjadi private
- menggunakan fungsi getter dan setter
- getter untuk mengambil data dari variabel
- setter untuk mensetting data dari variabel
"""


class Hero:

    def __init__(self, name, health, attackPower):
        self.__name = name
        self.__health = health
        self.__attackPower = attackPower

    # getter
    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health

    def getAttackPower(self):
        return self.__attackPower

    # setter
    def diserang(self, serangPower):
        self.__health -= serangPower

    def aturAtt(self, nilaibaru):
        self.__attackPower = nilaibaru


# awal dari game
earthshaker = Hero("earthshaker", 100, 5)

# game berjalan
print(earthshaker.getName())
# ambil health dari earthshaker
print(earthshaker.getHealth())
# earthshaker diserang dengan serangPower sebesar 78
earthshaker.diserang(78)
# tampilkan health dari earthshaker
print(earthshaker.getHealth())
# setter attack power
earthshaker.aturAtt(599)
# tampilkan attack power
print(earthshaker.getAttackPower())