from classes import Player, Skill, Orpheus, Arsene, Izanagi, Cerberus, NPC, Penthesilea, PhysicalAttack, ElementalAttack, Persona, medicine
from battle import battle_loop
from level1 import level_1
from level2 import level_2
from level3 import level_3
from level4 import level_4
from level5 import level_5
from level6 import level_6
from level7 import level_7
from level8 import level_8
from level9 import level_9
from level10 import level_10
from shop import shop_call
Makoto = Player(name="Makoto Yuki", maxhp=333, currenthp=333, defense=50, agility=30, maxsp=60, cursp=30, personas=[])

starting_characters = [Orpheus, Arsene, Izanagi]

print("""
    ==================================================
                    Persona 3 Relaod
                     Save the World
    ==================================================

    *In order to prevent a great cataclysm, you must 
    go through 10 levels of challenges to prove your
    worth and defeat the source of this malice. *

    *You are apart of a team named SEES tasked with 
    saving the earth, but you were seperated and must
    reunite within the dungeon. Your persona will 
    guide the way.*

    ==================================================
    """)

def battle_rewards():
    print("You earned 50 gold!")
    Makoto.coins += 100


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
Personas: {', '.join(persona.name for persona in Makoto.personas)}
Coins: {Makoto.coins}""")

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
            battle_rewards()
            intermission()
            if level_2(Makoto):
                battle_rewards()
                intermission()
                if level_3(Makoto):
                    battle_rewards()
                    intermission()
                    if level_4(Makoto):
                        battle_rewards()
                        intermission()
                        if level_5(Makoto):
                            battle_rewards()
                            shop_call(Makoto)
                            intermission()
                            if level_6(Makoto):
                                battle_rewards()
                                intermission()
                                if level_7(Makoto):
                                    battle_rewards()
                                    intermission()
                                    if level_8(Makoto):
                                        battle_rewards()
                                        intermission()
                                    if level_9(Makoto):
                                        battle_rewards()
                                        intermission()
                                        if level_10(Makoto):
                                            print("Congratulations, you have successfully reached the final destination!")
                                            return

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