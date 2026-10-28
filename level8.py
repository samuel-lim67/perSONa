from classes import Character, Player, Skill, Orpheus, Arsene, Izanagi, Cerberus, Penthesilea, Persona, PhysicalAttack, ElementalAttack, NPC
from battle import battle_loop


# ---------- SKILLS ----------

# Daring Gigas (Strength + Chariot) Skills - Attack/Defense Juggernaut
Mabufula = ElementalAttack("Ice", "Mabufula", 22, 200, 4, 0.99, "Freeze", 0.08)
Bufudyne = ElementalAttack("Ice", "Bufudyne", 18, 180, 1, 0.95, "Freeze", 0.10)

Devastating_End = PhysicalAttack("Slash", "Devastating End", 0.10, 225, 1, 0.95, 0.05)

# Vehement Idol (Lovers + Priestess) Skills - Speed/Critical Striker
Swift_Strike = PhysicalAttack("Strike", "Swift Strike", 0.12, 210, 4, 0.90, 0.05)
Myriad_Arrows =  PhysicalAttack("Pierce", "Myriad Arrows", 0.19, 80, 4, 0.88, 0.05)


# ---------- PERSONAS ----------

# Persona(name, skills, affinity, strength, magic, endurance, agility, luck)

Daring_Gigas_Persona = Persona("Flauros",[Mabufula, Bufudyne],{"Ice": "resist", "Phys": "null", "Fire": "weak"},24, 30, 32, 16, 18)
Daring_Gigas_Persona.arcana = "Strength"


Daring_Gigas_Persona2 = Persona("Titan",[Devastating_End],{"Ice": "resist", "Phys": "null", "Fire": "weak"},28, 28, 30, 18, 16)
Daring_Gigas_Persona2.arcana = "Chariot"


Vehement_Idol_Persona = Persona("Leanan Sidhe",[Swift_Strike],{"Ice": "resist", "Fire": "resist", "Phys": "weak"},32, 17, 20, 30, 21)


Vehement_Idol_Persona2 = Persona("Paravati",[Myriad_Arrows],{"Ice": "resist", "Fire": "resist", "Phys": "weak"},32, 19, 22, 38, 23)



# ---------- ENEMIES ----------

daring_gigas = NPC(
    name="Daring Gigas",
    maxhp=550,
    currenthp=550,
    defense=25,
    maxsp=200,
    cursp=200,
    classification="Enemy",
    personas=[Daring_Gigas_Persona, Daring_Gigas_Persona2]
)


vehement_idol = NPC(
    name="Vehement Idol",
    maxhp=420,
    currenthp=420,
    defense=18,
    maxsp=150,
    cursp=150,
    classification="Enemy",
    personas=[Vehement_Idol_Persona, Vehement_Idol_Persona2]
)


# ---------- LEVEL 2 ----------

def level_8(MainCharacter):
    print("""
    ==================================================
                        LEVEL 8
                  TWO ELITE ENEMIES
    ==================================================


    *Psychological pressure, self-doubt, and the insurmountable strength of the dual-persona Elite Shadows before you.*


    Yukari: "These two… they feel different than the other shadows again, watch out."


    Junpei: "Tsc, psychological warfare? Imma show them physical warfare! My Persona is ready for action!"


    Makoto: "Don’t let them rattle you,focus on their rhythm."


    *Makoto hopes Akihiko is okay as the Daring Gigas and Vehement Idol let out a bloodcurdling roar. Daring Gigas takes a berserk stance*

    ==================================================
                THE CRUCIBLE OF TRIALS
                MISSION: CLEAR LEVEL 8
    ==================================================
    """)

    input("\n[Press Enter to begin the battle...]")

    MainCharacter.curhp = MainCharacter.maxhp
    MainCharacter.cursp = MainCharacter.maxsp

    # 3 Allies
    makoto_yuki = NPC(
        name="Makoto Yuki",
        maxhp=200,
        currenthp=200,
        defense=22,
        maxsp=120,
        cursp=120,
        classification="Ally",
        personas=[Orpheus, Izanagi]
    )


    yukari_takeba = NPC(
        name="Yukari Takeba",
        maxhp=180,
        currenthp=180,
        defense=18,
        maxsp=140,
        cursp=140,
        classification="Ally",
        personas=[Penthesilea, Cerberus]
    )


    junpei_iori = NPC(
        name="Junpei Iori",
        maxhp=220,
        currenthp=220,
        defense=24,
        maxsp=90,
        cursp=90,
        classification="Ally",
        personas=[Arsene]
    )


    # 3 Allies vs 2 Enemies
    combatants = [
        MainCharacter,
        makoto_yuki,
        yukari_takeba,
        junpei_iori,
        daring_gigas,
        vehement_idol
    ]

    status = battle_loop(combatants)

    if status == "Win":
        print("You have cleared Level 8!")
        return True
    else:
        print("You have been defeated...")
        return False

if __name__ == "__main__":
    level_8()