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

    def use_skill(self, skill):
        cost = skill.cost
        if self.cursp < cost:
            print("Not enough Skill Points!")
            return

        self.cursp -= cost
        print(f"{self.name} used {skill.name}. It did {skill.effect} damage!")



MainCharacter = Player("Prog", 300, 150, 20, 100, 100, [])
print(MainCharacter.cursp)

#FIRE
Agi = Skill("Fire", "Agi", 3, 40, 1)
#ICE
Bufu = Skill("Ice", "Bufu", 4, 40, 1, "Freeze", 0.15)
#ELECTRIC
Zio = Skill("Electric", "Zio", 4, 40, 2, "Shock", 0.15)
#WIND
Garu = Skill("Wind", "Garu", 3, 40, 1)
#LIGHT
Kouha = Skill("Light", "Kouha", 4, 60, 1)
#DARK
Eiha = Skill("Dark", "Eiha", 4, 60, 1)
#ALMIGHTY
Megido = Skill("Almighty", "Megido", 20, 170, 4)
print(Agi.name, Agi.cost, Agi.element, Agi.effect, Agi.targets)

MainCharacter.use_skill(Agi)

print(MainCharacter.cursp)