class Hero:  # template/class
    pass


hero1 = Hero()  # object/instance (instanssiate)
hero2 = Hero()
hero3 = Hero()

hero1.name = "sniper"   # attribute dari object hero1
hero1.health = 100      # attribute dari object hero1

hero2.name = "sven"     # attribute dari object hero2
hero2.health = 200      # attribute dari object hero2

hero3.name = "ucup"     # attribute dari object hero3
hero3.health = 1000     # attribute dari object hero3

# fungsi __dict__ digunakan untuk membuat dictionary
print(hero1.__dict__)
print(hero1)  # menampilkan tipe data
print(hero1.name)  # menampilkan attribute name dari hero1/object
print(hero3.health)  # menampilkan attribute health dari hero3/object
