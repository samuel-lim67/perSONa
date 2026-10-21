import random

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

    def use_random_skill(self, persona):
        skills = persona.skills
        random_skill = random.choice(skills)
        cost = random_skill.cost
        if self.cursp < cost:
            print("Not enough Skill Points!")
            return

        self.cursp -= cost
        print(f"{self.name} used {random_skill.name}. It did {random_skill.effect} damage!")

class Persona:
    def __init__(self, name, skills, affinity, strength, magic, endurance, ability, luck):
        self.name = name
        self.skills = skills
        self.affinity = affinity
        self.strength = strength
        self.magic = magic
        self.endurance = endurance
        self.ability = ability
        self.luck = luck

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



Orpheus = Persona("Orpheus", [Agi, Megido], {"Fire": "normal","Ice": "weak", "Electric": "normal"}, 8, 12, 7, 10, 6)

MainCharacter = Player("Prog", 300, 150, 20, 100, 100, [Orpheus])

print(MainCharacter.cursp)

MainCharacter.use_skill(Agi)

print(MainCharacter.cursp)

MainCharacter.use_random_skill(Orpheus)

print(MainCharacter.cursp)