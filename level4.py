from classes import Character, Player, Skill, Orpheus, Arsene, Izanagi, Cerberus, NPC, Penthesilea
from battle import battle_loop
 
def start_lvl4(MainCharacter):
    print("\n=== LEVEL 4 ===")
    print("\n========================================")
    print("\n Three shadows block your path... ")
    print("Your ally fights beside you once more!")
    print("MISSION: CLEAR LEVEL 4")
    print("========================================\n")
 
def create_level4_combatants(MainCharacter):
    start_lvl4(MainCharacter)
    MainCharacter.curhp = MainCharacter.maxhp
    MainCharacter.cursp = MainCharacter.maxsp
 
    Gojo = NPC(
        #ally
        name="Gojo",
        maxhp=150,
        currenthp=150,
        defense=20,
        maxsp=100,
        cursp=100,
        classification="Ally",
        personas=[Izanagi])
 
    Jogo = NPC(
        #enemy1
        name="Jogo",
        maxhp=200,
        currenthp=200,
        defense=15,
        maxsp=80,
        cursp=80,
        classification="Enemy",
        personas=[Orpheus])
 
    Hanami = NPC(
        #enemy2
        name="Hanami",
        maxhp=200,
        currenthp=200,
        defense=20,
        maxsp=80,
        cursp=80,
        classification="Enemy",
        personas=[Penthesilea])
 
    Mahito = NPC(
        #enemy3
        name="Mahito",
        maxhp=250,
        currenthp=250,
        defense=20,
        maxsp=100,
        cursp=100,
        classification="Enemy",
        personas=[Cerberus])
 
    # 2 vs 3: MainCharacter + Gojo vs Jogo, Hanami, Mahito
    combatants = [MainCharacter, Gojo, Jogo, Hanami, Mahito]
    battle_loop(combatants)