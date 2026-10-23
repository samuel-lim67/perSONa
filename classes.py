import random

def target_selector(enemies):
    alive_enemies = alive_characters(enemies)
    for index, enemy in enumerate(alive_enemies):
        print(f"{index + 1} - {enemy.name}")
    print(f"{len(alive_enemies) + 1} - Back")
    while True:
        try:
            selection = int(input("Who would you like to attack?\n"))

            if 1 <= selection <= len(alive_enemies):
                return alive_enemies[selection - 1]
            elif selection == (len(alive_enemies) + 1):
                return None
            else:
                print("Please select a valid target!")
        except ValueError:
            print("Please enter a valid input!")

def alive_characters(combatants):
    alive_combatants = [character for character in combatants if character.curhp > 0]
    return alive_combatants

def npc_target_selector(allies):
    alive_allies = alive_characters(allies)
    return random.choice(alive_allies)

class Skill:
    def __init__(self, element, name, cost, effect, targets, sideeffecttype = None, sideeffectchance = None):
        self.element = element
        self.name = name
        self.cost = cost
        self.effect = effect
        self.targets = targets
        self.sideeffect = (sideeffecttype, sideeffectchance)


class Character:
    def __init__(self, name, maxhp, currenthp, defense, maxsp, cursp, personas = None):
        self.name = name
        self.maxhp = maxhp
        self.curhp = currenthp
        self.defense = defense
        self.maxsp = maxsp
        self.cursp = cursp
        self.personas = personas if personas is not None else []


    def use_skill(self, skill):
        cost = skill.cost
        if self.cursp < cost:
            return False

        else:
            return True

class Player(Character):
    def __init__(self, name, maxhp, currenthp, defense, maxsp, cursp, personas = None, inventory = None):
        super().__init__(name, maxhp, currenthp, defense, maxsp, cursp, personas)
        self.inventory = inventory if inventory is not None else []

    def player_turn(self, enemies, persona):
        # PLAYER TURN
        turn_ = True
        print(f"\n--- {self.name}'s Turn ---")
        while turn_:
            print(f"Current Persona: {persona.name}")
            print("Choose an action:")
            print("1. Basic Attack")
            print("2. Use Skill")
            print("3. Guard")

            choice = input("Enter choice (1-3): ")

            if choice == "1":
                # basic attack logic
                damage = 25  # placeholder for base attack calculation
                target = target_selector(enemies)
                if target:
                    target.curhp -= damage
                    print(f"{self.name} attacks {target.name} for {damage} physical damage!")
                    turn_ = False
                elif not target:  # if the player wants to back out and go back to the action menu
                    pass

            elif choice == "2":
                # skill logic
                while True:
                    for index, skill in enumerate(persona.skills):
                        print(f"{index + 1} - {skill.name}")
                    print(f"{len(persona.skills) + 1} - Back")
                    try:
                        selection = int(input("Please select a skill\n"))
                    except ValueError:
                        print("Please enter a valid input!")
                        continue
                    else:
                        if 1 <= selection <= len(persona.skills):
                            skill_to_use = persona.skills[selection - 1]
                            if self.use_skill(skill_to_use):
                                target = target_selector(enemies)
                                if target is None:
                                    break
                                else:
                                    self.cursp -= skill_to_use.cost
                                    target.curhp -= skill_to_use.effect
                                    print(
                                        f"{self.name} casts {skill_to_use.name} on {target.name} for {skill_to_use.cost} SP!")
                                    print(f"It deals {skill_to_use.effect} {skill_to_use.element} damage!")
                                    turn_ = False
                                    break
                            else:
                                print("Not enough SP!")
                        elif selection == (len(persona.skills) + 1):
                            break
                        else:
                            print("Please enter a valid input!")

            elif choice == "3":
                print(f"{self.name} takes a defensive stance! (Guard active)")
                turn_ = False
                # add guard logic here (e.g., temporary defense boost and calculation)

            else:
                print("Please enter a valid input!")

class NPC(Character):
    def __init__(self, name, maxhp, currenthp, defense, maxsp, cursp, classification, personas = None):
        super().__init__(name, maxhp, currenthp, defense, maxsp, cursp, personas)
        self.classification = classification

    def npc_turn(self, persona, targets):
        print(f"\n--- {self.name}'s Turn ---")
        print(f"Current Persona: {persona.name}")
        skill_to_use = random.choice(persona.skills)  # /////////add an algorithm for this
        if self.use_skill(skill_to_use):
            target = npc_target_selector(targets)
            self.cursp -= skill_to_use.cost
            target.curhp -= skill_to_use.effect
            print(f"{self.name} casts {skill_to_use.name} on {target.name} for {skill_to_use.cost} SP!")
            print(f"It deals {skill_to_use.effect} {skill_to_use.element} damage!")

        else:
            print("Not enough SP! Turn wasted.")

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

    def get_agility(self):
        return self.agility

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
Penthesilea = Persona("Penthesilea",[Bufu],{"Fire": "weak", "Ice": "resist"},13, 17, 11, 15, 11)


