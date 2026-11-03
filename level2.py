from classes import Persona, NPC, ElementalAttack, PhysicalAttack
from battle import battle_loop


# SKILLS
Agi = ElementalAttack("Fire", "Agi", 4, 15, 1, 95, "Burn", 0.10)
Maragi = ElementalAttack("Fire", "Maragi", 8, 10, 2, 90, "Burn", 0.05)
Rakunda = PhysicalAttack("Support", "Rakunda", 0.12, 20, 1, 100, 0.05)

Psio = ElementalAttack("Psy", "Psio", 10, 40, 1, 95, "Brainwash", 0.10)
Assault_Dive = PhysicalAttack("Strike", "Assault Dive", 0.12, 55, 1, 85, 0.12)
Marakukaja = ElementalAttack("Support", "Marakukaja", 12, 20, 2, 100)


# PERSONAS
Pyro_Jack = Persona("Pyro Jack",[Agi, Maragi, Rakunda],{"Fire": "resist", "Ice": "weak"},14, 18, 15, 21, 14)

Hierophant = Persona("Hierophant",[Psio, Assault_Dive, Marakukaja],{"Fire": "resist", "Ice": "weak"},15, 28, 18, 22, 12)


# ENEMIES
Crying_Tablet = NPC(name="Crying Tablet",maxhp=50,currenthp=50,defense=20,agility=30,maxsp=100,cursp=100,classification="Enemy",personas=[Pyro_Jack])

Phantom_Mage = NPC(name="Phantom Mage",maxhp=50,currenthp=50,defense=15,agility=30,maxsp=80,cursp=80,classification="Enemy",personas=[Hierophant])


# LEVEL 2
def level_2(MainCharacter):
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
    MainCharacter.status_effect = None

    Crying_Tablet.curhp = Crying_Tablet.maxhp
    Crying_Tablet.cursp = Crying_Tablet.maxsp
    Crying_Tablet.status_effect = None

    Phantom_Mage.curhp = Phantom_Mage.maxhp
    Phantom_Mage.cursp = Phantom_Mage.maxsp
    Phantom_Mage.status_effect = None

    combatants = [MainCharacter, Crying_Tablet, Phantom_Mage]

    status = battle_loop(combatants)

    if status == "Win":
        print("Level 2 cleared!")
        return True
    elif status == "Lose":
        print("GAME OVER")
        return False
    else:
        return False


if __name__ == "__main__":
    level_2()