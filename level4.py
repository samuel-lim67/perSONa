from classes import Character, Player, Skill, Izanagi, NPC
from classes import Persona, PhysicalAttack, ElementalAttack
from battle import battle_loop
 
# ---------- NEW SKILLS (level 4) ----------
# PhysicalAttack(element, name, cost, effect, targets, accuracy, criticalchance)
# ElementalAttack(element, name, cost, effect, targets, accuracy, sideeffecttype, sideeffectchance)
Strike_Attack = PhysicalAttack("Strike", "Strike Attack", 0, 40, 1, 0.95, 0.05)
Magaru = ElementalAttack("Wind", "Magaru", 8, 40, 4, 0.99)
Slash_Attack = PhysicalAttack("Slash", "Slash Attack", 0, 40, 1, 0.95, 0.05)
Power_Slash = PhysicalAttack("Slash", "Power Slash", 0.1, 80, 1, 0.9, 0.10)
Agidyne = ElementalAttack("Fire", "Agidyne", 14, 220, 1, 0.99)
Deathbound = PhysicalAttack("Slash", "Deathbound", 0.25, 130, 4, 0.9, 0.05)
 
# ---------- NEW PERSONAS (level 4) ----------
# Persona(name, skills, affinity, strength, magic, endurance, agility, luck)
Venus_Eagle = Persona("Venus Eagle", [Slash_Attack, Power_Slash],
                      {"Slash": "resist", "Electric": "weak"},
                      12, 18, 10, 24, 12)
Venus_Eagle.arcana = "Lovers"
 
Swift_Axle = Persona("Swift Axle", [Strike_Attack, Magaru],
                     {"Electric": "weak", "Slash": "resist", "Strike": "resist"},
                     22, 8, 16, 20, 8)
Swift_Axle.arcana = "Chariot"
 
Surt = Persona("Surt", [Agidyne, Deathbound],
               {"Pierce": "null", "Ice": "weak"},
               22, 28, 18, 14, 16)
Surt.arcana = "Emperor"
 
def start_lvl4(MainCharacter):
    print("\n=== LEVEL 4 - Corridors of Doubt ===")
    print("\n========================================")
    print("\n Three shadows block your path... ")
    print("Your ally fights beside you once more!")
    print("MISSION: CLEAR LEVEL 4")
    print("========================================\n")
 
def create_level4_combatants(MainCharacter):
    start_lvl4(MainCharacter)
    MainCharacter.curhp = MainCharacter.maxhp
    MainCharacter.cursp = MainCharacter.maxsp
 
    MakotoYuki = NPC(
        #ally
        name="Makoto Yuki",
        maxhp=150,
        currenthp=150,
        defense=20,
        maxsp=100,
        cursp=100,
        classification="Ally",
        personas=[Izanagi])
 
    WildDrive = NPC(
        #enemy1 (Chariot) -> Swift Axle persona
        name="Wild Drive",
        maxhp=200,
        currenthp=200,
        defense=15,
        maxsp=60,
        cursp=60,
        classification="Enemy",
        personas=[Swift_Axle])
 
    TranceTwins = NPC(
        #enemy2 (Lovers) -> Venus Eagle persona
        name="Trance Twins",
        maxhp=150,
        currenthp=150,
        defense=10,
        maxsp=80,
        cursp=80,
        classification="Enemy",
        personas=[Venus_Eagle])
 
    FatalTurret = NPC(
        #enemy3 (Emperor) -> Surt persona
        name="Fatal Turret",
        maxhp=250,
        currenthp=250,
        defense=20,
        maxsp=120,
        cursp=120,
        classification="Enemy",
        personas=[Surt])
 
    # 2 vs 3: MainCharacter + MakotoYuki vs Wild Drive, Trance Twins, Fatal Turret
    combatants = [MainCharacter, MakotoYuki, WildDrive, TranceTwins, FatalTurret]
    battle_loop(combatants)