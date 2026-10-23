from classes import Character, Player, Persona, NPC
import random

def alive_characters(combatants):
    alive_combatants = [character for character in combatants if character.curhp > 0]
    return alive_combatants

def calculate_turn_order(living_combatants):
    personas = {}
    for character in living_combatants:
        for persona in character.personas:
            personas[persona] = character
    sorted_order = sorted(list(personas), key=Persona.get_agility, reverse=True)
    move_order = []
    for persona in sorted_order:
        pair = (persona, personas[persona])
        move_order.append(pair)
    return move_order


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
                user.player_turn(enemies, persona)

                # CHECK IF ENEMY IS DEFEATED
                if enemy.curhp <= 0:
                    print(f"\n🎉 Victory! {enemy.name} has been defeated!")
                    battle_active = False
                    break

            else:
                if user.classification == "Enemy":
                    # ENEMY TURN
                    user.enemy_turn(persona, allies)
                    # CHECK IF PLAYER IS DEFEATED
                    if player.curhp <= 0:
                        print(f"\n💀 Game Over... {player.name} fell in battle.")
                        battle_active = False
                        break
                elif user.classification == "Ally":
                    pass

        turn_counter += 1


if __name__ == "__main__":
    battle_loop()
