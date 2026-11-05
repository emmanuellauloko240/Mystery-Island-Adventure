inventory = ['rope','water-bottle','map']
player = {
    "Energy": 50,
    "Location": "Beach",
    'inventory': inventory
}

wild_beast = {
    "Name": "Wild Beast",
    "Hp": 30,
    "Damage": 5
}

cave_monster = {
    "Name": "Cave Monster",
    "Hp": 50,
    "Damage": 10
}

temple_guardian = {
    "Name": "Temple Guardian",
    "Hp": 100,
    "Damage": 15
}

enemies = {
    "wild_beast": wild_beast,
    "cave_monster": cave_monster,
    "temple_guardian": temple_guardian
}
def fight_enemy(enemy, weapon_damage):
    while enemy['Hp'] > 0 and player['Energy'] > 0:
        enemy['Hp'] = enemy['Hp'] - weapon_damage
        print(f"{enemy['Name']} you've only got {enemy['Hp']} Hp left!")
        if enemy['Hp'] <= 0:
            print(f"You defeated the {enemy['Name']}!")
            break
        if enemy['Hp'] > 0:
            print(f"{enemy['Name']} attacks the player!")
            player['Energy'] = player['Energy'] - enemy['Damage']
            print(f"Careful...you only have {player['Energy']} Energy left!")

        if player['Energy'] <= 0:
            print("Game over you have been defeated")
            break
fight_enemy(wild_beast, 10)