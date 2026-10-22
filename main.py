from classes import Character, Player, Skill, Orpheus, Arsene, Izanagi
from battle import battle_loop
from selection import character_selector

MainCharacter = Player("Prog", 300, 150, 20, 100, 100, [])
starting_characters = [Orpheus, Arsene, Izanagi]
def intermission():
  progress_game = input(f"""
====================INTERMISSION====================
Are you ready to enter the next battle?
(Y/N)
""")
  if progress_game.lower().strip() == "y":
    return
  else:
    while True:
      menu = input(f"""
What would you like to do?
1 - Inspect
2 - Use Items
3 - Next Battle
""")
      if menu == "1":
        print(f"""
Name: {MainCharacter.name}
HP: {MainCharacter.curhp}/{MainCharacter.maxhp}
Skill Points: {MainCharacter.cursp}/{MainCharacter.maxsp}
Personas: {', '.join(persona.name for persona in MainCharacter.personas)}""")

def main():
  character_selector(starting_characters, MainCharacter)
  intermission()
  battle_loop()

if __name__ == "__main__":
    main()