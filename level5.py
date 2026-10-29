from classes import Character, Player, Skill, Orpheus, Arsene, Izanagi, Cerberus, NPC, Penthesilea, ElementalAttack, PhysicalAttack, Persona, Zio, Assault_Dive
from battle import battle_loop


# SKILLS
Fatal_End = PhysicalAttack("Slash", "Fatal End", 0.10, 80, 1, 0.95, 0.05)
Blade_of_Fury = PhysicalAttack("Slash", "Blade of Fury", 0.17, 40, 4, 0.90, 0.05)
Heat_Wave = PhysicalAttack("Strike", "Heat Wave", 0.20, 110, 4, 0.90, 0.05)
Swift_Strike = PhysicalAttack("Strike", "Swift Strike", 0.12, 50, 4, 0.90, 0.05)
Bufula = ElementalAttack("Ice", "Bufula", 8, 100, 1, 0.99, "Freeze", 0.10)
Mabufula = ElementalAttack("Ice", "Mabufula", 14, 80, 4, 0.99, "Freeze", 0.08)

# PERSONAS
Castor = Persona("Castor", [Fatal_End, Blade_of_Fury, Heat_Wave], {"Strike": "resist"}, 30, 14, 24, 18, 14)
Castor.arcana = "Hierophant"

Zouchouten = Persona("Zouchouten", [Assault_Dive, Zio, Swift_Strike], {"Slash": "resist", "Wind": "weak"}, 14, 7, 13, 6, 10)
Zouchouten.arcana = "Chariot"

King_Frost = Persona("King Frost", [Bufula, Mabufula], {"Slash": "null", "Pierce": "null", "Ice": "null"}, 18, 31, 26, 14, 20)
King_Frost.arcana = "Emperor"


# COMBATANTS
Makoto_Yuki = NPC("Makoto Yuki", 150, 150, 20, 30, 100, 100, "Ally", [Izanagi, Arsene])
Yukari_Takeba = NPC("Yukari Takeba", 150, 150, 15, 30, 100, 100, "Ally", [Arsene, Penthesilea])

Calm_Basalt = NPC("Calm Basalt", 50, 50, 15, 30, 80, 80, "Enemy", [Castor])
Raging_Facade = NPC("Raging Facade", 50, 50, 20, 30, 80, 80, "Enemy", [Zouchouten])
Intrepid_Knight = NPC("Intrepid Knight", 100, 100, 25, 30, 150, 150, "Enemy", [King_Frost])


# LEVEL 5 PERSONA SELECTION
level5_addcharacters = [Castor, Zouchouten, King_Frost]


# LEVEL 5
def level_5(MainCharacter):
    print("""
    ==================================================
                        LEVEL 5
                   THE TURNING POINT
    ==================================================

    *The walls shift around you. A winding corridor twists open.*

    Yukari: "Wait... is that a room? In the middle of all this?"

    *A mysterious safe haven appears: The Midpoint Bazaar.*

    Makoto: "Finally, somewhere to catch our breath."
    """)

    input("\n[Press Enter to continue...]")

    print("""
    *The team rests and upgrades their gear. Then Yukari notices
    something scrawled across the wall.*

    Yukari: "Makoto... look at this."

    Wall: "This tower is not what it seems..."

    Makoto: "What does that mean?"
    """)

    input("\n[Press Enter to continue...]")

    print("""
    *The floor trembles. A towering figure steps out of the dark.*

    Yukari: "That's... a boss!"

    Makoto: "The Iron Warden. We fight together. Ready?"

    Yukari: "Always!"

    ==================================================
         ALLIES READY: MAKOTO YUKI & YUKARI TAKEBA
                 MISSION: CLEAR LEVEL 5
    ==================================================
    """)

    input("\n[Press Enter to begin the battle...]")

    # Restore the main character
    MainCharacter.curhp = MainCharacter.maxhp
    MainCharacter.cursp = MainCharacter.maxsp

    # Reset allies and enemies
    Makoto_Yuki.curhp = Makoto_Yuki.maxhp
    Makoto_Yuki.cursp = Makoto_Yuki.maxsp

    Yukari_Takeba.curhp = Yukari_Takeba.maxhp
    Yukari_Takeba.cursp = Yukari_Takeba.maxsp

    Calm_Basalt.curhp = Calm_Basalt.maxhp
    Calm_Basalt.cursp = Calm_Basalt.maxsp

    Raging_Facade.curhp = Raging_Facade.maxhp
    Raging_Facade.cursp = Raging_Facade.maxsp

    Intrepid_Knight.curhp = Intrepid_Knight.maxhp
    Intrepid_Knight.cursp = Intrepid_Knight.maxsp

    combatants = [
        MainCharacter,
        Yukari_Takeba,
        Calm_Basalt,
        Raging_Facade,
        Intrepid_Knight
    ]

    status = battle_loop(combatants)

    if status == "Win":
        print("Level 5 cleared! The Iron Warden has fallen.")
        return True
    elif status == "Lose":
        print("GAME OVER")
        return False
    else:
        return False


if __name__ == "__main__":
    level_5()
