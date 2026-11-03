from game import move_player, new_game, get_room_description


def new_game():


nickname = input("Enter your name: ")
player = new_game(nickname)

print(f"Welcome, {player['name']}! ")
print(get_room_description(player['location']))

loop = True

while loop:
    command = input("\What do you want to do? ").strip().lower()
   
    if command == "q" or command == "quit":
        print("Thanks for playing! Goodbye.")
        loop = False 
    # else:
    #     print("Invalid choice, try again.")
