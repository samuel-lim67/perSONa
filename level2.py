from classes import Character, Player, Skill, Orpheus, Arsene, Izanagi, Cerberus, NPC, Penthesilea, Persona, ElementalAttack, PhysicalAttack
from battle import battle_loop
from selection import character_selector

def start_lvl2(MainCharacter):
    print("\n=== LEVEL 2 ===")
    MainCharacter.curhp = MainCharacter.maxhp
    MainCharacter.cursp = MainCharacter.maxsp

def create_level2_combatants(MainCharacter):
    start_lvl2(MainCharacter)
    Agi = ElementalAttack(
        element="Fire", name="Agi", cost=4, effect=15, 
        targets="Single", accuracy=95, 
        sideeffecttype="Burn", sideeffectchance=0.10)
    
    Maragi = ElementalAttack(
        element="Fire", name="Maragi", cost=8, effect=10, 
        targets="All", accuracy=90, 
        sideeffecttype="Burn", sideeffectchance=0.05)
    
    Rakunda = PhysicalAttack(
        element="Support", name="Rakunda", cost=8, effect=-20, 
        targets="Single", accuracy=100, criticalchance=0.05) 

    Psio = ElementalAttack(element="Psy", name="Psio",  cost=10, effect=40, targets="Single",
        accuracy=95, sideeffecttype="Brainwash", sideeffectchance=0.10)
    Assault_Dive = PhysicalAttack( element="Strike", name="Assault Dive", cost=12,  effect=55, 
        targets="Single",  accuracy=85, criticalchance=0.12)
    Marakukaja = ElementalAttack(element="Support",  name="Marakukaja", cost=12, effect=20, targets="All",  accuracy=100,sideeffectchance=0.10)
    
    Pyro_Jack = Persona("Pyro Jack", [Agi, Maragi, Rakunda], {"Fire": "resist", "Ice": "weak"}, 14, 18, 15, 21, 14)
    Hierophant = Persona("Hierophant", [Psio, Assault_Dive, Marakukaja], {"Fire": "resist", "Ice": "weak"}, 15, 28, 18, 22, 12)
    
    Crying_Tablet = NPC(
        #enemy1
        name="Crying Tablet",
        maxhp=50,
        currenthp=50,
        defense=20,
        maxsp=100,
        cursp=100,
        classification="Enemy",
        personas=[Pyro_Jack])

    Phantom_Mage = NPC(
        #enemy2
        name="Phantom Mage",
        maxhp=50,
        currenthp=50,
        defense=15,
        maxsp=80,
        cursp=80,
        classification="Enemy",
        personas=[Hierophant])

    combatants = [MainCharacter, Crying_Tablet, Phantom_Mage]
    battle_loop(combatants)

    