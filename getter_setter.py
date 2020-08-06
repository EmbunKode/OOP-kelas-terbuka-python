"""
Ecanpsulation dengan GETTER, SETTER AND DELETER PYTHON
- Didalam class Hero memiliki method __init__ yang berisi self.info namun info ini masih bisa dirubah
- Terus bagaimana supaya tidak bisa dirubah yaitu dengan menggunakan dekorator yang namanya @property

- namun jika pada property info dengan varibel info dibuat menjadi private variabel dan info hanya mereturn self.__info
maka tidak dapat mengubah name
"""


class Hero:

    def __init__(self, name, health, armor):
        self.name = name
        self.__health = health
        self.__armor = armor
        # self.__info = "name {} : \n\thealth: {}".format(self.name, self.__health)

    # dekorator property digunakan untuk membuat setter dan getter
    # membuat method info seperti variabel
    @property
    def info(self):
        return "name {} : \n\thealth: {}".format(self.name, self.__health)

    # property getter
    @property
    def armor(self):
        pass

    @armor.getter
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self, nilaibaru):
        self.__armor = nilaibaru

    @armor.deleter
    def armor(self):
        print('armor di delete')
        self.__armor = None


# object dengan nama sniper
sniper = Hero('sniper', 100, 10)

# mencetak variabel info sebelum name diubah
print(sniper.info)

# mengubah nama dari variabel name melalui method info
# variabel name adalah public variabel
sniper.name = "Sigit"

# mencetak variabel info setelah name diubah
print(sniper.info)

# Cetak getter dan setter untuk __armor
print(sniper.armor)
print(sniper.__dict__)
sniper.armor = 212
print(sniper.armor)
print(sniper.__dict__)

# delete method armor
del sniper.armor
print(sniper.__dict__)
