from classes import Character, Player, Persona

def get_agility(character):
  return character.equipped_persona.agility

def calculate_turn_order(combatants: list):
  alive_combatants = [character for character in combatants if character.curhp > 0]
  return sorted(alive_combatants, key=get_agility,reverse=True)

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

    for turn in order:
      if type(turn) == Player:
        # PLAYER TURN
        print(f"\n--- {player.name}'s Turn ---")
        print("Choose an action:")
        print("1. Basic Attack")
        print("2. Use Skill")
        print("3. Guard")

        choice = input("Enter choice (1-3): ")

        if choice == "1":
          #basic attack logic
          damage = 25  #placeholder for base attack calculation
          enemy.curhp -= damage
          print(f"{player.name} attacks {enemy.name} for {damage} physical damage!")

        elif choice == "2":
          #skill logic
          for index, skill in enumerate(player.equipped_persona.skills):
            print(f"{index+1}. {skill.name}")

          selection = int(input("Please select a skill\n"))
          skill_to_use = player.equipped_persona.skills[selection-1]
          if player.use_skill(skill_to_use):
            player.cursp -= skill_to_use.cost
            enemy.curhp -= skill_to_use.effect
            print(f"{player.name} casts {skill_to_use.name} for"
                f" {skill_to_use.cost} SP!")
            print(f"It deals {skill_to_use.effect} {skill_to_use.element} damage!")
          else:
            print("Not enough SP! Turn wasted.")

        elif choice == "3":
          print(f"{player.name} takes a defensive stance! (Guard active)")
          #add guard logic here (e.g., temporary defense boost and calculation)
        else:
          print("Invalid choice, turn skipped!")

        # CHECK IF ENEMY IS DEFEATED
        if enemy.curhp <= 0:
          print(f"\n🎉 Victory! {enemy.name} has been defeated!")
          battle_active = False
          break

      else:
        # ENEMY TURN
        print(f"\n--- {enemy.name}'s Turn ---")
        skill_to_use = random.choice(enemy.equipped_persona.skills)
        if enemy.use_skill(skill_to_use):
          enemy.cursp -= skill_to_use.cost
          player.curhp -= skill_to_use.effect
          print(f"{enemy.name} casts {skill_to_use.name} for"
                f" {skill_to_use.cost} SP!")
          print(f"It deals {skill_to_use.effect} {skill_to_use.element} damage!")

        else:
          print("Not enough SP! Turn wasted.")
        # CHECK IF PLAYER IS DEFEATED
        if player.curhp <= 0:
          print(f"\n💀 Game Over... {player.name} fell in battle.")
          battle_active = False
          break

    turn_counter += 1

if __name__ == "__main__":
    battle_loop()