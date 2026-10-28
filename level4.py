
from classes import Character, Player, Skill, Izanagi, NPC
from classes import Persona, PhysicalAttack, ElementalAttack
from battle import battle_loop


# SKILLS
Strike_Attack = PhysicalAttack("Strike", "Strike Attack", 0, 40, 1, 0.95, 0.05)
Magaru = ElementalAttack("Wind", "Magaru", 8, 40, 4, 0.99)
Slash_Attack = PhysicalAttack("Slash", "Slash Attack", 0, 40, 1, 0.95, 0.05)
Power_Slash = PhysicalAttack("Slash", "Power Slash", 0.1, 80, 1, 0.9, 0.10)
Agidyne = ElementalAttack("Fire", "Agidyne", 14, 220, 1, 0.99)
Deathbound = PhysicalAttack("Slash", "Deathbound", 0.25, 130, 4, 0.9, 0.05)


# PERSONAS
Venus_Eagle = Persona("Venus Eagle", [Slash_Attack, Power_Slash], {"Slash": "resist", "Electric": "weak"}, 12, 18, 10, 24, 12)
Venus_Eagle.arcana = "Lovers"

Swift_Axle = Persona("Swift Axle", [Strike_Attack, Magaru], {"Electric": "weak", "Slash": "resist", "Strike": "resist"}, 22, 8, 16, 20, 8)
Swift_Axle.arcana = "Chariot"

Surt = Persona("Surt", [Agidyne, Deathbound], {"Pierce": "null", "Ice": "weak"}, 22, 28, 18, 14, 16)
Surt.arcana = "Emperor"


# COMBATANTS
MakotoYuki = NPC(name="Makoto Yuki", maxhp=150, currenthp=150, defense=20, agility=30, maxsp=100, cursp=100, classification="Ally", personas=[Izanagi])

WildDrive = NPC(name="Wild Drive", maxhp=200, currenthp=200, defense=15, agility=30, maxsp=60, cursp=60, classification="Enemy", personas=[Swift_Axle])

TranceTwins = NPC(name="Trance Twins", maxhp=150, currenthp=150, defense=10, agility=30, maxsp=80, cursp=80, classification="Enemy", personas=[Venus_Eagle])

FatalTurret = NPC(name="Fatal Turret", maxhp=250, currenthp=250, defense=20, agility=30, maxsp=120, cursp=120, classification="Enemy", personas=[Surt])


# LEVEL 4
def level_4(MainCharacter):
    print("""
    ==================================================
                       LEVEL 4
                  CORRIDORS OF DOUBT
    ==================================================

    *The corridor stretches on, the walls whispering
    as you pass.*

    Makoto: "Keep your guard up. Something feels wrong here."

    *Three Shadows step out of the dark, blocking the path.*

    Makoto: "Three of them... Stay close. I've got your back."
    """)

    input("\n[Press Enter to continue...]")

    print("""
    *Makoto draws his Evoker and steadies his breath.*

    Makoto: "We don't stop now. Not this close."

    ==================================================
          ALLY FIGHTS BESIDE YOU: MAKOTO YUKI
                 MISSION: CLEAR LEVEL 4
    ==================================================
    """)

    input("\n[Press Enter to begin the battle...]")

    # Restore the main character
    MainCharacter.curhp = MainCharacter.maxhp
    MainCharacter.cursp = MainCharacter.maxsp

    # Reset combatants for a fresh battle
    MakotoYuki.curhp = MakotoYuki.maxhp
    MakotoYuki.cursp = MakotoYuki.maxsp

    WildDrive.curhp = WildDrive.maxhp
    WildDrive.cursp = WildDrive.maxsp

    TranceTwins.curhp = TranceTwins.maxhp
    TranceTwins.cursp = TranceTwins.maxsp

    FatalTurret.curhp = FatalTurret.maxhp
    FatalTurret.cursp = FatalTurret.maxsp

    combatants = [MainCharacter, WildDrive, TranceTwins, FatalTurret]

    status = battle_loop(combatants)

    if status == "Win":
        print("LEVEL 4 CLEARED! The corridor is finally quiet.")
        return True

    elif status == "Lose":
        print("GAME OVER. The Shadows overwhelmed the party.")
        return False
    else:
        return False


if __name__ == "__main__":
    level_4()
