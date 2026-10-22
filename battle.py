from classes import Character, Player, Skill

#MainCharacter will use the Player class instead of jsut character so they have SP and Personas
player = Player(name="Prog", maxhp=300, currenthp=150, defense=20, maxsp=100, cursp=100, personas=[])

#sample enemy
enemy = Character(name="Shadow Shadow", maxhp=200, currenthp=200, defense=10, maxsp= 200, cursp= 100, personas = [])

#create some skills
Agi = Skill("Fire", "Agi", 3, 40, 1)
Bufu = Skill("Ice", "Bufu", 4, 40, 1, "Freeze", 0.15)


def battle_loop():
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

    #PLAYER TURN
    print("Choose an action:")
    print("1. Basic Attack")
    print("2. Use Skill (Agi)")
    print("3. Guard")

    choice = input("Enter choice (1-3): ")

    if choice == "1":
      #basic attack logic
      damage = 25  #placeholder for base attack calculation
      enemy.curhp -= damage
      print(f"{player.name} attacks {enemy.name} for {damage} physical damage!")

    elif choice == "2":
      #skill logic
      skill_to_use = Agi
      if player.use_skill(skill_to_use):
        player.cursp -= skill_to_use.cost
        enemy.curhp -= skill_to_use.effect
        print(
            f"{player.name} casts {skill_to_use.name} for"
            f" {skill_to_use.cost} SP!"
        )
        print(f"It deals {skill_to_use.effect} {skill_to_use.element} damage!")
      else:
        print("Not enough SP! Turn wasted.")

    elif choice == "3":
      print(f"{player.name} takes a defensive stance! (Guard active)")
      #add guard logic here (e.g., temporary defense boost and calculation)

    else:
      print("Invalid choice, turn skipped!")

    #CHECK IF ENEMY IS DEFEATED
    if enemy.curhp <= 0:
      print(f"\n🎉 Victory! {enemy.name} has been defeated!")
      battle_active = False
      break

    #ENEMY TURN
    print(f"\n--- {enemy.name}'s Turn ---")
    enemy_damage = 20  #placeholder enemy attack
    #factor in player defense if you want: max(1, enemy_damage - player.defense)
    actual_damage = max(1, enemy_damage - player.defense)
    player.curhp -= actual_damage
    print(
        f"{enemy.name} strikes back, dealing {actual_damage} damage to"
        f" {player.name}!"
    )

    #CHECK IF PLAYER IS DEFEATED
    if player.curhp <= 0:
      print(f"\n💀 Game Over... {player.name} fell in battle.")
      battle_active = False
      break

    turn_counter += 1

if __name__ == "__main__":
    battle_loop()