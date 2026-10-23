from classes import Character, Player, Persona
import random

def get_agility(persona):
  return persona.agility

def alive_characters(combatants):
  alive_combatants = [character for character in combatants if character.curhp > 0]
  return alive_combatants

def calculate_turn_order(living_combatants):
  personas = {}
  for character in living_combatants:
    for persona in character.personas:
      personas[persona] = character
  sorted_order = sorted(list(personas), key=get_agility, reverse=True)
  move_order = []
  for persona in sorted_order:
    pair = (persona, personas[persona])
    move_order.append(pair)
  return move_order

  #return sorted(alive_combatants, key=get_agility,reverse=True)

def target_selector(enemies):
  alive_enemies = alive_characters(enemies)
  for index, enemy in enumerate(alive_enemies):
    print(f"{index+1} - {enemy.name}")
  print(f"{len(alive_enemies)+1 } - Back")
  while True:
    try:
      selection = int(input("Who would you like to attack?\n"))

      if 1 <= selection <= len(alive_enemies):
        return alive_enemies[selection-1]
      elif selection == (len(alive_enemies)+1):
        return None
      else:
        print("Please select a valid target!")
    except ValueError:
      print("Please enter a valid input!")

def player_turn(player, enemies, persona):
  # PLAYER TURN
  print(f"\n--- {player.name}'s Turn ---")
  while True:
    print(f"Current Persona: {persona.name}")
    print("Choose an action:")
    print("1. Basic Attack")
    print("2. Use Skill")
    print("3. Guard")

    choice = input("Enter choice (1-3): ")

    if choice == "1":
      # basic attack logic
      damage = 25  # placeholder for base attack calculation
      target = target_selector(enemies)
      if target:
        target.curhp -= damage
        print(f"{player.name} attacks {target.name} for {damage} physical damage!")
      elif not target: #if the player wants to back out and go back to the action menu
        pass

    elif choice == "2":
      # skill logic
      while True:
        for index, skill in enumerate(persona.skills):
          print(f"{index + 1} - {skill.name}")
        print(f"{len(persona.skills)+1} - Back)
        try:
          selection = int(input("Please select a skill\n"))
        except ValueError:
          print("Please enter a valid input!")
          continue
        else:
          if 1 <= selection <= len(persona.skills):
            skill_to_use = persona.skills[selection - 1]
            if player.use_skill(skill_to_use):
              target = target_selector(enemies)
              if target is None:
                break
              else:
                player.cursp -= skill_to_use.cost
                target.curhp -= skill_to_use.effect
                print(f"{player.name} casts {skill_to_use.name} for"
                      f" {skill_to_use.cost} SP!")
                print(f"It deals {skill_to_use.effect} {skill_to_use.element} damage!")
                break
            else:
              print("Not enough SP!")
          elif selection == (len(persona.skills)+1):
            break
          else:
            print("Please enter a valid input!")

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
  allies = [player]
  enemies = [enemy]
  combatants = allies + enemies
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

    living_combatants = alive_characters(combatants)
    order = calculate_turn_order(living_combatants)

    for persona, user in order:
      if user.curhp <= 0:
        continue

      elif type(user) == Player:
        # PLAYER TURN
        player_turn(player, enemies, persona)

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