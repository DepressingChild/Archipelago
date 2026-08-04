#offsets?
LEVEL_OFFSET = 0
GOLDEN_FRUIT_OFFSET = 100
KEY_OFFSET = 200
COSTUME_OFFSET = 300
FRUIT_SWITCH_OFFSET = 400
MOVEMENT_OFFSET = 500
#Some item to collect for goal

TIMETRIAL_OFFSET = 1000
MISSION_OFFSET = 2000
GASHAPON_OFFSET = 3000
GALAXIAN_OFFSET = 4000
CHERRY_OFFSET = 5000
STRAWBERRY_OFFSET = 6000
ORANGE_OFFSET = 7000
APPLE_OFFSET = 8000
MELON_OFFSET = 9000
FILLER_OFFSET = 20000

#Need to figure out how to hash fruits as unique items. Ignoring them for now.

#Level IDs are 1 less in game than here. ex: bear basics = 0

level_data = {
    "Pac-Village": {
        "id": 0,
        "Collectibles":{
           #"Cherries" : 26,
           #"Strawberries" : 29,
           #"Oranges" : 17,
           #"Apples" : 0,
           #"Melons" : 0,
           #"Galaxian" : 0
        },
        "Gashapons":{
        },
        "Missions":{
            "Collect All Fruit": 0
        }
    },
    "The Bear Basics": {
        "id": 1,
        "Collectibles":{
           #"Cherries" : 4,
           #"Strawberries" : 7,
           #"Oranges" : 3,
           #"Apples" : 7,
           #"Melons" : 4,
           #"Galaxian" : 0
        },
        "Gashapons":{
            "Orange Chest": 0,
            "Melon Chest": 1
        },
        "Missions":{
             #might need reworking
            "Clear Stage": 1,
            "Score 10,000": 2,
            "Collect All Fruits": 3
        }
    },
    "Canyon Chaos": {
        "id": 2,
        "Collectibles":{
           #"Cherries" : 4,
           #"Strawberries" : 2,
           #"Oranges" : 3,
           #"Apples" : 4,
           #"Melons" : 6,
           #"Galaxian" : 1
        },
        "Gashapons":{
            "Orange Chest": 2,
            "Melon Chest": 3
        },
        "Missions":{
            "Collect All Fruits": 4,
            "Destroy Bear Traps": 5,
            "Time Trial": 6
        }
    },
    "Pac-Dot Pond": {
        "id": 3,
        "Collectibles":{
           #"Cherries" : 0,
           #"Strawberries" : 0,
           #"Oranges" : 0,
           #"Apples" : 0,
           #"Melons" : 0,
           #"Galaxian" : 1
        },
        "Gashapons":{
            "Apple Chest": 4,
            "Melon Chest": 5
        },
        "Missions":{
            "Collect All Fruits": 7,
            "Defeat All Enemies": 8,
            "Time Trial": 9
        }
    },
    "Clyde's Frog": {
        "id": 4,
        "Collectibles":{},
        "Gashapons":{},
        "Missions":{
            "Don't Die": 10,
            "Time Trial": 11
        }
    },
    "B-Doing Woods": {
        "id": 5,
        "Gashapons":{
            "Strawberry Chest": 6,
            "Melon Chest": 7
        },
        "Missions":{
            "Collect All Fruits": 12,
            "Score 20,000": 13,
            "Time Trial": 14
        }
    },
    "Treewood Forest": {
        "id": 6,
        "Gashapons": {
            "Cherry Chest": 8,
            "Melon Chest": 9
        },
        "Missions": {
            "Collect All Fruits": 15,
            "Destroy Crates": 16,
            "Time Trial": 17
        }
    },
    "Butane Pain": {
        "id": 7,
        "Gashapons": {
            "Melon Chest": 10,
            "Strawberry Chest": 11
        },
        "Missions": {
            "Collect All Fruits": 18,
            "Defeat Enemies": 19,
            "Time Trial": 20
        }
    },
    "Inky's Whimsy": {
        "id": 8,
        "Gashapons": {},
        "Missions": {
            "Don't Die": 21,
            "Time Trial": 22
        }
    },
    "Ice River Run": {
        "id": 9,
        "Gashapons": {
            "Cherry Chest": 12,
            "Melon Chest": 13
        },
        "Missions": {
            "Collect All Fruits": 23,
            "Destroy Crates": 24,
            "Time Trial": 25
        }
    },
    "Avalanche Alley": {
        "id": 10,
        "Gashapons": {
            "Melon Chest": 14,
            "Strawberry Chest": 15
        },
        "Missions": {
            "Collect All Fruits": 26,
            "Defeat Enemies": 27,
            "Time Trial": 28
        }
    },
    "Blade Mountain": {
        "id": 11,
        "Gashapons": {
            "Orange Chest": 16,
            "Strawberry Chest": 17
        },
        "Missions": {
            "Collect All Fruits": 29,
            "Destroy Crates": 30,
            "Time Trial": 31
        }
    },
    "Pinky's Revenge": {
        "id": 12,
        "Gashapons": {},
        "Missions": {
            "Don't Die": 32,
            "Time Trial": 33
        }
    },
    "Into the Volcano!": {
        "id": 13,
        "Gashapons": {
            "Strawberry Chest": 18,
            "Melon Chest": 19
        },
        "Missions": {
            "Collect All Fruits": 34,
            "Never hang off an edge": 35, #Should maybe change to mention only in that one room.
            "Time Trial": 36
        }
    },
    "Volcanic Panic": {
        "id": 14,
        "Gashapons": {
            "Cherry Chest": 20,
            "Melon Chest": 21
        },
        "Missions": {
            "Collect All Fruits": 37,
            "Defeat Enemies": 38,
            "Time Trial": 39
        }
    },
    "Magma Opus": {
        "id": 15,
        "Gashapons": {
            "Strawberry Chest": 22,
            "Melon Chest": 23
        },
        "Missions": {
            "Collect All Fruits": 40,
            "Never fall down a slope": 41,
            "Time Trial": 42
        }
    },
    "Blinky in the Caldera": {
        "id": 16,
        "Gashapons": {},
        "Missions": {
            "Don't Die": 43,
            "Time Trial": 44
        }
    },
    "Scuba Duba": {
        "id": 17,
        "Gashapons": {
            "Strawberry Chest": 24,
            "Melon Chest": 25
        },
        "Missions": {
            "Collect All Fruits": 45,
            "Destroy Crates": 46,
            "Time Trial": 47
        }
    },
    "Shark Attack": {
        "id": 18,
        "Gashapons": {
            "Strawberry Chest": 26,
            "Melon Chest": 27
        },
        "Missions": {
            "Collect All Fruits": 48,
            "Never get caught by the Wild Shark": 49,
            "Time Trial": 50
        }
    },
    "Yellow Pac-Marine": {
        "id": 19,
        "Gashapons": {
            "Purple": 28,
            "Red": 29
        },
        "Missions": {
            "Collect All Fruits": 51,
            "Defeat Enemies": 52,
            "Don't Die": 53
        }
    },
    "Whale on a Sub": {
        "id": 20,
        "Gashapons": {},
        "Missions": {
            "Don't Die": 54,
            "Time Trial": 55
        }
    },
    "Haunted Boardwalk": {
        "id": 21,
        "Gashapons": {
            "Apple Chest": 30,
            "Melon Chest": 31
        },
        "Missions": {
            "Collect All Fruits": 56,
            "Score 11,000": 57,
            "Time Trial": 58
        }
    },
    "Night Crawling": {
        "id": 22,
        "Gashapons": {
            "Melon Chest": 32,
            "Strawberry Chest": 33
        },
        "Missions": {
            "Collect All Fruits": 59,
            "Destroy Crates": 60,
            "Time Trial": 61
        }
    },
    "Ghost Bayou": {
        "id": 23,
        "Gashapons": {
            "Apple Chest": 34,
            "Melon Chest": 35
        },
        "Missions": {
            "Collect All Fruits": 62,
            "Defeat Enemies": 63,
            "Time Trial": 64
        }
    },
    "Spooky": {
        "id": 24,
        "Gashapons": {},
        "Missions": {
            "Don't Die": 65,
            "Time Trial": 66
        }
    },
    "Deadly Poisonous Meadows": {
        "id": 25,
        "Gashapons": {
            "Apple Chest": 36,
            "Orange Chest": 37,
            "Melon Chest": 38
        },
        "Missions": {
            "Collect All Fruits": 67,
            "Destroy Bear Traps": 68,
            "Time Trial": 69
        }
    },
    "A Long Poisonous Tongue": {
        "id": 26,
        "Gashapons": {},
        "Missions": {
            "Don't Die": 70,
            "Time Trial": 71
        }
    },
    "Harsh Harsh Winds": {
        "id": 27,
        "Gashapons": {
            "Strawberry Chest": 39,
            "Orange Chest": 40,
            "Melon Chest": 41
        },
        "Missions": {
            "Collect All Fruits": 72,
            "Score 20,000": 73,
            "Time Trial": 74,
        }
    },
    "Hunter of Darkness": {
        "id": 28,
        "Gashapons": {},
        "Missions": {
            "Don't Die": 75,
            "Time Trial": 76
        }
    },
    "Pro Thunder Skater": {
        "id": 29,
        "Gashapons": {
            "Strawberry Chest": 42,
            "Orange Chest": 43,
            "Melon Chest": 44
        },
        "Missions": {
            "Collect All Fruits": 77,
            "Destroy Crates": 78,
            "Time Trial": 79
        }
    },
    "Boom! Boom! Clap!": {
        "id": 30,
        "Gashapons": {},
        "Missions": {
            "Don't Die": 80,
            "Time Trial": 81
        }
    },
    "Hot! Fire Trouble": {
        "id": 31,
        "Gashapons": {
            "Cherry Chest": 45,
            "Apple Chest": 46,
            "Melon Chest": 47
        },
        "Missions": {
            "Collect All Fruits": 82,
            "Score 25,000": 83,
            "Time Trial": 84
        }
    },
    "Burning-Hot Beats": {
        "id": 32,
        "Gashapons": {},
        "Missions": {
            "Don't Die": 85,
            "Time Trial": 86
        }
    },
    "Sharks Everywhere": {
        "id": 33,
        "Gashapons": {
            "Orange Chest": 48,
            "Strawberry Chest": 49,
            "Melon Chest": 50
        },
        "Missions": {
            "Collect All Fruits": 87,
            "Score 24,000": 88,
            "Time Trial": 89
        }
    },
    "Pac-Marine Battle!": {
        "id": 34,
        "Gashapons": {},
        "Missions": {
            "Don't Die": 90,
            "Time Trial": 91
        }
    },
    "Clumsy Bayou": {
        "id": 35,
        "Gashapons": {
            "Orange Chest": 51,
            "Apple Chest": 52,
            "Melon Chest": 53
        },
        "Missions": {
            "Collect All Fruits": 92,
            "Defeat Enemies": 93,
            "Time Trial": 94
        }
    },
    "Legendary Story": {
        "id": 36,
        "Gashapons": {},
        "Missions": {
            "Don't Die": 95,
            "Time Trial": 96
        }
    },
    "Flying Dark Shadow": {
        "id": 37,
        "Gashapons": {},
        "Missions": {
            "Don't Die": 97,
            "Time Trial": 98
        }
    },
}

