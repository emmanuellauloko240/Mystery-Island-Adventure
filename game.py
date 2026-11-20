import json

inventory = ['rope','water-bottle','map']

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

player = {
    "Energy": 50,
    "Location": "Forest",
    'inventory': inventory,
    'Weapon': 'wooden sword'
}


enemies = {
    "wild_beast": wild_beast,
    "cave_monster": cave_monster,
    "temple_guardian": temple_guardian
}

game_data = {
    "player": player, 
    "enemies": enemies
}

def save_game():
    with open("save_game.json","w") as file:
        json.dump(game_data,file)

def load_game():
    try:
        with open("save_game.json", "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("No saved game found starting a new game...")
        return game_data
choice = input("1. Continue game\n2. Start new game\nEnter your choice: ")
while choice not in ['1', '2']:
    choice = input("Invalid choice! Enter 1 or 2: ")
if choice == '1':
    data = load_game()
    player.update(data["player"])
    wild_beast.update(data["enemies"]["wild_beast"])
    cave_monster.update(data['enemies']['cave_monster'])
    temple_guardian.update(data['enemies']['temple_guardian'])


elif choice == '2':
    print("Starting a new game...")
    player['Energy'] = 50
    player['Location'] = 'Forest'
    player['Weapon'] = 'wooden sword'
    player['inventory'] = ['rope', 'water-bottle', 'map']


    wild_beast.update({
        "Hp": 30,
        "Defeated": False
    })

    cave_monster.update({
        "Hp": 50,
        "Defeated": False
    })

    temple_guardian.update({
        "Hp": 100,
        "Defeated": False
    })

else:
    print("Invalid choice!")


weapons = {
    "bare hands": 5,
    "wooden sword": 10,
    "metal dagger": 20
}

location_enemies = {
    "Forest": wild_beast,
    "Cave": cave_monster,
    "Temple": temple_guardian
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
            if player['Energy'] >= enemy['Damage']:
                print(f"{enemy['Name']} attacks the player!")
                player['Energy'] = player['Energy'] - enemy['Damage']
                print(f"Careful...you only have {player['Energy']} Energy left!")
            else:            
                print("Game over you have been defeated")
                break
print("Where would you like to go?")
print("1. Forest")
print("2. Cave")
print("3. Temple")

destination = input("Choose your destination: ")

if destination in ['1', '2', '3'] and player['Energy'] >= 10:

    if destination == '1':
        player['Location'] = 'Forest'
    elif destination == '2':
        player['Location'] = 'Cave'
    elif destination == '3':
        player['Location'] = 'Temple'

    player['Energy'] = player['Energy'] - 10

else:
    print("You cannot travel!")
    
print(player['Location'])

if player['Location'] in location_enemies:
    enemy = location_enemies[player['Location']]
    fight_enemy(enemy, weapons[player['Weapon']])
    save_game()
else:
    print("No enemies here you can rest and explore")


# fight_enemy(enemy,weapon_damage)
