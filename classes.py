import random
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

    return round(damage), effectivness

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

class Skill:
    def __init__(self, element, name, cost, effect, targets, accuracy, sideeffecttype = None, sideeffectchance = None):
        self.element = element
        self.name = name
        self.cost = cost
        self.effect = effect
        self.targets = targets
        self.accuracy = accuracy

class PhysicalAttack(Skill):
    def __init__(self, element, name, cost, effect, targets, accuracy, criticalchance):
        super().__init__(element, name, cost, effect, targets, accuracy)
        self.criticalchance = criticalchance

class ElementalAttack(Skill):
    def __init__(self, element, name, cost, effect, targets, accuracy, sideeffecttype = None, sideeffectchance = None):
        super().__init__(element, name, cost, effect, targets, accuracy)
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

        self.knocked_down = False

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
            print("4. View Inventory")

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
                                target_persona, enemy = target_selector(enemies)
                                if target_persona is None:
                                    break
                                else:
                                    if isinstance(skill_to_use, PhysicalAttack):
                                        damage, effectiveness = calculate_damage(skill_to_use, persona, target_persona, enemy)
                                    elif isinstance(skill_to_use, ElementalAttack):
                                        damage, effectiveness = calculate_damage(skill_to_use, persona, target_persona, enemy)
                                        self.cursp -= skill_to_use.cost
                                        enemy.curhp -= damage

                                    print(f"{self.name} casts {skill_to_use.name} on {enemy.name}'s {target_persona.name} for {skill_to_use.cost} SP!")
                                    print(f"{effectiveness} It deals {damage} {skill_to_use.element} damage!")
                                    extra_turn = check_effectiveness(effectiveness, enemy)
                                    if not extra_turn:
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

            elif choice == "4":
                #view inventory
                if not self.inventory:
                    print("\nYour inventory is empty")
                    input("Press any button to return")
                    return
                else:
                    print("----Inventory----")
                    for index, item in enumerate(self.inventory):
                        print(f'{index}. {item.name} x{item.quantity}')


            else:
                print("Please enter a valid input!")

class NPC(Character):
    def __init__(self, name, maxhp, currenthp, defense, maxsp, cursp, classification, personas = None):
        super().__init__(name, maxhp, currenthp, defense, maxsp, cursp, personas)
        self.classification = classification

    def npc_turn(self, persona, targets):
        turn_ = True
        while turn_:
            print(f"\n--- {self.name}'s Turn ---")
            print(f"Current Persona: {persona.name}")
            skill_to_use = random.choice(persona.skills)  # /////////add an algorithm for this
            if self.use_skill(skill_to_use):
                target_persona, enemy = npc_target_selector(targets)
                if isinstance(skill_to_use, PhysicalAttack):
                    damage, effectiveness = calculate_damage(skill_to_use, persona, target_persona, enemy)
                elif isinstance(skill_to_use, ElementalAttack):
                    damage, effectiveness = calculate_damage(skill_to_use, persona, target_persona, enemy)
                    self.cursp -= skill_to_use.cost
                    enemy.curhp -= damage

                print(f"{self.name} casts {skill_to_use.name} on {enemy.name}'s {target_persona.name} for {skill_to_use.cost} SP!")
                print(f"{effectiveness} It deals {damage} {skill_to_use.element} damage!")
                extra_turn = check_effectiveness(effectiveness, enemy)
                if not extra_turn:
                    turn_ = False

            else:
                print("Not enough SP!")

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

class Item:
    def __init__(self, name, quantity, stat_type , effect, duration,price):
        self.name = name
        self.quantity = quantity
        self.type = stat_type
        self.effect = effect
        self.duration = duration
        self.price = price

shop_items = {"Medicine": Item("Medicine",1,"health",50,0,30),
              "SP Bead": Item("SP Bead",1,"sp",50,0,25),
              "Guard Charm": Item("Guard Charm",1,"defense",50,2,35)}

def add_item(player,item):
    for owned_item in player.inventory:
        if owned_item == item.name:
            owned_item.quantity += item.quantity
            return
            
    player.inventory.append(item)


#PHYSICAL
Assault_Dive = PhysicalAttack("Strike", "Assault Dive", 0.12, 120, 1, 0.88, 0.13)
Cross_Slash = PhysicalAttack("Slash", "Cross Slash", 0.18, 150, 1, 0.99, 0.13)
Bash = PhysicalAttack("Strike", "Bash", 0.07, 50, 1, 0.9, 0.08)

#FIRE
Agi = ElementalAttack("Fire", "Agi", 3, 40, 1, 0.99)
#ICE
Bufu = ElementalAttack("Ice", "Bufu", 4, 40, 1, 0.99, "Freeze", 0.15)
#ELECTRIC
Zio = ElementalAttack("Electric", "Zio", 4, 40, 2, 0.99, "Shock", 0.15)
Ziodyne = ElementalAttack("Electric", "Ziodyne", 14, 220, 1, 0.99, "Shock", 0.15)
#WIND
Garu = ElementalAttack("Wind", "Garu", 3, 40, 1, 0.99)
#LIGHT
Kouha = ElementalAttack("Light", "Kouha", 4, 60, 1, 0.99)
#DARK
Eiha = ElementalAttack("Dark", "Eiha", 4, 60, 1, 0.99)
#Eiga = ElementalAttack("Dark", )
#ALMIGHTY
Megido = ElementalAttack("Almighty", "Megido", 20, 170, 4, 0.99)
#SUPPORT
Dia = Skill("Healing", "Dia", 3, 50, 1, 1)
Marakukaja = Skill("Support", "Marakukaja", 24, 0.4, 1, 1)
#Tarunda

Orpheus = Persona("Orpheus", [Agi, Bufu], {"Fire": "resist", "Electric": "weak", "Dark": "weak"}, 2, 2, 2, 3, 2)
Arsene = Persona("Arsene", [Eiha], {"Ice": "weak","Light": "weak", "Dark": "resist"}, 2, 2, 2, 3, 1)
Izanagi = Persona("Izanagi", [Zio, Cross_Slash, ], {"Electric": "resist", "Wind": "weak", "Dark": "null"}, 3, 2, 2, 3, 2)

Cerberus = Persona("Cerberus",[Agi, Eiha, Megido],{"Ice": "weak", "Light": "null", "Dark": "resist"},25, 24, 21, 29, 19)
Penthesilea = Persona("Penthesilea",[Bufu],{"Fire": "weak", "Ice": "resist"},13, 17, 11, 15, 11)


#FINAL BOSS IS MARA
#charge
#primal force
#spirit drain