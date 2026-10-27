from classes import NPC, Persona, PhysicalAttack, ElementalAttack, Cerberus, Penthesilea, Player, medicine
from battle import battle_loop

#SKILLS
myriad_arrows = PhysicalAttack("Pierce", "Myriad Arrows", 0.19, 80, 4, 0.88, 0.05)
primal_force = PhysicalAttack("Pierce", "Primal Force", 0.21, 580, 1, 0.95, 0.05)
maralagidyne = ElementalAttack("Fire", "Maralagidyne", 32, 220, 4, 0.9)
#spirit_drain is tbd once i make support skills
heat_wave = PhysicalAttack("Strike", "Heat Wave", 0.20, 280, 4, 0.9, 0.1)

#PERSONA
Mara = Persona("Mara", [myriad_arrows, primal_force, maralagidyne, heat_wave], {"Strike": "absorb","Fire": "absorb", "Ice": "weak","Light": "weak","Dark": "absorb"}, 60, 50, 50, 48, 39)

#ENEMY
Hastur = NPC("Hastur", 1500, 1500, 1, 50, 500, 500, "Enemy", [Mara], status_effect = None)

#ignore this cause were only gonna use one throughout the playthrough
MainCharacter = Player("Prog", 4000, 4000, 400, 50, 100, 100, [Cerberus, Penthesilea], None, [medicine])

combatants = [MainCharacter, Hastur]

def level_10(combatants):
    print("At long last, you reach the top of the tower. All that you've sacrificed along the way have now come to this. Before you stands the figure of a shriveled man, peering down to the city below. You wonder")
    status = battle_loop(combatants)
    if status == "Win":
        print("some dialogue here")
    elif status == "Lose":
        print("GAME OVER")



if __name__ == "__main__":
    level_10(combatants)