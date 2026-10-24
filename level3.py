from classes import Character, Player, Skill, Orpheus, Arsene, Izanagi, Cerberus, NPC, Penthesilea
from battle import battle_loop
from selection import character_selector

starting_characters = [Orpheus, Arsene, Izanagi, Cerberus]

def start_lvl3(MainCharacter):
    print("\n=== LEVEL 3 ===")
    start_lvl3()
    print("\n========================================")
    print("\n Your eforts are not in vain... ")
    print("A new power awaits within you.")
    print("Choose a Persona to unlock your potential!")
    character_selector(starting_characters,MainCharacter)
    print("========================================\n")

def create_level3_combatants(MainCharacter):
    start_lvl3()
    MainCharacter.curhp = MainCharacter.maxhp
    MainCharacter.cursp = MainCharacter.maxsp
    Gojo = NPC(
            #enemy1
            name="Gojo",
            maxhp=150,
            currenthp=150,
            defense=20,
            maxsp=100,
            cursp=100,
            classification="Ally",
            personas=[Izanagi])

    Kenjaku = NPC(
        #enemy1
        name="Kenjaku",
        maxhp=250,
        currenthp=250,
        defense=20,
        maxsp=100,
        cursp=100,
        classification="Enemy",
        personas=[Orpheus])

    Sukuna = NPC(
        #enemy2
        name="Sukuna",
        maxhp=250,
        currenthp=250,
        defense=15,
        maxsp=80,
        cursp=80,
        classification="Enemy",
        personas=[Cerberus])
    combatants = [MainCharacter, Kokushibo, Muzan, Gojo]
    battle_loop(combatants)

