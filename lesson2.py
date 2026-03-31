from lesson1 import luffi


class Pirat:
    def __init__(self, name, reward, age):
        self.name_pirat = name
        self.reward_pirat = reward
        self.age_pirat = age

    def action(self):
        return f"{self.name_pirat} pirat one of the four yonko!! "

luffi = Pirat("Luffi", 3000000000, 19)
shanks = Pirat("Shanks", 4048900000, 41)
tich = Pirat("Tish", 2247600000, 42)
baggi = Pirat("Baggi", 3189000000, 40)

print(luffi.action())
print(shanks.action())
print(tich.action())
print(baggi.action())