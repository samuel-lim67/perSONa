from classes import Character, Player, Skill, Arsene, Izanagi, NPC, Penthesilea
from classes import Persona, PhysicalAttack, ElementalAttack, Assault_Dive, Zio
from battle import battle_loop

# ---------- NEW SKILLS (level 5) ----------
# PhysicalAttack(element, name, cost, effect, targets, accuracy, criticalchance)
# ElementalAttack(element, name, cost, effect, targets, accuracy, sideeffecttype, sideeffectchance)

Fatal_End = PhysicalAttack("Slash", "Fatal End", 0.10, 80, 1, 0.95, 0.05)
Blade_of_Fury = PhysicalAttack("Slash", "Blade of Fury", 0.17, 40, 4, 0.90, 0.05)
Heat_Wave = PhysicalAttack("Strike", "Heat Wave", 0.20, 110, 4, 0.90, 0.05)
Swift_Strike = PhysicalAttack("Strike", "Swift Strike", 0.12, 50, 4, 0.90, 0.05)
Bufula = ElementalAttack("Ice", "Bufula", 8, 100, 1, 0.99, "Freeze", 0.10)
Mabufula = ElementalAttack("Ice", "Mabufula", 14, 80, 4, 0.99, "Freeze", 0.08)

# ---------- NEW PERSONAS (level 5) ----------
# Persona(name, skills, affinity, strength, magic, endurance, agility, luck)
Castor = Persona("Castor", [Fatal_End, Blade_of_Fury, Heat_Wave],
                 {"Strike": "resist"},
                 30, 14, 24, 18, 14)
Castor.arcana = "Hierophant"

Zouchouten = Persona("Zouchouten", [Assault_Dive, Zio, Swift_Strike],
                     {"Slash": "resist", "Wind": "weak"},
                     14, 7, 13, 6, 10)
Zouchouten.arcana = "Chariot"

King_Frost = Persona("King Frost", [Bufula, Mabufula],
                     {"Slash": "null", "Pierce": "null", "Ice": "null"},
                     18, 31, 26, 14, 20)
King_Frost.arcana = "Emperor"

def start_lvl5(MainCharacter):
    print("\n=== LEVEL 5 ===")
    print("\nThe Midpoint Bazaar & The Iron Warden")
    print("\n=========================================")
    print("\n The final shadow awaits... ")
    print("You and your allies stand together against a powerful boss!")
    print("MISSION: CLEAR LEVEL 5")
    print("=========================================\n")

def create_level5_combatants(MainCharacter):
    start_lvl5(MainCharacter)
    MainCharacter.curhp = MainCharacter.maxhp
    MainCharacter.cursp = MainCharacter.maxsp

    makoto_yuki = NPC(
        #ally1
        name="Makoto Yuki",
        maxhp=150,
        currenthp=150,
        defense=20,
        maxsp=100,
        cursp=100,
        classification="Ally",
        personas=[Izanagi, Arsene])

    yukari_takeba = NPC(
        #ally2
        name="Yukari Takeba",
        maxhp=150,
        currenthp=150,
        defense=15,
        maxsp=100,
        cursp=100,
        classification="Ally",
        personas=[Arsene, Penthesilea])

    calm_basalt = NPC(
        #enemy1 (Hierophant) -> Castor persona
        name="Calm Basalt",
        maxhp=200,
        currenthp=200,
        defense=15,
        maxsp=80,
        cursp=80,
        classification="Enemy",
        personas=[Castor])

    raging_facade = NPC(
        #enemy2 (Chariot) -> Zouchouten persona
        name="Raging Facade",
        maxhp=200,
        currenthp=200,
        defense=20,
        maxsp=80,
        cursp=80,
        classification="Enemy",
        personas=[Zouchouten])

    intrepid_knight = NPC(
        #BOSS (Emperor) -> King Frost persona
        name="Intrepid Knight",
        maxhp=450,
        currenthp=450,
        defense=25,
        maxsp=150,
        cursp=150,
        classification="Enemy",
        personas=[King_Frost])

    # 3 vs 3
    combatants = [MainCharacter, makoto_yuki, yukari_takeba, calm_basalt, raging_facade, intrepid_knight]
    battle_loop(combatants)