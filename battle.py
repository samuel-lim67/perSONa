from classes import Character, Player, Persona
import random

def get_agility(persona):
  return persona.agility

def calculate_turn_order(combatants: list):
  alive_combatants = [character for character in combatants if character.curhp > 0]
  personas = {}
  for character in alive_combatants:
    for persona in character.personas:
      personas[persona] = character
  sorted_order = sorted(list(personas), key=get_agility, reverse=True)
  move_order = []
  for persona in sorted_order:
    pair = (persona, personas[persona])
    move_order.append(pair)
  return move_order

  #return sorted(alive_combatants, key=get_agility,reverse=True)

def player_turn(player, enemy, persona):
  # PLAYER TURN
  print(f"\n--- {player.name}'s Turn ---")
  print(f"Current Persona: {persona.name}")
  print("Choose an action:")
  print("1. Basic Attack")
  print("2. Use Skill")
  print("3. Guard")

  choice = input("Enter choice (1-3): ")

  if choice == "1":
    # basic attack logic
    damage = 25  # placeholder for base attack calculation
    enemy.curhp -= damage
    print(f"{player.name} attacks {enemy.name} for {damage} physical damage!")

  elif choice == "2":
    # skill logic
    for index, skill in enumerate(persona.skills):
      print(f"{index + 1}. {skill.name}")

    selection = int(input("Please select a skill\n"))
    skill_to_use = persona.skills[selection - 1]
    if player.use_skill(skill_to_use):
      enemy.curhp -= skill_to_use.effect
      print(f"{player.name} casts {skill_to_use.name} for"
            f" {skill_to_use.cost} SP!")
      print(f"It deals {skill_to_use.effect} {skill_to_use.element} damage!")
    else:
      print("Not enough SP! Turn wasted.")

  elif choice == "3":
    print(f"{player.name} takes a defensive stance! (Guard active)")
    # add guard logic here (e.g., temporary defense boost and calculation)
  else:
    print("Invalid choice, turn skipped!")

def enemy_turn(player, enemy, persona):
  print(f"\n--- {enemy.name}'s Turn ---")
  print(f"Current Persona: {persona.name}")
  skill_to_use = random.choice(persona.skills)
  if enemy.use_skill(skill_to_use):
    player.curhp -= skill_to_use.effect
    print(f"{enemy.name} casts {skill_to_use.name} for"
          f" {skill_to_use.cost} SP!")
    print(f"It deals {skill_to_use.effect} {skill_to_use.element} damage!")

  else:
    print("Not enough SP! Turn wasted.")

def battle_loop(player, enemy):
  print(f"--- BATTLE START: {player.name} vs {enemy.name} ---")
  battle_active = True
  turn_counter = 1
  while battle_active:
    print(f"\n=================== TURN {turn_counter} ===================")
    print(
        f"{player.name} HP: {player.curhp}/{player.maxhp} | SP:"
        f" {player.cursp}/{player.maxsp}"
    )
    print(f"{enemy.name} HP: {enemy.curhp}/{enemy.maxhp}")
    print("---------------------------------------------------")

    order = calculate_turn_order([player, enemy])

    for persona, user in order:
      if type(user) == Player:
        # PLAYER TURN
        player_turn(player, enemy, persona)

        # CHECK IF ENEMY IS DEFEATED
        if enemy.curhp <= 0:
          print(f"\n🎉 Victory! {enemy.name} has been defeated!")
          battle_active = False
          break

      else:
        # ENEMY TURN
        enemy_turn(player, enemy, persona)
        # CHECK IF PLAYER IS DEFEATED
        if player.curhp <= 0:
          print(f"\n💀 Game Over... {player.name} fell in battle.")
          battle_active = False
          break

    turn_counter += 1

if __name__ == "__main__":
    battle_loop()