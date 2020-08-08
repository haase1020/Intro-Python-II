from room import Room
from player import Player
from room_info import room_info

room_map = room_info()

name = input("Please enter your name to get started on your journey:  ")
player = Player(name, room_map["outside"])
print(f"{player.name}, you are currently at {player.room.name}")


while True:
    print(
        f" you are currently at {player.room.name}, {player.room.description}")

    user_input = input(
        "Please choose from the following to play: 1) move in directions n,s,e,w 2) p for pickup 3) q for quit   ")

    if user_input.lower() in ['n', 's', 'e', 'w']:
        if player.room.connections is not None:
            player.move(user_input)
            print("You are now in ", player.room.name)
            print("Items in this room are: ", player.room.items)
        else:
            print("You have reached a dead end")
    elif user_input.lower() == 'p':
        item_check = input("what item will you choose? ")
        player.pickup(item_check)
    elif user_input.lower() == 'q':
        print("Thank you for playing!")
        break

    else:
        print("Do not understand your input. Please enter a valid command or press q to quit. ")
