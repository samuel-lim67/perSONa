from classes import Character, Persona, Player, Skill, NPC, ElementalAttack, PhysicalAttack
from battle import battle_loop

# SKILLS
Cleave = PhysicalAttack("Slash", "Cleave", 0.07, 30, 1, 0.9, 0.1)
Agi = ElementalAttack("Fire", "Agi", 3, 40, 1, 0.99)
Bufu = ElementalAttack("Ice", "Bufu", 4, 40, 1, 0.99, "Freeze", 0.15)

# PERSONAS
Shadow_Core = Persona(name="Shadow Core",skills=[Cleave],affinity={},strength=6,magic=6,endurance=6,agility=6,luck=6)

# ENEMIES
Brave_Hand = NPC(name="Brave Hand", maxhp=60, currenthp=60, defense=3, agility=6, maxsp=20, cursp=20, classification="Enemy", personas=[Shadow_Core])


# LEVEL 1
def level_1(MainCharacter):
    print("""
    ==========================================
              LEVEL 1: THE AWAKENING GATE
    ==========================================

    Story: Makoto awakens his initial power just
    as Shadows breach the dormitory threshold.
    """)

    input("\n[Press Enter to begin the battle...]")

    # Reset HP and SP
    MainCharacter.curhp = MainCharacter.maxhp
    MainCharacter.cursp = MainCharacter.maxsp

    Brave_Hand.curhp = Brave_Hand.maxhp
    Brave_Hand.cursp = Brave_Hand.maxsp

    combatants = [MainCharacter, Brave_Hand]

    status = battle_loop(combatants)

    if status == "Win":
        print("""
        [LEVEL 1 COMPLETE]
        The dormitory breach is secured.
        """)
        return True

    elif status == "Lose":
        print("""
        [LEVEL 1 FAILED]
        The Shadows overwhelmed the dormitory...
        """)
        return False
    else:
        return False


if __name__ == "__main__":
    level_1()
