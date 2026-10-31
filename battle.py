from classes import Character, Player, Persona, NPC
import random

def alive_characters(combatants):
    alive_combatants = [character for character in combatants if character.curhp > 0]
    return alive_combatants

def calculate_turn_order(living_combatants):
    personas = []

    for character in living_combatants:
        for persona in character.personas:
            personas.append((persona, character))
    sorted_order = sorted(personas, key=Persona.get_agility, reverse=True)
    return sorted_order

def sort_combatants(combatants):
    allies = []
    enemies = []
    for combatant in combatants:
        if type(combatant) != Player:
            if combatant.classification == "Enemy":
                enemies.append(combatant)
            else:
                allies.append(combatant)
        else:
            allies.append(combatant)
    return allies, enemies

def battle_loop(combatants):
    print(f"--- BATTLE START ---")
    allies, enemies = sort_combatants(combatants)
    battle_active = True
    turn_counter = 1
    while battle_active:
        print(f"\n=================== TURN {turn_counter} ===================")
        print("===ALLIES===")
        for ally in allies:
            print(f"{ally.name} HP: {round(ally.curhp)}/{ally.maxhp} | SP:{ally.cursp}/{ally.maxsp} | Status Effects: {ally.status_effect}" )
        print("===ENEMIES===")
        for enemy in enemies:
            print(f"{enemy.name} HP: {round(enemy.curhp,1)}/{enemy.maxhp} | SP:{enemy.cursp}/{enemy.maxsp} | Status Effects: {enemy.status_effect}")
        print("---------------------------------------------------")

        living_combatants = alive_characters(combatants)
        order = calculate_turn_order(living_combatants)

        for persona, user in order:

            if user.curhp <= 0:
                print(f"{user.name} is down.")
                continue

            if user.knocked_down:
                user.knocked_down = False
                print(f"\n{user.name} gets back up!")

            if type(user) == Player:
                # PLAYER TURN
                if not alive_characters(enemies):
                    print(f"\n🎉 Victory! All enemies have been defeated!")
                    battle_active = False
                    return "Win"

                user.player_turn(enemies, persona)

                # CHECK IF ENEMIES ARE DEFEATED
                if not alive_characters(enemies):
                    print(f"\n🎉 Victory! All enemies have been defeated!")
                    battle_active = False
                    return "Win"

            else:
                if user.classification == "Enemy":
                    # ENEMY TURN
                    if not alive_characters(allies):
                        print(f"\n💀 Game Over... your whole party has fainted.")
                        battle_active = False
                        return "Lose"

                    user.npc_turn(persona, allies)
                    # CHECK IF NO ALLIES ARE ALIVE
                    if not alive_characters(allies):
                        print(f"\n💀 Game Over... your whole party has fainted.")
                        battle_active = False
                        return "Lose"
                elif user.classification == "Ally":
                    # ALLY TURN

                    if not alive_characters(enemies):
                        print(f"\n🎉 Victory! All enemies have been defeated!")
                        battle_active = False
                        return "Lose"

                    user.npc_turn(persona, enemies)

                    if not alive_characters(enemies):
                        print(f"\n🎉 Victory! All enemies have been defeated!")
                        battle_active = False
                        return "Lose"

        turn_counter += 1
    return None

if __name__ == "__main__":
    battle_loop()
