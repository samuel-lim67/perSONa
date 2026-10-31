from classes import Persona, NPC, ElementalAttack, PhysicalAttack, Orpheus, Arsene, Izanagi, Cerberus, Penthesilea
from battle import battle_loop

# SKILLS
Megido = ElementalAttack("Almighty", "Megido", 20, 170, 4, 0.99)
Maragidyne = ElementalAttack("Fire", "Maragidyne", 22, 160, 4, 0.95, "Burn", 0.10)

Brave_Blade = PhysicalAttack("Slash", "Brave Blade", 0.24, 210, 1, 0.90, 0.12)
Myriad_Arrows = PhysicalAttack("Pierce", "Myriad Arrows", 0.19, 80, 4, 0.88, 0.05)


# PERSONAS
Basalt_Statue_Persona = Persona("Daisoujou", [Megido, Maragidyne], {"Phys": "resist", "Fire": "null", "Curse": "weak"}, 18, 26, 28, 12, 14)

Judgment_Sword_Persona = Persona("Melchizedek", [Brave_Blade, Myriad_Arrows], {"Phys": "resist", "Wind": "weak"}, 28, 12, 16, 26, 18)


# ENEMIES
Basalt_Statue = NPC(name="Basalt Statue", maxhp=150, currenthp=150, defense=25, agility=20, maxsp=200, cursp=200, classification="Enemy", personas=[Basalt_Statue_Persona])
Judgment_Sword = NPC(name="Judgment Sword", maxhp=150, currenthp=150, defense=18, agility=30, maxsp=150, cursp=150, classification="Enemy", personas=[Judgment_Sword_Persona])


# LEVEL 8
def level_8(MainCharacter):
    print("""
    ==================================================
                        LEVEL 8
                  TWO ELITE ENEMIES
    ==================================================


    *Psychological pressure, self-doubt, and the insurmountable strength of the dual-persona Elite Shadows before you.*


    Yukari: "These two… they feel different than the other shadows again, watch out."


    Junpei: "Tsc, psychological warfare? Imma show them physical warfare! My Persona is ready for action!"


    Makoto: "Don’t let them rattle you,focus on their rhythm."


    *Makoto hopes Akihiko is okay as the Daring Gigas and Vehement Idol let out a bloodcurdling roar. Daring Gigas takes a berserk stance*

    ==================================================
                THE CRUCIBLE OF TRIALS
                MISSION: CLEAR LEVEL 8
    ==================================================
    """)

    input("\n[Press Enter to begin the battle...]")

    MainCharacter.curhp = MainCharacter.maxhp
    MainCharacter.cursp = MainCharacter.maxsp

    yukari_takeba = NPC(name="Yukari Takeba", maxhp=180, currenthp=180, defense=18, agility=35, maxsp=140, cursp=140, classification="Ally", personas=[Penthesilea, Cerberus])
    junpei_iori = NPC(name="Junpei Iori", maxhp=220, currenthp=220, defense=24, agility=25, maxsp=90, cursp=90, classification="Ally", personas=[Hermes, Arsene])

    combatants = [MainCharacter, yukari_takeba, junpei_iori, Basalt_Statue, Judgment_Sword]

    status = battle_loop(combatants)

    if status == "Win":
        print("Level 8 cleared!")
        return True
    elif status == "Lose":
        print("GAME OVER")
        return False
    else:
        return False

if __name__ == "__main__":
    level_8()