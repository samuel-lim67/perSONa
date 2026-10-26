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
    def __init__(self, name, maxhp, currenthp, defense, agility, maxsp, cursp, personas = None, status_effect = None):
        self.name = name
        self.maxhp = maxhp
        self.curhp = currenthp
        self.defense = defense
        self.maxsp = maxsp
        self.cursp = cursp
        self.agility = agility
        self.personas = personas if personas is not None else []
        self.status_effect = status_effect

        self.knocked_down = False

    def use_skill(self, skill):
        cost = skill.cost
        if self.cursp < cost:
            return False
        else:
            return True

    def battle_damage_display(self, skill_to_use, target_persona, enemy, damage, effectiveness):
        if isinstance(skill_to_use, PhysicalAttack):
            damage = critical_hit(skill_to_use, enemy, damage)
            print(f"{self.name} casts {skill_to_use.name} on {enemy.name}'s {target_persona.name} for {round((skill_to_use.cost*self.maxhp), 1)} HP!")
        elif isinstance(skill_to_use, ElementalAttack):
            side_effect(skill_to_use, enemy)
            print(f"{self.name} casts {skill_to_use.name} on {enemy.name}'s {target_persona.name} for {skill_to_use.cost} SP!")
        enemy.curhp -= damage
        print(f"{effectiveness} It deals {damage} {skill_to_use.element} damage!")

    def accuracy_check(self, skill_to_use, enemy):
        rate_calculation = (skill_to_use.accuracy * (self.agility / enemy.agility))
        chance = random.random()
        if chance <= rate_calculation:
            return True
        else:
            return False

    def cost_calculator(self, skill_to_use):
        if isinstance(skill_to_use, PhysicalAttack):
            self.curhp -= (skill_to_use.cost * self.maxhp)
            print(f"{round((skill_to_use.cost * self.maxhp), 1)} HP was consumed.")
        elif isinstance(skill_to_use, ElementalAttack):
            self.cursp -= skill_to_use.cost
            print(f"{skill_to_use.cost} SP was consumed.")

class Player(Character):
    def __init__(self, name, maxhp, currenthp, defense, agility, maxsp, cursp, personas = None, status_effect = None, inventory = None):
        super().__init__(name, maxhp, currenthp, defense, agility, maxsp, cursp, personas, status_effect)
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
                if target is None:
                    continue
                else:
                    target_persona, enemy = target
                    enemy.curhp -= damage
                    print(f"{self.name} used a basic attack on {enemy.name} for 25 damage!")


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
                                if skill_to_use.targets < 4:
                                    for _ in range(skill_to_use.targets):
                                        target = target_selector(enemies)
                                        if target is None:
                                            break
                                        else:
                                            target_persona, enemy = target
                                            if self.accuracy_check(skill_to_use, enemy):
                                                damage, effectiveness = calculate_damage(skill_to_use, persona, target_persona,enemy)
                                                self.battle_damage_display(skill_to_use, target_persona, enemy, damage, effectiveness)
                                                extra_turn = check_effectiveness(effectiveness, enemy)
                                                if extra_turn:
                                                    turn_ = True
                                                else:
                                                    turn_ = False
                                            else:
                                                print(f"{skill_to_use.name} missed!")
                                                turn_ = False
                                    break
                                else:
                                    for enemy in enemies:
                                        if enemy.curhp <= 0:
                                            continue

                                        for target_persona in enemy.personas:
                                            if self.accuracy_check(skill_to_use, enemy):
                                                damage, effectiveness = calculate_damage(skill_to_use, persona, target_persona,enemy)
                                                self.battle_damage_display(skill_to_use, target_persona, enemy, damage, effectiveness)
                                                extra_turn = check_effectiveness(effectiveness, enemy)
                                                if extra_turn:
                                                    turn_ = True
                                                else:
                                                    turn_ = False
                                            else:
                                                print(f"{skill_to_use.name} missed!")
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

    def character_selector(self, choices):
        while True:
            print("Please Select Your Starting Persona")
            for index, persona in enumerate(choices):
                print(f"{index + 1}. {persona.name}")
            try:
                selection = int(input())
            except ValueError:
                print("Please enter a valid input!")
                continue
            else:
                if selection <= 0:
                    print("Please enter a valid input!")
                    continue
                else:
                    confirm = str(input((f"Are you sure you want to select {choices[selection - 1].name}? Y/N\n")))
                    if confirm.lower().strip() == "y":
                        self.personas.append(choices[selection - 1])
                        print(f"Successfully selected {choices[selection - 1].name}")
                        return
                    else:
                        print("Please enter a valid input!")
                        continue

    def switch_slots(self):
        print("========YOUR PERSONAS========")
        while True:
            for index, persona in enumerate(self.personas):
                print(f"{index+1} - {persona.name}")

            print(f"{len(self.personas) + 1} - Back")
            try:
                selection_original = int(input("Who would you like to switch?"))
            except ValueError:
                print("Please enter a valid input!")
                continue
            else:
                if 1 <= selection_original <= len(self.personas):
                    selected_persona = self.personas[selection_original - 1]
                    other_personas = [persona for persona in self.personas if persona != selected_persona]
                    for index, persona in enumerate(other_personas):
                        print(f"{index + 1} - {persona.name}")

                    print(f"{len(other_personas) + 1} - Back")
                    try:
                        selection_new = int(input(f"Who would you like to switch {selected_persona.name} with?"))
                    except ValueError:
                        print("Please enter a valid input!")
                        continue
                    else:
                        if 1 <= selection_new <= len(other_personas):
                            original_index = self.personas.index(selected_persona)
                            new_index = self.personas.index(other_personas[selection_new-1])
                            self.personas[original_index], self.personas[new_index] = self.personas[new_index], self.personas[original_index]
                            print(f"Swapped {selected_persona.name} with {other_personas[selection_new - 1].name}!")
                            return
                        elif selection_new == (len(other_personas) + 1):
                            return
                        else:
                            print("Please select a valid input!")

                elif selection_original == (len(self.personas)+1):
                    return
                else:
                    print("Please select a valid input!")


