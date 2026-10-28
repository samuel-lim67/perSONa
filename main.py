from classes import Player, Skill, Orpheus, Arsene, Izanagi, Cerberus, NPC, Penthesilea, PhysicalAttack, ElementalAttack, Persona, medicine
from battle import battle_loop
from level1 import level_1
from level2 import level_2
from level3 import level_3
from level4 import level_4
from level5 import level_5
from level10 import level_10
from shop import shop_call
Makoto = Player(name="Makoto Yuki", maxhp=100, currenthp=100, defense=50, agility=10, maxsp=30, cursp=30, personas=[])
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
1 - Inspect {Makoto.name}
2 - Inspect Personas
3 - Check Inventory
4 - Change Slots
5 - Next Battle
""")
      if menu == "1": #inspects the player themselves
        print(f"""
Name: {Makoto.name}
HP: {Makoto.curhp}/{Makoto.maxhp}
Skill Points: {Makoto.cursp}/{Makoto.maxsp}
Personas: {', '.join(persona.name for persona in Makoto.personas)}""")

      elif menu == "2": #inspect personas
        for index, persona in enumerate(Makoto.personas):
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
    Persona: {Makoto.personas[selection-1].name}
Skills: {', '.join(skill.name for skill in Makoto.personas[selection-1].skills)}
---------
Affinity: {Makoto.personas[selection-1].affinity}
Strength: {Makoto.personas[selection-1].strength}
Magic: {Makoto.personas[selection-1].magic}
Endurance: {Makoto.personas[selection-1].endurance}
Agility: {Makoto.personas[selection-1].agility}
Luck: {Makoto.personas[selection-1].luck}
""")
      elif menu == "3":
        Makoto.check_inventory()
      elif menu == "4":
          Makoto.switch_slots()
      elif menu == "5":
        print("Moving to the next battle...")
        break
      else:
        print("Please enter a valid input!")


def main():
    while True:
        Makoto.character_selector(starting_characters)
        intermission()
        if level_1(Makoto):
            intermission()
            if level_2(Makoto):
                intermission()
                if level_3(Makoto):
                    intermission()
                    if level_4(Makoto):
                        intermission()
                        if level_5(Makoto):
                            intermission()

        while True:
            print("Start again? Y/N")
            start_over = input()
            if start_over.strip().lower() == "y":
                break
            elif start_over.strip().lower() == "n":
                return
            else:
                print("Please enter a valid input!")
                continue


if __name__ == "__main__":
    main()