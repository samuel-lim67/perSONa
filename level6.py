from classes import NPC, Persona, PhysicalAttack, ElementalAttack, Penthesilea, Izanagi
from battle import battle_loop


# SKILLS
Agidyne = ElementalAttack("Fire", "Agidyne", 12, 160, 1, 0.95, "Burn", 0.10)
Bufudyne = ElementalAttack("Ice", "Bufudyne", 12, 160, 1, 0.95, "Freeze", 0.10)
Ziodyne = ElementalAttack("Electric", "Ziodyne", 12, 160, 1, 0.95, "Shock", 0.10)
Garudyne = ElementalAttack("Wind", "Garudyne", 12, 160, 1, 0.95)


Gigantomachia = PhysicalAttack("Strike", "Gigantomachia", 0.25, 200, 4, 0.90,0.05)
Gods_Hand = PhysicalAttack("Strike", "God's Hand", 0.25, 180, 1, 0.88, 0.13)
Vicious_Strike = PhysicalAttack("Strike", "Vicious Strike", 0.18, 160, 4, 0.8, 0.05)


# PERSONAS
Surtr = Persona("Surtr", [Agidyne, Bufudyne, Ziodyne, Garudyne], {"Phys": "resist", "Ice": "weak"}, 12, 18, 10, 24, 12)

White_Rider = Persona("White Rider", [Gigantomachia, Gods_Hand, Vicious_Strike], {"Phys": "resist", "Curse": "weak"}, 28, 8, 22, 24, 12)

# COMBATANTS
Yukari_Takeba = NPC("Yukari Takeba", 100, 100, 15, 30, 100, 100, "Ally", [Penthesilea])
Noble_Seeker = NPC("Noble Seeker", 70, 70, 15, 30, 240, 240, "Enemy", [Surtr])
Steed_Beast = NPC("Steed Beast", 70, 70, 20, 30, 80, 80, "Enemy", [White_Rider])

level6_addcharacters = [Surtr, White_Rider]

# LEVEL 6
def level_6(MainCharacter):
    print("""
    ==================================================
                        LEVEL 6
               SHATTERED MIRRORED HALLS
    ==================================================


    *The party advances deeper into a distorted hall lined with fracture-cracked mirrors.*


    Yukari: "Look out! The reflections in these mirrors aren't moving with us..."


    Makoto Yuki: "Be on your guard. The air here feels heavy... an intense aura is approaching."


    *The glass shatters outward as two elite Shadows emerge from the rift!*


    *One channels intense elemental magic, while the other readies a charging strike!*


    Noble Seeker: "Intruders shall not pass the inner sanctuary..."


    Steed Beast: "Prepare to be crushed!"
    """)


    input("\n[Press Enter to continue...]")


    print("""
    *An ancient power resonates from the shattered glass, surging into your mind.*


    Makoto Yuki: "You feel it too, don't you? Let that power guide your wild card!"
    """)


    input("\n[Press Enter to choose your Persona...]")
    MainCharacter.character_selector(level6_addcharacters)


    print("""
    Yukari: "We've faced worse than this! Let's hit them with everything we've got!"


    Makoto Yuki: "Right. Focus on their weaknesses and coordinate our strikes!"


    ==================================================
                  ELITE SHADOW ENCOUNTER
                  MISSION: CLEAR LEVEL 6
    ==================================================
    """)

    input("\n[Press Enter to begin the battle...]")

    MainCharacter.curhp = MainCharacter.maxhp
    MainCharacter.cursp = MainCharacter.maxsp

    Yukari_Takeba.curhp = Yukari_Takeba.maxhp
    Yukari_Takeba.cursp = Yukari_Takeba.maxsp

    Noble_Seeker.curhp = Noble_Seeker.maxhp
    Noble_Seeker.cursp = Noble_Seeker.maxsp

    Steed_Beast.curhp = Steed_Beast.maxhp
    Steed_Beast.cursp = Steed_Beast.maxsp

    combatants = [MainCharacter, Yukari_Takeba, Noble_Seeker, Steed_Beast]

    status = battle_loop(combatants)

    if status == "Win":
        print("Level 6 cleared!")
        return True
    elif status == "Lose":
        print("GAME OVER")
        return False
    else:
        return False

if __name__ == "__main__":
    level_6()