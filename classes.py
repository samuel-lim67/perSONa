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
    def __init__(self, name, maxhp, currenthp, defense, maxsp, cursp, personas = []):
        self.name = name
        self.maxhp = maxhp
        self.curhp = currenthp
        self.defense = defense
        self.maxsp = maxsp
        self.cursp = cursp
        self.personas = personas


    def use_skill(self, skill):
        cost = skill.cost
        if self.cursp < cost:
            return False

        else:

            return True

class Player(Character):
    def __init__(self, name, maxhp, currenthp, defense, maxsp, cursp, personas = []):
        super().__init__(name, maxhp, currenthp, defense, maxsp, cursp, personas)


    def use_skill(self, skill):
        cost = skill.cost
        if self.cursp < cost:
            return False

        else:

            return True

    def use_random_skill(self, persona):
        skills = persona.skills
        random_skill = random.choice(skills)
        cost = random_skill.cost
        if self.cursp < cost:
            print("Not enough Skill Points!")
            return False

        else:
            return True

class Persona:
    def __init__(self, name, skills, affinity, strength, magic, endurance, agility, luck):
        self.name = name
        self.skills = skills
        self.affinity = affinity
        self.strength = strength
        self.magic = magic
        self.endurance = endurance
        self.agility = agility
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

Orpheus = Persona("Orpheus", [Agi], {"Fire": "resist", "Electric": "weak", "Dark": "weak"}, 2, 2, 2, 3, 2)
Arsene = Persona("Arsene", [Eiha], {"Ice": "weak","Light": "weak", "Dark": "resist"}, 2, 2, 2, 3, 1)
Izanagi = Persona("Izanagi", [Zio], {"Electric": "resist", "Wind": "weak", "Dark": "null"}, 3, 2, 2, 3, 2)

Cerberus = Persona("Cerberus",[Agi, Eiha, Megido],{"Ice": "weak", "Light": "null", "Dark": "resist"},25, 24, 21, 29, 19)



