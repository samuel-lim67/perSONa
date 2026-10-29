import random
<<<<<<< Updated upstream
=======
import math


def target_selector(enemies):
    alive_enemies = alive_characters(enemies)
    targets = []
    for enemy in alive_enemies:
        for persona in enemy.personas:
            target = (persona, enemy)
            targets.append(target)
    for index, (persona, enemy) in enumerate(targets):
        print(f"{index + 1} - {persona.name} : {enemy.name}")
    print(f"{len(targets) + 1} - Back")
    while True:
        try:
            selection = int(input("Who would you like to attack?\n"))

            if 1 <= selection <= len(alive_enemies):
                return targets[selection - 1]
            elif selection == (len(alive_enemies) + 1):
                return None
            else:
                print("Please select a valid target!")
        except ValueError:
            print("Please enter a valid input!")

def alive_characters(combatants):
    alive_combatants = [character for character in combatants if character.curhp > 0]
    return alive_combatants

def npc_target_selector(targets):
    alive_targets = alive_characters(targets)
    targets_list = []
    for enemy in alive_targets:
        for persona in enemy.personas:
            target = (persona, enemy)
            targets_list.append(target)
    return random.choice(targets_list)

def calculate_damage(skill, persona, target_persona, enemy):
    if isinstance(skill, PhysicalAttack):
        offense = persona.strength
    elif isinstance(skill, ElementalAttack):
        offense = persona.magic
    else:
        return 0, "No effect."
    damage = 2 * math.sqrt(skill.effect * 15 * offense / enemy.defense)
    affinity = target_persona.affinity.get(skill.element, "neutral")
    effectivness = "It was normal effectiveness."
    if affinity == "weak":
        effectivness = "It was very effective!"
        damage *= 1.5
    elif affinity == "resist":
        effectivness = "It wasn't very effective..."
        damage *= 0.5
    elif affinity == "null":
        effectivness = "It had no effect."
        return 0, effectivness
    elif affinity == "absorb":
        absorb_logic(skill, damage, target_persona, enemy)
        return None

    return round(damage), effectivness

def absorb_logic(skill, damage, target_persona, enemy):
    if enemy.curhp == enemy.maxhp:
        print(f"{target_persona.name} absorbed {skill.name}!")
    else:
        missing_hp = enemy.maxhp - enemy.curhp
        if damage < missing_hp:
            enemy.curhp += round(damage, 1)
            print(f"{target_persona.name} absorbed {skill.name}! {enemy.name} healed {round(damage,1)} HP...")
        else:
            enemy.curhp += missing_hp(round,1)
            print(f"{target_persona.name} absorbed {skill.name}! {enemy.name} healed {round(missing_hp, 1)} HP...")

def check_effectiveness(effectiveness, enemy):
    if enemy.curhp <= 0:
        return False

    if effectiveness == "It was very effective!":
        if not enemy.knocked_down:
            print(f"{enemy.name} was knocked down!")
            print("One more turn!")
            enemy.knocked_down = True
            return True
        else:

            print(f"{enemy.name} is still knocked down")
            return False
    else:
        return False

def side_effect(skill_to_use, enemy):
    sideeffecttype, sideeffect_chance = skill_to_use.sideeffect
    if enemy.status_effect:
        return
    else:
        if sideeffecttype is None:
            return
        else:
            chance = random.random()
            if chance <= sideeffect_chance:
                enemy.status_effect = sideeffecttype
                print(f"{sideeffecttype} was applied on {enemy.name}!")

def critical_hit(skill_to_use, enemy, damage):
    chance = random.random()
    if chance <= skill_to_use.criticalchance:
        print("Critical hit!")
        return damage*1.5
    else:
        if enemy.status_effect == "Freeze":
            print("Critical hit!")
            return damage*1.5
        elif enemy.status_effect == "Shock":
            chance = random.random()
            if chance <= 0.35:
                print("Critical hit!")
                return damage*1.5
            else:
                return damage
        else:
            return damage
>>>>>>> Stashed changes

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

        self.equipped_persona = (self.personas[0] if self.personas else None)

    def use_skill(self, skill):
        cost = skill.cost
        if self.cursp < cost:
            print("Not enough Skill Points!")
            return False

        else:
            return True

class Player(Character):
    def __init__(self, name, maxhp, currenthp, defense, maxsp, cursp, personas = []):
        super().__init__(name, maxhp, currenthp, defense, maxsp, cursp, personas)

        self.equipped_persona = (self.personas[0] if self.personas else None)

    def use_skill(self, skill):
        cost = skill.cost
        if self.cursp < cost:
            print("Not enough Skill Points!")
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



