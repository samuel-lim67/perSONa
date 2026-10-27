from classes import Character, Player, Skill, Orpheus, Arsene, Izanagi, Cerberus, NPC, Penthesilea
from battle import battle_loop
from level2 import create_level2_combatants
from level3 import create_level3_combatants

MainCharacter = Player("Prog", 300, 300, 20, 50, 100, 100, [Orpheus])
Enemy = NPC("TestDummy1", 200, 200, 20, 100, 100 ,100, "Enemy", [Cerberus])
Ally = NPC("TestAlly1", 200, 200, 20, 50, 100, 100, "Ally", [Penthesilea])

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
3 - Use Items
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
        print("not yet implemented")
        pass

      elif menu == "4":
          MainCharacter.switch_slots()
      elif menu == "5":
        print("Moving to the next battle...")
        break
      else:
        print("Please enter a valid input!")


def main():
  MainCharacter.character_selector(starting_characters)
  intermission()
  battle_loop(combatants)
  create_level2_combatants(MainCharacter)
  create_level3_combatants(MainCharacter)

if __name__ == "__main__":
    main()