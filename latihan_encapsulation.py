"""
Latihan Encapsulation ini akan menggunakan Sistem Level dan Experience
jadi ketika hero1 menyerang maka experience akan nambah dan levelnya akan naik begitupun sebaliknya
"""


class Hero:
    # private class variabel
    __jumlah = 0

    def __init__(self, name, health, attPower, armor):
        self.__name = name
        self.__healthStandar = health
        self.__attPowerStandar = attPower
        self.__armorStandar = armor
        self.__level = 1
        self.__exp = 0

        self.__heatlhMax = self.__healthStandar * self.__level
        self.__attPower = self.__attPowerStandar * self.__level
        self.__armor = self.__armorStandar * self.__level

        self.__health = self.__heatlhMax

        Hero.__jumlah += 1

    @property
    def info(self):
        return "{} level {} : \n\thealth = {}/{} \n\tattack = {} \n\tarmor = {}".format(self.__name, self.__level,
                                                                                        self.__health,
                                                                                        self.__heatlhMax,
                                                                                        self.__attPower,
                                                                                        self.__armor)

    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self, addExp):
        self.__exp += addExp
        if self.__exp >= 100:
            print(self.__name, 'level up')
            self.__level += 1
            self.__exp -= 100

            self.__heatlhMax = self.__healthStandar * self.__level
            self.__attPower = self.__attPowerStandar * self.__level
            self.__armor = self.__armorStandar * self.__level

    def attack(self, musuh):
        self.gainExp = 299


slandar = Hero('slandar', 100, 5, 10)
axe = Hero('axe', 100, 5, 10)
print(slandar.info)

slandar.attack(axe)
slandar.attack(axe)
slandar.attack(axe)
slandar.attack(axe)
print(slandar.info)
