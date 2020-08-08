from room import Room


def room_info():
    room_map = {
        'outside':  Room("the outside of Lambda School",
                         "The only way to enter is go go up."),

        'foyer':    Room("the Foyer", """You have made it inside. You see light streaming
from both north and east."""),

        'overlook': Room("the Balcony", """You can see a beautiful view of trees and nature, but no diary. Ahead to the north you see a light, but there is no way to get there. 
        You must go back to the foyer."""),

        'narrow':   Room("the Narrow Passage", """The narrow passage bends here from west
to north. The smell of musty paper that could be a notebook permeates the air."""),

        'treasure': Room("the Treasure Chamber", """You've found the missing diary! You have found the missing password to unlock access to the best
        website in the world and thus landed yourself a job at Google. Way to go tech stud!"""),
    }


# Link rooms together

    room_map['outside'].connections["n"] = room_map['foyer']
    room_map['foyer'].connections["s"] = room_map['outside']
    room_map['foyer'].connections["n"] = room_map['overlook']
    room_map['foyer'].connections["e"] = room_map['narrow']
    room_map['overlook'].connections["s"] = room_map['foyer']
    room_map['narrow'].connections["w"] = room_map['foyer']
    room_map['narrow'].connections["n"] = room_map['treasure']
    room_map['treasure'].connections["s"] = room_map['narrow']

    return room_map
