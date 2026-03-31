class Hero:

    #конструктор класса
    def __init__(self, name, hp, lvl):
        #атрибуты класса
        self.name_hero = name
        self.hp_hero = hp
        self.lvl_hero = lvl

    #метод класса
    def action(self):
        return f"{self.name_hero} hero base action!!"


#обьект на основе класса
kirito = Hero("Kirito", 1000, 1000)
asuna = Hero("Asuna", 10000, 10000)
luffi = Hero("Luffi", 10000, 10000)
my_str = "Just text"


print(kirito.action())
print(asuna.action())
print(luffi.name_hero)