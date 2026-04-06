class Hero:
    def __init__(self, name, level,  health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def attack(self):
        print(f"{self.name} герой наносит удар!")

    def rest(self):
        print(f"{self.name} герой отдыхает и восстанавливает здоровье")


class WarriorHero(Hero):
    def __init__(self, name, lvl, health, strength,  stamina):
        super().__init__(name, lvl, health, strength)
        self.stamina = stamina

    def action(self):
        print(f"i'm {self.name} Воин атакует мечом! {self.stamina}")

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def attack(self):
        print(f"{self.name} воин наносит удар!")

    def rest(self):
        print(f"{self.name} воин отдыхает и восстанавливает здоровье")


class MageHero(Hero):
    def __init__(self, name, lvl, health, strength,  mp):
        super().__init__(name, lvl, health, strength)
        self.mp = mp

    def action(self):
        print(f"i'm {self.name} Маг кастует заклинание! {self.mp}")

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def attack(self):
        print(f"{self.name} маг наносит удар!")

    def rest(self):
        print(f"{self.name} маг отдыхает и восстанавливает здоровье")


class AssassinHero(Hero):
    def __init__(self, name, lvl, health, strength, stealth ):
        super().__init__(name, lvl, health, strength)
        self.stealth = stealth

    def action(self):
        print(f"i'm {self.name} Ассасин атакует из-под тишка! {self.stealth}")

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def attack(self):
        print(f"{self.name} Ассасин наносит удар!")

    def rest(self):
        print(f"{self.name} Ассасин отдыхает и восстанавливает здоровье")

zoro = WarriorHero("Warrior", 100, 1000, 10000, 10000)
rudeus = MageHero("Mage", 100, 1000, 10000, 10000)
gabimaru = AssassinHero("Assassin", 100, 1000, 10000, 10000)


heroes = [zoro, rudeus, gabimaru]

wins = {
    "Warrior": "Assassin",
    "Assassin": "Mage",
    "Mage": "Warrior"
}

aliases = {
    "warrior": "Warrior",
    "воин": "Warrior",

    "mage": "Mage",
    "маг": "Mage",

    "assassin": "Assassin",
    "ассасин": "Assassin"
}
import random

user_input = input("Выберите героя (Warrior / Mage / Assassin):\n").lower()

if user_input not in aliases:
    print("Ошибка выбора!")
else:
    player_name = aliases[user_input]

    player = next(hero for hero in heroes if hero.name == player_name)

    enemy = random.choice(heroes)

    print(f"\nВы выбрали: {player.name}")
    print(f"Противник: {enemy.name}\n")

    player.attack()
    enemy.attack()

    if player.name == enemy.name:
        print("\nНичья!")
    elif wins[player.name] == enemy.name:
        print(f"\n{player.name} победил!")
    else:
        print(f"\n{enemy.name} победил!")