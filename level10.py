from classes import NPC, Persona, PhysicalAttack, ElementalAttack, Cerberus, Penthesilea, Player, medicine
from battle import battle_loop


# SKILLS
myriad_arrows = PhysicalAttack("Pierce", "Myriad Arrows", 0.19, 80, 4, 0.88, 0.05)
primal_force = PhysicalAttack("Pierce", "Primal Force", 0.21, 580, 1, 0.95, 0.05)
maralagidyne = ElementalAttack("Fire", "Maralagidyne", 32, 220, 4, 0.9)
# Spirit Drain is TBD until support skills are implemented
heat_wave = PhysicalAttack("Strike", "Heat Wave", 0.20, 280, 4, 0.9, 0.1)


# PERSONA
Mara = Persona("Mara", [myriad_arrows, primal_force, maralagidyne, heat_wave], {"Strike": "absorb", "Fire": "absorb", "Ice": "weak", "Light": "weak", "Dark": "absorb"}, 60, 50, 50, 48, 39)


# ENEMY
Hastur = NPC("Hastur", 1500, 1500, 1, 50, 500, 500, "Enemy", [Mara], status_effect=None)


# LEVEL 10
def level_10(MainCharacter):
    print("""
    ==================================================
                 LEVEL 10: THE HOUR OF JUDGMENT
    ==================================================

    *The descent culminates at the core of Tartarus.*

    *Here, SEES faces the avatar of Death itself.
    The fate of humanity hangs in the balance.*

    Makoto: "So this is where it ends..."

    *Before you stands the source of the darkness
    threatening to consume the city.*

    Makoto: "We won't let you take away our tomorrow.
    Everyone, get ready!"

    ==================================================
    """)

    input("\n[Press Enter to face the final enemy...]")

    # Restore the main character
    MainCharacter.curhp = MainCharacter.maxhp
    MainCharacter.cursp = MainCharacter.maxsp

    # Reset the final enemy
    Hastur.curhp = Hastur.maxhp
    Hastur.cursp = Hastur.maxsp

    combatants = [MainCharacter, Hastur]

    status = battle_loop(combatants)

    if status == "Win":
        print("""
        *The avatar of Death has fallen.*

        *The core of Tartarus grows silent.
        For the first time, tomorrow feels possible.*

        LEVEL 10 CLEARED!
        """)
        return True

    elif status == "Lose":
        print("GAME OVER")
        return False

    else:
        return False

if __name__ == "__main__":
    level_10()