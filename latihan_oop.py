"""
Latihan Object Oriented Programming
Sesi latihan ini yaitu tentang Game Sederhana Saling Serang
Antara Hero Sniper melawan Hero Rikimaru
"""


class Hero:

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
        attack_diterima = attackPower_lawan/self.armorNumber
        print(f'serangan menghabiskan health sebesar = {attack_diterima}')

    def bertahan(self, lawan):
        print(self.name + ' Bertahan ketika dilawan ' + lawan.name)


sniper = Hero('sniper', 100, 10, 5)
rikimaru = Hero('rikimaru', 100, 5, 10)
ucup = Hero('ucup', 300, 40, 25)

sniper.serang(rikimaru)
rikimaru.serang(sniper)
print('\n')
ucup.serang(rikimaru)
rikimaru.serang(ucup)
print('\n')
ucup.bertahan(rikimaru)
sniper.bertahan(rikimaru)
