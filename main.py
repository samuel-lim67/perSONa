from classes import Character, Player, Skill, Orpheus, Arsene, Izanagi, Cerberus, NPC, Penthesilea, PhysicalAttack, ElementalAttack, Persona, medicine
from battle import battle_loop
from level2 import create_level2_combatants
from level3 import create_level3_combatants
from level10 import level_10
from shop import shop_call
MainCharacter = Player("Prog", 4000, 4000, 400, 50, 100, 100, [Cerberus, Penthesilea], None, [medicine])
Enemy = NPC("TestDummy1", 200, 200, 20, 100, 100 ,100, "Enemy", [Cerberus])
Ally = NPC("TestAlly1", 200, 200, 20, 50, 100, 100, "Ally", [Penthesilea])

#LEVEL 10////////////////////////////////////////////
#SKILLS
myriad_arrows = PhysicalAttack("Pierce", "Myriad Arrows", 0.19, 80, 4, 0.88, 0.05)
primal_force = PhysicalAttack("Pierce", "Primal Force", 0.21, 580, 1, 0.95, 0.05)
maralagidyne = ElementalAttack("Fire", "Maralagidyne", 32, 220, 4, 0.9)
heat_wave = PhysicalAttack("Strike", "Heat Wave", 0.20, 280, 4, 0.9, 0.1)

#PERSONAS
Mara = Persona("Mara", [myriad_arrows, primal_force, maralagidyne, heat_wave], {"Strike": "absorb","Fire": "absorb", "Ice": "weak","Light": "weak","Dark": "absorb"}, 60, 50, 50, 48, 39)

#ENEMIES
Hastur = NPC("Hastur", 1500, 1500, 1, 50, 500, 500, "Enemy", [Mara], status_effect = None)

level_10_combatants = [MainCharacter, Hastur]


combatants = [MainCharacter, Enemy, Ally]

starting_characters = [Orpheus, Arsene, Izanagi]

def intermission():
  progress_game = input(f"""
====================INTERMISSION====================
Are you ready to enter the next battle?
(Y/N)
""")
  if progress_game.lower().strip() == "y":
    print("Moving to the next battle...")
    return
  else:
    while True:
      menu = input(f"""
What would you like to do?
1 - Inspect {MainCharacter.name}
2 - Inspect Personas
3 - Check Inventory
4 - Change Slots
5 - Next Battle
""")
      if menu == "1": #inspects the player themselves
        print(f"""
Name: {MainCharacter.name}
HP: {MainCharacter.curhp}/{MainCharacter.maxhp}
Skill Points: {MainCharacter.cursp}/{MainCharacter.maxsp}
Personas: {', '.join(persona.name for persona in MainCharacter.personas)}""")

      elif menu == "2": #inspect personas
        for index, persona in enumerate(MainCharacter.personas):
            print(f"{index+1}. {persona.name}")
        try:
          selection = int(input("Please select a persona to inspect\n"))
        except ValueError:
          print("Please enter a valid input!")
          continue
        else:
          if selection <= 0:
            print("Please enter a valid input!")
            continue
          else:
            print(f"""
Persona: {MainCharacter.personas[selection-1].name}
Skills: {', '.join(skill.name for skill in MainCharacter.personas[selection-1].skills)}
---------
Affinity: {MainCharacter.personas[selection-1].affinity}
Strength: {MainCharacter.personas[selection-1].strength}
Magic: {MainCharacter.personas[selection-1].magic}
Endurance: {MainCharacter.personas[selection-1].endurance}
Agility: {MainCharacter.personas[selection-1].agility}
Luck: {MainCharacter.personas[selection-1].luck}
""")
      elif menu == "3":
        MainCharacter.check_inventory()
      elif menu == "4":
          MainCharacter.switch_slots()
      elif menu == "5":
        print("Moving to the next battle...")
        break
      else:
        print("Please enter a valid input!")


def main():
    while True:
      MainCharacter.character_selector(starting_characters)
      intermission()
      shop_call()
      create_level2_combatants(MainCharacter)
      level_10(level_10_combatants)

if __name__ == "__main__":
    main()