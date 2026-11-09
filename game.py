inventory = ['rope','water-bottle','map']

weapons = {
    "bare hands": 5,
    "wooden sword": 10,
    "metal dagger": 20
}

player = {
    "Energy": 50,
    "Location": "Beach",
    'inventory': inventory,
    'Weapon': 'wooden sword'
}

wild_beast = {
    "Name": "Wild Beast",
    "Hp": 30,
    "Max_Hp": 30,
    "Damage": 5,
    "Defeated": False
}

cave_monster = {
    "Name": "Cave Monster",
    "Hp": 50,
    "Max_Hp": 50,
    "Damage": 10,
    "Defeated": False
}

temple_guardian = {
    "Name": "Temple Guardian",
    "Hp": 100,
    "Max_Hp": 100,
    "Damage": 15,
    "Defeated": False
}

enemies = {
    "wild_beast": wild_beast,
    "cave_monster": cave_monster,
    "temple_guardian": temple_guardian
}
def fight_enemy(enemy, weapon_damage):

    if enemy['Defeated'] == True:
        print("Villain has already been defeated")
        return
    else:
        print("Villain is still alive")
        
    while enemy['Hp'] > 0 and player['Energy'] > 0:
        enemy['Hp'] = enemy['Hp'] - weapon_damage
        print(f"{enemy['Name']} you've only got {enemy['Hp']} Hp left!")
        if enemy['Hp'] <= 0:
            enemy['Defeated'] = True
            print(f"You defeated the {enemy['Name']}!")
            break
        if enemy['Hp'] > 0:
            print(f"{enemy['Name']} attacks the player!")
            player['Energy'] = player['Energy'] - enemy['Damage']
            print(f"Careful...you only have {player['Energy']} Energy left!")

        if player['Energy'] <= 0:
            
            print("Game over you have been defeated")
            break
player['Weapon'] = 'bare hands'
fight_enemy(cave_monster, weapons[player['Weapon']])
player['Energy'] = 50
fight_enemy(cave_monster, weapons[player['Weapon']])
print(cave_monster['Defeated'])
