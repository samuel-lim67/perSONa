from battle import battle_loop
from classes import Character, Persona, Player, Skill

def run_level():
  print("\n==========================================")
  print("      LEVEL 1: THE AWAKENING GATE         ")
  print("==========================================")
  print(
      "Story: Makoto awakens his initial power just as shadows breach the"
      " dormitory threshold."
  )

  #1. Create Skills for Level 1
  slash_skill = Skill(
      element="Slash", name="Cleave", cost=3, effect=30, targets=1
  )

  #2. Create Personas
  orpheus = Persona(
      name="Orpheus", arcana="Fool", agility=10, skills=[slash_skill]
  )
  brave_hand_persona = Persona(
      name="Shadow Core", arcana="Chariot", agility=6, skills=[slash_skill]
  )

  #3. Create Player & Enemy
  player = Player(
      name="Makoto Yuki",
      maxhp=100,
      currenthp=100,
      defense=5,
      maxsp=30,
      cursp=30,
      personas=[orpheus],
  )
  player.equipped_persona = orpheus

  enemy = Player(
      name="Brave Hand",
      maxhp=60,
      currenthp=60,
      defense=3,
      maxsp=20,
      cursp=20,
      personas=[brave_hand_persona],
  )
  enemy.equipped_persona = brave_hand_persona

  combatants = [player, enemy]

  battle_loop(player, enemy)

  if player.curhp > 0:
    print(
        "\n[LEVEL 1 COMPLETE] The dormitory breach is secured. You earned 30"
        " EXP!"
    )
    return True
  else:
    print("\n[LEVEL 1 FAILED] The shadows overwhelmed the dormitory...")
    return False


if __name__ == "__main__":
  run_level()

