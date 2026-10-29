from classes import Character, Player, Skill, Orpheus, Arsene, Izanagi, Cerberus, NPC, Penthesilea, ElementalAttack, PhysicalAttack, Persona
from battle import battle_loop



# SKILLS
Bufudyne = ElementalAttack("Ice", "Bufudyne", 16, 35, 1, 0.95, "Freeze", 0.10)
Mabufula = ElementalAttack("Ice", "Mabufula", 16, 20, 4, 0.90, "Freeze", 0.05)
Garula = ElementalAttack("Wind", "Garula", 6, 25, 1, 0.99)
Masukukaja = ElementalAttack("Support", "Masukukaja", 24, 15, 4, 1.00)
Dekaja = ElementalAttack("Support", "Dekaja", 10, 0, 4, 1.00)

# PERSONAS
Magical_Magus = Persona("Magical Magus", [Bufudyne, Mabufula], {"Pierce": "resist", "Fire": "weak"}, 23, 28, 20, 24, 15)
Anzu = Persona("Hierophant", [Garula, Masukukaja, Dekaja], {"Wind": "resist", "Lightning": "weak"}, 14, 18, 15, 21, 14)

# COMBATANTS
Yukari_Takeba = NPC("Yukari Takeba", 150, 150, 20, 30, 100, 100, "Ally", [Izanagi])
Dancing_Hand = NPC("Dancing Hand", 100, 100, 20, 10, 100, 100, "Enemy", [Magical_Magus])
Avian_Grandmaster = NPC("Avian Grandmaster", 100, 100, 15, 10, 80, 80, "Enemy", [Anzu])

level3_addcharacters = [Magical_Magus, Anzu]

def level_3(MainCharacter):
    print("""
    ==================================================
                        LEVEL 3
                    THE LAST SIGNAL
    ==================================================

    *Makoto searches an abandoned subway station.*

    Makoto: "Still no signal... Where is everyone?"

    *His communicator crackles.*

    Unknown Voice: "Help... anyone...?"

    *The signal cuts off. Two Shadows appear.*

    Makoto: "I have to get through them!"
    """)

    input("\n[Press Enter to continue...]")

    print("""
    *An unfamiliar power awakens within Makoto.*
    Makoto: "Another Persona...?"
    """)

    input("\n[Press Enter to choose your Persona...]")
    MainCharacter.character_selector(level3_addcharacters)

    print("""
    *Someone calls out from the darkness.*

    Yukari: "Makoto! There you are!"

    Makoto: "Yukari! Let's find the others."

    Yukari: "Right. I'm coming with you!"

    ==================================================
              ALLY REUNITED: YUKARI TAKEBA
                 MISSION: CLEAR LEVEL 3
    ==================================================
    """)

    input("\n[Press Enter to begin the battle...]")

    MainCharacter.curhp = MainCharacter.maxhp
    MainCharacter.cursp = MainCharacter.maxsp

    combatants = [MainCharacter, Yukari_Takeba, Dancing_Hand, Avian_Grandmaster]
    status = battle_loop(combatants)

    if status == "Win":
        print("Level 3 cleared!")
        return True
    elif status == "Lose":
        print("GAME OVER")
        return False
    else:
        return False


if __name__ == "__main__":
    level_3()
