from EEE111.Include.perSONa.main import combatants
from classes import NPC, Persona, PhysicalAttack, ElementalAttack, Cerberus, Penthesilea, Player
from battle import battle_loop


myriad_arrows = PhysicalAttack("Pierce", "Myriad Arrows", 0.19, 80, 4, 0.88, 0.05)
primal_force = PhysicalAttack("Pierce", "Primal Force", 0.21, 580, 1, 0.95, 0.05)
maralagidyne = ElementalAttack("Fire", "Maralagidyne", 32, 220, 4, 0.9)
#spirit_drain is tbd once i make support skills
heat_wave = PhysicalAttack("Strike", "Heat Wave", 0.20, 280, 4, 0.9, 0.1)
Mara = Persona("Mara", [myriad_arrows, primal_force, maralagidyne, heat_wave], {"Strike": "absorb","Fire": "absorb", "Ice": "weak","Light": "weak","Dark": "absorb"}, 60, 50, 50, 48, 39)


Hastur = NPC("Hastur", 1500, 1500, 300, 300, 500, 500, "Enemy", [Mara], status_effect = None)

MainCharacter = Player("Prog", 4000, 4000, 400, 50, 100, 100, [Cerberus, Penthesilea])

combatants = [MainCharacter, Hastur]

battle_loop(combatants)