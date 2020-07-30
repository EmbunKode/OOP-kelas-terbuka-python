class Hero:
    # class variabel
    jumlah = 0

    # __init__  metode yang dipanggil saat kita membuat sebuah objek.
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # instance variabel
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1
        print("membuat hero dengan nama " + inputName)


hero1 = Hero('Sniper', 100, 10, 4)
print(Hero.jumlah)
hero2 = Hero('Mirana', 100, 20, 1)
print(Hero.jumlah)
hero3 = Hero('Ucup', 10000, 200, 0)
print(Hero.jumlah)

# NB
"""
    Maka class variable akan nempel/kepunyaan class Hero
    sedangkan instance variable akan nempel/kepunyaan object hero1, hero2 dll 
"""
