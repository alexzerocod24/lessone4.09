
from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        print("Боец наносит удар мечом.")

class Bow(Weapon):
    def attack(self):
        print("Боец наносит удар из лука.")

class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon):
        self.weapon = weapon
        weapon_type = weapon.__class__.__name__
        print(f"{self.name} выбирает {weapon_type.lower()}.")

    def attack(self):
        if self.weapon:
            self.weapon.attack()
        else:
            print(f"{self.name} безоружен.")

class Monster:
    def __init__(self, name):
        self.name = name

    def defeated(self):
        print(f"{self.name} побежден!")


def battle(fighter, monster):
    fighter.attack()
    monster.defeated()

if __name__ == "__main__":

    fighter = Fighter("Боец")
    monster = Monster("Монстр")

    sword = Sword()
    fighter.change_weapon(sword)
    battle(fighter, monster)

    bow = Bow()
    fighter.change_weapon(bow)
    battle(fighter, monster)


