#offsets?
LEVEL_OFFSET = 0
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
            #use actual gashapons received in levels.
            "Pac-Knight": 0,
            "Pac-Wizard": 1
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
            "Stopwatch": 2,
            "Small PAC-MAN": 3
        },
        "Missions":{
            "Collect All Fruits": 4,
            "Destroy Traps": 5,
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
            "Goal Coin": 4,
            "PAC-MAN (Silver)": 5
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
            "Help Island": 6,
            "Mega PAC-MAN": 7
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
            "Golden Cherry": 8,
            "Blinky (Gold)": 9
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
            "Pac-Buddy (Silver)": 10,
            "Killer Frog (Gold)": 11
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
            "Galaxian": 12,
            "Pac-Ranger (Silver)": 13
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
            "Golden Strawberry": 14,
            "Inky (Gold)": 15
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
            "PAC-MAN (Ice Skating)": 16,
            "Owl Mecha (Gold)": 17
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
            "Dot Chain": 18,
            "Pac-Sis (Silver)": 19
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
            "Golden Orange": 20,
            "Pinky (Gold)": 21
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
            "Pac-Mom (Silver)": 22,
            "Polar Bear Mecha (Gold)": 23
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
            "PAC-MAN (Diving)": 24,
            "Handy-Pac (Silver)": 25
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
            "Golden Apple": 26,
            "Clyde (Gold)": 27
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
            "Pac-Boy (Silver)": 28,
            "Spider Mecha (Gold)": 29
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
            "PAC-MAN (In-Line Skating)": 30,
            "Clie (Silver)": 31
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
            "Golden Melon": 32,
            "Professor Pac (Silver)": 33
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
            "Mega-Whale (Gold)": 34,
            "PAC-MAN (PAC-MAN MUSEUM+)": 35
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
        },
        "Missions": {

        }
    },
    "A Long Poisonous Tongue": {
        "id": 26,
        "Gashapons": {
        },
        "Missions": {

        }
    },
    "Harsh Harsh Winds": {
        "id": 27,
        "Gashapons": {
        },
        "Missions": {

        }
    },
    "Hunter of Darkness": {
        "id": 28,
        "Gashapons": {
        },
        "Missions": {

        }
    },
    "Pro Thunder Skater": {
        "id": 29,
        "Gashapons": {
        },
        "Missions": {

        }
    },
    "Boom! Boom! Clap!": {
        "id": 30,
        "Gashapons": {
        },
        "Missions": {

        }
    },
    "Hot! Fire Trouble": {
        "id": 31,
        "Gashapons": {
        },
        "Missions": {

        }
    },
    "Burning-Hot Beats": {
        "id": 32,
        "Gashapons": {
        },
        "Missions": {

        }
    },
    "Sharks Everywhere": {
        "id": 33,
        "Gashapons": {
        },
        "Missions": {

        }
    },
    "Pac-Marine Battle!": {
        "id": 34,
        "Gashapons": {
        },
        "Missions": {

        }
    },
    "Clumsy Bayou": {
        "id": 35,
        "Gashapons": {
        },
        "Missions": {

        }
    },
    "Legendary Story": {
        "id": 36,
        "Gashapons": {
        },
        "Missions": {

        }
    },
    "Flying Dark Shadow": {
        "id": 37,
        "Gashapons": {
        },
        "Missions": {

        }
    },
}