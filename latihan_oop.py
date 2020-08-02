"""
Latihan Object Oriented Programming
Sesi latihan ini yaitu tentang Game Sederhana Saling Serang
Antara Hero Sniper melawan Hero Rikimaru
"""


class Hero:

    # self adalah sebagai sebuah variable saja yang menyatakan kelas itu sendiri.
    # untuk memanggil sebuah variable dan sebuah metode yang ada pada dirinya sendiri yang diawali dengan self.
    def __init__(self, name, health, attackPower, armorNumber):
        self.armorNumber = armorNumber
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armor = armorNumber

    def serang(self, lawan):
        print(self.name + ' menyerang ' + lawan.name)
        lawan.diserang(self, self.attackPower)

    def diserang(self, lawan, attackPower_lawan):
        print(self.name + ' diserang ' + lawan.name)
        # attack_diterima = 20 / 5
        attack_diterima = attackPower_lawan/self.armorNumber
        print(f'serangan terasa = ' + str(attack_diterima))
        # darah atau health dikurang dengan attack_diterima
        self.health -= attack_diterima
        print('darah ' + self.name + ' tersisa ' + str(self.health))

    def bertahan(self, lawan):
        print(self.name + ' Bertahan ketika dilawan ' + lawan.name)


# name: sniper, health: 100, attackPower: 10, armorNumber: 5
sniper = Hero('sniper', 100, 10, 5)
rikimaru = Hero('rikimaru', 100, 20, 10)
# ucup = Hero('ucup', 300, 40, 25)

sniper.serang(rikimaru)
print('\n')
rikimaru.serang(sniper)
# print('\n')
# ucup.serang(rikimaru)
# rikimaru.serang(ucup)
# print('\n')
# ucup.bertahan(rikimaru)
# sniper.bertahan(rikimaru)
