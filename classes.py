class Skill:
    def __init__(self, element, name, cost, effect, targets, sideeffecttype = None, sideeffectchance = None):
        self.element = element
        self.name = name
        self.cost = cost
        self.effect = effect
        self.targets = targets
        self.sideeffect = (sideeffecttype, sideeffectchance)


class Character:
    def __init__(self, name, maxhp, currenthp, defense):
        self.name = name
        self.maxhp = maxhp
        self.curhp = currenthp
        self.defense = defense

class Player(Character):
    def __init__(self, name, maxhp, currenthp, defense, maxsp, cursp, personas):
        super().__init__(name, maxhp, currenthp, defense)

        self.maxsp = maxsp
        self.cursp = cursp
        self.personas = personas

    def check_spcost(self, cost):
        if self.cursp < cost:
            return False
        elif self.cursp >= cost:
            return True
        else:
            return None


MainCharacter = Character("Prog", 300, 150, 20)
print(MainCharacter.defense)

Agi = Skill("Fire", "Agi", 3, 40, 1)
Bufu = Skill("Ice", "Bufu", 4, 40, 1, "Freeze", 0.15)
print(Agi.name, Agi.cost, Agi.element, Agi.effect, Agi.targets)