from classes import Persona, NPC, ElementalAttack, PhysicalAttack, Orpheus, Arsene, Izanagi, Cerberus, Penthesilea
from battle import battle_loop


# SKILLS
Megido = ElementalAttack("Almighty", "Megido", 20, 170, 4, 0.99)
Maragidyne = ElementalAttack("Fire", "Maragidyne", 22, 160, 0, 0.95, "Burn", 0.10)

Brave_Blade = PhysicalAttack("Slash", "Brave Blade", 0.24, 210, 1, 0.90, 0.12)
Myriad_Arrows =  PhysicalAttack("Pierce", "Myriad Arrows", 0.19, 80, 4, 0.88, 0.05)

Deathbound = PhysicalAttack("Slash", "Deathbound", 0.22, 180, 4, 0.85, 0.12)


# PERSONAS
Basalt_Statue_Persona = Persona("Daisoujou", [Megido, Maragidyne], {"Phys": "resist", "Fire": "null", "Curse": "weak"}, 18, 26, 28, 12, 14)
Basalt_Statue_Persona.arcana = "Hierophant"

Judgment_Sword_Persona = Persona("Melchizedek", [Brave_Blade, Myriad_Arrows], {"Phys": "resist", "Wind": "weak"}, 28, 12, 16, 26, 18)
Judgment_Sword_Persona.arcana = "Justice"

Decaying_Titan_Persona = Persona("Hell Biker", [Deathbound], {"Phys": "resist", "Ice": "weak"}, 26, 20, 24, 14, 10)
Decaying_Titan_Persona.arcana = "Hanged Man"


# ENEMIES
Basalt_Statue = NPC(name="Basalt Statue", maxhp=80, currenthp=80, defense=25, agility=30, maxsp=200, cursp=200, classification="Enemy", personas=[Basalt_Statue_Persona])
Judgment_Sword = NPC(name="Judgment Sword", maxhp=80, currenthp=80, defense=18, agility=30, maxsp=150, cursp=150, classification="Enemy", personas=[Judgment_Sword_Persona])
Decaying_Titan = NPC(name="Decaying Titan", maxhp=200, currenthp=200, defense=22, agility=30, maxsp=180, cursp=180, classification="Enemy", personas=[Decaying_Titan_Persona])


# LEVEL 7
def level_7(MainCharacter):
    print("""
    ==================================================
                        LEVEL 7
                  THE DEEPENING CHASM
    ==================================================


    *The air grows suffocatingly cold as a Basalt Statue comes to life from bedrock.*


    Junpei: "Whoa… okay, temperature just dropped 20 degrees. Are we sure we're heading in the right direction?"


    Yukari: "Yes Junpei, it's fine. Stay close, the shadows down here are reacting to our panic."


    Makoto: "Let's move it guys, I can see the next group of enemies."


    *Junpei's grip tightens on his hilt as the Decaying Titan looms forward.*
    """)

    input("\n[Press Enter to continue...]")

    print("""
    Junpei: "Hell yeah! Let's show these overgrown rocks what we can do!"


    Yukari: "Watch out for the Titan! Don't let them surround us!"


    ==================================================
                 DEEP CHASM AMBUSH
               MISSION: CLEAR LEVEL 7
    ==================================================
    """)

    input("\n[Press Enter to begin the battle...]")

    MainCharacter.curhp = MainCharacter.maxhp
    MainCharacter.cursp = MainCharacter.maxsp

    yukari_takeba = NPC(name="Yukari Takeba", maxhp=180, currenthp=180, defense=18, agility=30, maxsp=140, cursp=140, classification="Ally", personas=[Penthesilea, Cerberus])
    junpei_iori = NPC(name="Junpei Iori", maxhp=220, currenthp=220, defense=24, agility=30, maxsp=90, cursp=90, classification="Ally", personas=[Arsene])

    combatants = [MainCharacter, yukari_takeba, junpei_iori, Basalt_Statue, Judgment_Sword, Decaying_Titan]

    status = battle_loop(combatants)

    if status == "Win":
        print("Level 7 cleared!")
        return True
    elif status == "Lose":
        print("GAME OVER")
        return False
    else:
        return False


if __name__ == "__main__":
    level_7()
