
# def new_game(player_name):
#     return{
#         'name': player_name,
#         'location': 'Beach',
#         'energy': 5,
#         'inventory': [],
#         'game_over': False,
#         'won': False
#     }
# def get_room_description(location):
#     if location == 'Beach':
#         return("You wake up on a sandy beach after a fierce storm. The sky is grey, and the lighthouse looms in the distance.")

# map = {
#     "Beach": {"north": "Jungle"},
#     "Jungle": {"south": "Beach", "north": "Cave"},
#     "Cave": {"south": "Jungle", "east": "Old Bridge"},
#     "Old Bridge": {"west": "Cave", "east": "Lighthouse"},
#     "Lighthouse": {"west": "Old Bridge"}
# }


# def move_player(player, direction):
#     current_room = player['location']
#     if direction in map[current_room]:
#         player['location'] = map[current_room][direction]
#         return True
#     elif direction not in map[current_room]:
#         return False

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
def fight_enemy(enemy):
    while enemy['Hp'] > 0 and player['Energy'] > 0:
        enemy['Hp'] = enemy['Hp'] - 10
        print(f"{enemy['Name']} you've only got {enemy['Hp']} Hp left!")
    if enemy['Hp'] <= 0:
        print(f"You defeated the {enemy['Name']}!")
        break
    if enemy['Hp'] > 0:
        print(f"{enemy['Name']} attacks the player!")
    player['Energy'] = player['Energy'] - enemy['Damege']

    print("Game Over!")
    break
    
if enemies['wild_beast']['Hp'] <= 0:
    print("Wild Beast defeated!")

while enemies['wild_beast']['Hp'] > 0 and player['Energy'] > 0:
    
    enemies['wild_beast']['Hp'] = enemies['wild_beast']['Hp'] - 10

    print(f"Wild Beast Hp: {enemies['wild_beast']['Hp']}")
    if enemies['wild_beast']['Hp'] <= 0:
        print("Wild Beast defeated!")
        break
    if enemies['wild_beast']['Hp'] > 0:
        print('Wild Beast attacks the player!')
        player['Energy'] = player['Energy'] - enemies['wild_beast']['Damage']
        
    if player['Energy'] <= 0:
        print("Game over! You have been defeated.")
        break


def move_player(destination):

    if  player["Energy"] >= 10:

        player["Energy"] = player["Energy"] - 10

        player["Location"] = destination         
    else:
        print("Not enough energy to travel!")
