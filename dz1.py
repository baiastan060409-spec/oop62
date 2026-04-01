class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def attack(self):
        print(f"{self.name} наносит удар!")
        self.strength -= 1

    def rest(self):
        print(f"{self.name} отдыхает…")
        self.health += 1

hero1 = Hero("Кирито", 100, 80, 200)
hero2 = Hero("Асуна", 99, 95, 150)

print("=== Hero 1 ===")
hero1.greet()
hero1.attack()
hero1.rest()

print(f"Здоровье: {hero1.health}, Сила: {hero1.strength}")

print("\n=== Hero 2 ===")
hero2.greet()
hero2.attack()
hero2.rest()

print(f"Здоровье: {hero2.health}, Сила: {hero2.strength}")




