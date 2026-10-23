from battle import battle_loop
from classes import Character, Persona, Player, Skill, Orpheus, Arsene, Izanagi
from selection import character_selector


print("\n==========================================")
print("      LEVEL 1: LEARNING COMBAT         ")
print("==========================================")

# 1. Initialize Player
player = Player("Protagonist", maxhp=100, currenthp=100, defense=5, maxsp=40, cursp=40, personas=[])
    
# Starting Persona Selection
starter_choices = [Orpheus, Arsene, Izanagi]
character_selector(starter_choices, player)
player.equipped_persona = player.personas[0]

# 2. Setup Enemy (Enemy1)
slash_skill = Skill("Slash", "Cleave", 0, 20, 1)
enemy1_persona = Persona("Malice_Core", [slash_skill], {}, 1, 1, 1, 2, 1)
enemy = Character("Enemy1", maxhp=60, currenthp=60, defense=2, maxsp=20, cursp=20, personas=[enemy1_persona])
enemy.equipped_persona = enemy1_persona

# 3. Trigger Battle Loop
combantants = [player, enemy]
battle_loop(player, enemy)


