from classes import Character, Player, Skill, Orpheus, Arsene, Izanagi, Cerberus, NPC, Penthesilea, Persona, ElementalAttack, PhysicalAttack
from battle import battle_loop
from selection import character_selector

starting_characters = [Orpheus, Arsene, Izanagi, Cerberus, Penthesilea]

def start_lvl3(MainCharacter):
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
    Makoto: "Another Persona...?""")

    input("\n[Press Enter to choose your Persona...]")
    character_selector(starting_characters, MainCharacter)

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

def create_level3_combatants(MainCharacter):
    start_lvl3(MainCharacter)
    MainCharacter.curhp = MainCharacter.maxhp
    MainCharacter.cursp = MainCharacter.maxsp
    Bufudyne = ElementalAttack(
        element="Ice", name="Bufudyne", cost=16, effect=35, 
        targets=1, accuracy=95, 
        sideeffecttype="Freeze", sideeffectchance=0.10)
    
    Mabufula = ElementalAttack(
        element="Ice", name="Mabufula", cost=16, effect=20, 
        targets=2, accuracy=90, 
        sideeffecttype="Freeze", sideeffectchance=0.05)
    
    Concentrate = ElementalAttack(
        element="Ice", name="Concentrate", cost=15, effect=2.0, 
        targets=1, accuracy=100,sideeffectchance=0.05)

    Garula = ElementalAttack(
        element="Wind", name="Garula", cost=6, effect=25, 
        targets=1, accuracy=99, 
        sideeffecttype="None", sideeffectchance=0.00)
    
    Masukukaja = ElementalAttack(
        element="Wind", name="Masukukaja", cost=24, effect=15, 
        targets=2, accuracy=100,sideeffectchance=0.00)
    
    Dekaja = ElementalAttack(
        element="Wind", name="Dekaja", cost=10, effect=0, 
        targets="2", accuracy=100,sideeffectchance=0.00)
        
    Magical_Magus = Persona("Magical Magus", [Bufudyne, Mabufula, Concentrate], {"Pierce": "resist", "Fire": "weak"}, 23, 28, 20, 24, 15)
    Anzu = Persona("Hierophant", [Garula, Masukukaja, Dekaja], {"Wind": "resist", "Lightning": "weak"}, 14, 18, 15, 21, 14)
    
    Yukari_Takeba = NPC(
            #Ally1
            name="Yukari Takeba",
            maxhp=150,
            currenthp=150,
            defense=20,
            maxsp=100,
            cursp=100,
            classification="Ally",
            personas=[Izanagi])

    Dancing_Hand = NPC(
        #enemy1
        name="Dancing Hand",
        maxhp=250,
        currenthp=250,
        defense=20,
        maxsp=100,
        cursp=100,
        classification="Enemy",
        personas=[Magical_Magus])

    Avian_Grandmaster = NPC(
        #enemy2
        name="Avian Grandmaster",
        maxhp=250,
        currenthp=250,
        defense=15,
        maxsp=80,
        cursp=80,
        classification="Enemy",
        personas=[Anzu])
    
    combatants = [MainCharacter, Yukari_Takeba, Dancing_Hand, Avian_Grandmaster]
    
    battle_loop(combatants)