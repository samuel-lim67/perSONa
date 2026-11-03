from classes import NPC, Persona, PhysicalAttack, ElementalAttack, Cerberus, Penthesilea, Player, medicine
from battle import battle_loop


# SKILLS
myriad_arrows = PhysicalAttack("Pierce", "Myriad Arrows", 0.19, 40, 4, 0.88, 0.05)
primal_force = PhysicalAttack("Pierce", "Primal Force", 0.21, 40, 1, 0.95, 0.05)
maralagidyne = ElementalAttack("Fire", "Maralagidyne", 32, 40, 4, 0.9)
# Spirit Drain is TBD until support skills are implemented
heat_wave = PhysicalAttack("Strike", "Heat Wave", 0.20, 40, 4, 0.9, 0.1)


# PERSONA
Mara = Persona("Mara", [myriad_arrows, primal_force, maralagidyne, heat_wave], {"Strike": "absorb", "Fire": "absorb", "Ice": "weak", "Light": "weak", "Dark": "absorb"}, 60, 50, 50, 15, 39)


# ENEMY
Hastur = NPC("Hastur", 3000, 3000, 20, 15, 500, 500, "Enemy", [Mara], status_effect=None)


# LEVEL 10
def level_10(MainCharacter):
    print("""
       ==================================================
                       LEVEL 10
                    THE HOUR OF JUDGMENT
       ==================================================


       *The reunited SEES finally meet their journey’s end. What stands in front of them is the accumulation of humanities dread and fears. The fate of the world sits in your hands, do not fail us now.*


       Yukari: "Wait… No way, that thing is massive!"


       Junpei: "Talk about overcompensating! What kind of nightmare spawn is that?!."


       Akihiko: “...Don’t let its appearance fool you. That mass of energy is radiating enough power
                 to level a city block. Stay Sharp!!!”


       Makoto: "You… So it’s you that caused all of this!."


       *Mara, The Great King, towers over the battlefield, casting an overwhelming shadow across all of SEES! Do you have what it takes? Will you step on up to battle?*
       """)

    input("\n[Press Enter to continue...]")

    print("""
       *Good. Prove it…”
       """)

    # Restore the main character
    MainCharacter.curhp = MainCharacter.maxhp
    MainCharacter.cursp = MainCharacter.maxsp
    MainCharacter.status_effect = None

    # Reset the final enemy
    Hastur.curhp = Hastur.maxhp
    Hastur.cursp = Hastur.maxsp
    Hastur.status_effect = None

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