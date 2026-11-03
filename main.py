from game import new_game, get_room_description

nickname = input("Enter your name: ")

print(f"Welcome, {nickname}! ")

loop = True

while loop:
    menu_choice = input("1. Look around | q. Quit: ").strip().lower()
    
    if menu_choice == "1":
        print("You look around the beach. The waves crash softly.")
    elif menu_choice == "q":
        print("Thanks for playing! Goodbye.")
        loop = False 
    else:
        print("Invalid choice, try again.")