class NPC(Character):
    def __init__(self, name, maxhp, currenthp, defense, agility, maxsp, cursp, classification, personas = None, status_effect = None):
        super().__init__(name, maxhp, currenthp, defense, agility, maxsp, cursp, personas, status_effect)
        self.classification = classification

    def npc_turn(self, persona, targets):
        turn_ = True
        while turn_:
            print(f"\n--- {self.name}'s Turn ---")
            print(f"Current Persona: {persona.name}")
            skill_to_use = random.choice(persona.skills)  # /////////add an algorithm for this
            if self.use_skill(skill_to_use):
                self.cost_calculator(skill_to_use)
                if skill_to_use.targets < 4:
                    for _ in range(skill_to_use.targets):
                        target_persona, enemy = npc_target_selector(targets)
                        if self.accuracy_check(skill_to_use, enemy):
                            damage, effectiveness = calculate_damage(skill_to_use, persona, target_persona, enemy)
                            self.battle_damage_display(skill_to_use, target_persona, enemy, damage, effectiveness)
                            extra_turn = check_effectiveness(effectiveness, enemy)
                            if extra_turn:
                                turn_ = True
                            else:
                                turn_ = False
                        else:
                            print(f"{skill_to_use.name} missed!")
                            turn_ = False
                else:
                    for target in targets:
                        if target.curhp <= 0:
                            continue

                        for target_persona in target.personas:
                            if self.accuracy_check(skill_to_use, target):
                                damage, effectiveness = calculate_damage(skill_to_use, persona, target_persona, target)
                                self.battle_damage_display(skill_to_use, target_persona, target, damage, effectiveness)
                                extra_turn = check_effectiveness(effectiveness, target)
                                if extra_turn:
                                    turn_ = True
                                else:
                                    turn_ = False
                            else:
                                print(f"{skill_to_use.name} missed!")
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
Arsene = Persona("Arsene", [Eiha, Bash, Cross_Slash], {"Ice": "weak","Light": "weak", "Dark": "resist"}, 2, 2, 2, 3, 1)
Izanagi = Persona("Izanagi", [Zio, Cross_Slash], {"Electric": "resist", "Wind": "weak", "Dark": "null"}, 3, 2, 2, 3, 2)

Cerberus = Persona("Cerberus",[Agi, Eiha, Megido],{"Ice": "weak", "Light": "null", "Dark": "resist"},25, 24, 21, 29, 19)
Penthesilea = Persona("Penthesilea",[Bufu, Bash, Cross_Slash],{"Fire": "weak", "Ice": "resist"},13, 17, 11, 15, 11)


#FINAL BOSS IS MARA
#charge
#primal force
#spirit drain