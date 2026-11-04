
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

    player["Energy"] = player["Energy"] - 10

    player["Location"] = "Cave"

    print(player)


def move_player(destination):

    if  player["Energy"] >= 10:

        player["Energy"] = player["Energy"] - 10

        player["Location"] = destination         
    else:
        print("Not enough energy to travel!")
