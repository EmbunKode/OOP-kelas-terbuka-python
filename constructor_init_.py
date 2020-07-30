class Hero:

    # metode yang dipanggil saat kita membuat sebuah objek.
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # Variabel self merujuk kepada objek dari class yang dibuat seperti hero1
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor


hero1 = Hero('Sniper', 100, 10, 4)
hero2 = Hero('Mirana', 100, 20, 1)
hero3 = Hero('Ucup', 10000, 200, 0)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)