golden_fruit_data = {
    "Golden Cherry": 0,
    "Golden Strawberry": 1,
    "Golden Apple": 2,
    "Golden Orange": 3,
    "Golden Melon": 4
}

key_data = {
    "Windy Woods Key": 0,
    "Thunder Snow Mountain Key": 1,
    "Fiery Caverns Key": 2,
    "Dim Underwaters Key": 3,
    "Ghost Island Key": 4
}

costume_data = {
    "Hunter (Green)": 1,
    "Hunter (Brown)": 2,
    "Hunter (Blue)": 3,
    "Street (Blue)": 4,
    "Street (Red)": 5,
    "Street (Pink)": 6,
    "Cowboy (Brown)": 7,
    "Cowboy (Red)": 8,
    "Cowboy (Pink)": 9,
    "Ushanka (Brown)": 10,
    "Ushanka (Red)": 11,
    "Ushanka (Blue)": 12,
    "Explorer (White)": 13,
    "Explorer (Green)": 14,
    "Explorer (Pink)": 15,
    "Diver (Blue)": 16,
    "Diver (Green)": 17,
    "Diver (Pink)": 18,
    "Blinky": 19,
    "Inky": 20,
    "Clyde": 21,
    "Pinky": 22,
    "Magician (Black)": 23,
    "Magician (Purple)": 24,
    "Magician (Green)": 25,
    "Pac-Knight": 26,
    "Toc-Man": 27, #Do we remove this because you need re-pac 1?
    "Pac-Wizard": 28,
    "Orson": 29,
    "Pac-Land": 30, #Do we remove this because pre-order bonus?
    "Spooky": 31,
    #No sonic dlc for you
    "Holiday (Red)": 33,
    "Holiday (Green)": 34,
    "Holiday (Blue)": 35,
    "Birthday Hat": 36
}

fruit_switch_data = {
    "Cherry Switch": 0,
    "Strawberry Switch": 1,
    "Orange Switch": 2,
    "Apple Switch": 3,
    "Melon Switch": 4
}

movement_data = {
    "Progressive Butt Bounce": 0,
    "Flip Kick": 1,
    "Rev Roll": 2,
    "Pac-Dot Attack": 3,
    "Flutter": 4
}
