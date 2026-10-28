
from classes import Character, Player, Skill, Orpheus, Arsene, Izanagi, Cerberus, NPC, Penthesilea
from battle import battle_loop
 
def start_lvl5(MainCharacter):
    print("\n=== LEVEL 5 ===")
    print("\n========================================")
    print("\n The final shadow awaits... ")
    print("You and your allies stand together against a powerful boss!")
    print("MISSION: CLEAR LEVEL 5")
    print("========================================\n")
 
def create_level5_combatants(MainCharacter):
    start_lvl5(MainCharacter)
    MainCharacter.curhp = MainCharacter.maxhp
    MainCharacter.cursp = MainCharacter.maxsp
 
    Gojo = NPC(
        #ally1
        name="Gojo",
        maxhp=150,
        currenthp=150,
        defense=20,
        maxsp=100,
        cursp=100,
        classification="Ally",
        personas=[Izanagi])
 
    Itadori = NPC(
        #ally2
        name="Itadori",
        maxhp=150,
        currenthp=150,
        defense=15,
        maxsp=100,
        cursp=100,
        classification="Ally",
        personas=[Arsene])
 
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
 
    Sukuna = NPC(
        #BOSS 
        name="Sukuna",
        maxhp=450,
        currenthp=450,
        defense=25,
        maxsp=150,
        cursp=150,
        classification="Enemy",
        personas=[Cerberus])
 
    # 3 vs 3: MainCharacter + Gojo + Itadori vs Jogo, Hanami, Sukuna (boss)
    combatants = [MainCharacter, Gojo, Itadori, Jogo, Hanami, Sukuna]
    battle_loop(combatants)