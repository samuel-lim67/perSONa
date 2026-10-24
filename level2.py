from classes import Character, Player, Skill, Orpheus, Arsene, Izanagi, Cerberus, NPC, Penthesilea
from battle import battle_loop
from selection import character_selector

def start_lvl2(MainCharacter):
    print("\n=== LEVEL 2 ===")
    MainCharacter.curhp = MainCharacter.maxhp
    MainCharacter.cursp = MainCharacter.maxsp

def create_level2_combatants(MainCharacter):
    start_lvl2(MainCharacter)
    Kokushibo = NPC(
        #enemy1
        name="Kokushibo",
        maxhp=80,
        currenthp=80,
        defense=20,
        maxsp=100,
        cursp=100,
        classification="Enemy",
        personas=[Penthesilea])

    Muzan = NPC(
        #enemy2
        name="Muzan",
        maxhp=80,
        currenthp=80,
        defense=15,
        maxsp=80,
        cursp=80,
        classification="Enemy",
        personas=[Arsene])
    combatants = [MainCharacter, Kokushibo, Muzan]
    battle_loop(combatants)