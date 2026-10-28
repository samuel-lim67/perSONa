from classes import Character, Player, Skill, Orpheus, Arsene, Izanagi, Cerberus, NPC, Penthesilea, Persona, \
    ElementalAttack, PhysicalAttack
from battle import battle_loop



def start_lvl2(MainCharacter):
    print("""
    ==================================================
                        LEVEL 2
                      SPLIT PATHS
    ==================================================

    *Makoto reaches a deserted street, its buildings
    warped by the strange distortion.*

    Makoto: "This place... it's getting worse."

    *Two Shadows emerge, blocking his path.*

    Makoto: "Fine. I'll deal with you first."

    ==================================================
    """)

    input("\n[Press Enter to continue...]")

    print("""
    *As the Shadows close in, Makoto senses
    a strange power waiting to be awakened.*

    Makoto: "I can't stop here. I need to get stronger."

    ==================================================
                 MISSION: CLEAR LEVEL 2
    ==================================================
    """)

    input("\n[Press Enter to begin the battle...]")
    MainCharacter.curhp = MainCharacter.maxhp
    MainCharacter.cursp = MainCharacter.maxsp


def create_level2_combatants(MainCharacter):
    start_lvl2(MainCharacter)
    Agi = ElementalAttack("Fire", "Agi", 4, 15, 1, 95, "Burn", 0.10)

    Maragi = ElementalAttack("Fire", "Maragi", 8, 10, 4, 90, "Burn", 0.05)

    Rakunda = PhysicalAttack("Support", "Rakunda", 8, 20, 1, 100, 0.05)

    Psio = ElementalAttack("Psy", "Psio", 10, 40, 1, 95)
    Assault_Dive = PhysicalAttack("Strike", "Assault Dive", 12, 55, 1, 85, 0.12)
    Marakukaja = ElementalAttack("Support", "Marakukaja", 12, 20,  4, 100, 0.10)

    Pyro_Jack = Persona("Pyro Jack", [Agi, Maragi, Rakunda], {"Fire": "resist", "Ice": "weak"}, 14, 18, 15, 21, 14)
    Hierophant = Persona("Hierophant", [Psio, Assault_Dive, Marakukaja], {"Fire": "resist", "Ice": "weak"}, 15, 28, 18,
                         22, 12)

    Crying_Tablet = NPC(
        # enemy1
        name="Crying Tablet",
        maxhp=50,
        currenthp=50,
        defense=20,
        agility=30,
        maxsp=100,
        cursp=100,
        classification="Enemy",
        personas=[Pyro_Jack])

    Phantom_Mage = NPC(
        # enemy2
        name="Phantom Mage",
        maxhp=50,
        currenthp=50,
        defense=15,
        agility=30,
        maxsp=80,
        cursp=80,
        classification="Enemy",
        personas=[Hierophant])

    combatants = [MainCharacter, Crying_Tablet, Phantom_Mage]
    battle_loop(combatants)
