from classes import Persona, NPC, ElementalAttack, PhysicalAttack
from battle import battle_loop

# SKILLS
Cleave = PhysicalAttack("Slash", "Cleave", 3, 30, 1, 0.95, 0.12)
Assault_Dive = PhysicalAttack("Strike", "Assault Dive", 8, 55, 1, 0.90, 0.12)

Garu = ElementalAttack("Wind", "Garu", 3, 25, 1, 0.95, )
Magaru = ElementalAttack("Wind", "Magaru", 6, 20, 4, 0.90, )
Zionga = ElementalAttack("Electric", "Zionga", 8, 60, 1, 0.90, )


# PERSONAS
eligor = Persona(name="Eligor",skills=[Cleave, Assault_Dive],affinity={"Strike": "resist","Wind": "weak"},strength=18,magic=9,endurance=15,agility=11, luck=10)
harmonic_relic = Persona( name="Harmonic Relic",skills=[Garu, Magaru, Zionga],affinity={"Wind": "Resist"},strength=12,magic=32,endurance=18,agility=22,luck=20)
# ENEMIES
Jail_Guard = NPC(name="Jail Guard", maxhp=85, currenthp=85, defense=28, agility=22, maxsp=70, cursp=70, classification="Enemy", personas=[eligor])
Carnal_Snake = NPC(name="Carnal Snake", maxhp=70, currenthp=70, defense=18, agility=32, maxsp=90, cursp=90, classification="Enemy", personas=[harmonic_relic])

level9_addcharacters = [eligor, harmonic_relic]
# LEVEL 9
def level_9(MainCharacter):
    print("""
    ==================================================
                        LEVEL 9
                 THE FINAL REUNION
    ==================================================


    *The team senses a suspicious aura from around the corner.*


    Makoto: "Keep your guard up anyone"


    *His communicator crackles once again.*


    Unknown Voice: "Hellooo... Makoto...?"


    Makoto: "Akihiko?!?! "


    *The signal cuts off. Two Shadows appear.*


    Makoto: "We can’t lose them again team!"
    """)

    input("\n[Press Enter to continue...]")

    print("""
    *An unfamiliar power awakens within Makoto.*


    Makoto: "Another Persona...?"
    """)

    input("\n[Press Enter to choose your Persona...]")

    MainCharacter.character_selector(level9_addcharacters)

    print("""
    *Someone calls out from the darkness.*


    Akihiko: "Everyone! Finally!"


    Makoto: "Long time no see! I hope you're ready for what’s next."


    Akihiko: "Understood! I will do my best"


    *The Jail Guard’s heavy armor and chains grind against the stone floor, and the Carnal Snake coils tightly, its eyes glowing with a hypnotic malice. Will you make it to the end?*
    """)

    input("\n[Press Enter to begin the battle...]")

    MainCharacter.curhp = MainCharacter.maxhp
    MainCharacter.cursp = MainCharacter.maxsp

    combatants = [MainCharacter, Jail_Guard, Carnal_Snake]
    status = battle_loop(combatants)

    if status == "Win":
        print("Level 9 cleared!")
        return True
    elif status == "Lose":
        print("GAME OVER")
        return False
    else:
        return False

if __name__ == "__main__":
    level_9()