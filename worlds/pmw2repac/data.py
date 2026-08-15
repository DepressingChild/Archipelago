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
FILLER_OFFSET = 10000
TRAP_OFFSET = 11000

#Need to figure out how to hash fruits as unique items. Ignoring them for now.

#Level IDs are 1 less in game than here. ex: bear basics = 0

level_data = {
    "Pac-Village": {
        "id": 0,
        "Collectibles": {
           #"Cherries" : 26,
           #"Strawberries" : 29,
           #"Oranges" : 17,
           #"Apples" : 0,
           #"Melons" : 0,
           "Galaxian": {}
        },
        "Gashapons": {},
        "Missions": {
            "Collect All Fruits":{
                "id": 0,
                "fm_rules": "sbb&fk | sbb&dt",
                "am_rules": "sbb&rr",
                "ag_rules": ""
            }
        }
    },
    "The Bear Basics": {
        "id": 1,
        "Clear": {
            "fm_rules": "bb",
            "am_rules": "",
            "ag_rules": ""
        },
        "Collectibles": {
           #"Cherries" : 4,
           #"Strawberries" : 7,
           #"Oranges" : 3,
           #"Apples" : 7,
           #"Melons" : 4,
           "Galaxian": {}
        },
        "Gashapons": {
            "Orange Chest": {
                "id": 0,
                "fm_rules": "bb",
                "am_rules": "",
                "ag_rules": ""
            },
            "Melon Chest": {
                "id": 1,
                "fm_rules": "bb&fk | bb&dt",
                "am_rules": "",
                "ag_rules": ""
            }
        },
        "Missions": {
             #might need reworking
            "Clear Stage": {
                "id": 1,
                "fm_rules": "bb",
                "am_rules": "",
                "ag_rules": ""
            },
            "Score 10,000": {
                "id": 2,
                "fm_rules": "bb",
                "am_rules": "",
                "ag_rules": ""
            },
            "Collect All Fruits": {
                "id": 3,
                "fm_rules": "sbb&fk | sbb&dt",
                "am_rules": "bb&fk | bb&dt",
                "ag_rules": ""
            }
        }
    },
    "Canyon Chaos": {
        "id": 2,
        "Clear": {
            "fm_rules": "bb",
            "am_rules": "",
            "ag_rules": ""
        },
        "Collectibles":{
           #"Cherries" : 4,
           #"Strawberries" : 2,
           #"Oranges" : 3,
           #"Apples" : 4,
           #"Melons" : 6,
           "Galaxian" : {
               "id": 51,
                "fm_rules": "fk | rr | dt",
                "am_rules": "sbb",
                "ag_rules": ""

           }
        },
        "Gashapons": {
            "Orange Chest": {
                "id": 2,
                "fm_rules": "fk | dt",
                "am_rules": "bb",
                "ag_rules": ""
            },
            "Melon Chest": {
                "id": 3,
                "fm_rules": "sbb",
                "am_rules": "bb&fk | bb&dt | bb&f",
                "ag_rules": ""
            }
        },
        "Missions": {
            "Collect All Fruits": {
                "id": 4,
                "fm_rules": "sbb&fk | sbb&dt",
                "am_rules": "",
                "ag_rules": ""
            },
            "Destroy Bear Traps": {
                "id": 5,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Time Trial": {
                "id": 6,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        }
    },
    "Pac-Dot Pond": {
        "id": 3,
        "Clear": {
            "fm_rules": "",
            "am_rules": "",
            "ag_rules": ""
        },
        "Collectibles":{
           #"Cherries" : 0,
           #"Strawberries" : 0,
           #"Oranges" : 0,
           #"Apples" : 0,
           #"Melons" : 0,
           "Galaxian" :{
               "id": 32,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""

           }
        },
        "Gashapons":{
            "Apple Chest": {
                "id": 4,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Melon Chest": {
                "id": 5,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        },
        "Missions":{
            "Collect All Fruits": {
                "id": 7,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Defeat All Enemies": {
                "id": 8,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Time Trial": {
                "id": 9,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        }
    },
    "Clyde's Frog": {
        "id": 4,
        "Clear": {
            "fm_rules": "",
            "am_rules": "",
            "ag_rules": ""
        },
        "Collectibles":{},
        "Gashapons":{},
        "Missions":{
            "Don't Die": {
                "id": 10,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Time Trial": {
                "id": 11,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        }
    },
    "B-Doing Woods": {
        "id": 5,
        "Clear": {
            "fm_rules": "",
            "am_rules": "",
            "ag_rules": ""
        },
        "Collectibles":{
           #"Cherries" : 0,
           #"Strawberries" : 0,
           #"Oranges" : 0,
           #"Apples" : 0,
           #"Melons" : 0,
           "Galaxian" :{
               "id": 119,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""

           }
        },
        "Gashapons":{
            "Strawberry Chest": {
                "id": 6,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Melon Chest": {
                "id": 7,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        },
        "Missions":{
            "Collect All Fruits": {
                "id": 12,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Score 20,000": {
                "id": 13,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Time Trial": {
                "id": 14,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        }
    },
    "Treewood Forest": {
        "id": 6,
        "Clear": {
            "fm_rules": "",
            "am_rules": "",
            "ag_rules": ""
        },
        "Collectibles":{
           #"Cherries" : 0,
           #"Strawberries" : 0,
           #"Oranges" : 0,
           #"Apples" : 0,
           #"Melons" : 0,
           "Galaxian" :{
               "id": 54,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""

           }
        },
        "Gashapons": {
            "Cherry Chest": {
                "id": 8,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Melon Chest": {
                "id": 9,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        },
        "Missions": {
            "Collect All Fruits": {
                "id": 15,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Destroy Crates": {
                "id": 16,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Time Trial": {
                "id": 17,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        }
    },
    "Butane Pain": {
        "id": 7,
        "Clear": {
            "fm_rules": "",
            "am_rules": "",
            "ag_rules": ""
        },
        "Collectibles":{
           #"Cherries" : 0,
           #"Strawberries" : 0,
           #"Oranges" : 0,
           #"Apples" : 0,
           #"Melons" : 0,
           "Galaxian" :{
               "id": 57,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""

           }
        },
        "Gashapons": {
            "Melon Chest": {
                "id": 10,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Strawberry Chest": {
                "id": 11,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        },
        "Missions": {
            "Collect All Fruits": {
                "id": 18,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Defeat Enemies": {
                "id": 19,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Time Trial": {
                "id": 20,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        }
    },
    "Inky's Whimsy": {
        "id": 8,
        "Clear": {
            "fm_rules": "",
            "am_rules": "",
            "ag_rules": ""
        },
        "Collectibles":{},
        "Gashapons": {},
        "Missions": {
            "Don't Die": {
                "id": 21,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Time Trial": {
                "id": 22,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        }
    },
    "Ice River Run": {
        "id": 9,
        "Clear": {
            "fm_rules": "",
            "am_rules": "",
            "ag_rules": ""
        },
        "Collectibles":{
           #"Cherries" : 0,
           #"Strawberries" : 0,
           #"Oranges" : 0,
           #"Apples" : 0,
           #"Melons" : 0,
           "Galaxian" :{
               "id": 10,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
           }
        },
        "Gashapons": {
            "Cherry Chest": {
                "id": 12,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Melon Chest": {
                "id": 13,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        },
        "Missions": {
            "Collect All Fruits": {
                "id": 23,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Destroy Crates": {
                "id": 24,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Time Trial": {
                "id": 25,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""

            }
        }
    },
    "Avalanche Alley": {
        "id": 10,
        "Clear": {
            "fm_rules": "",
            "am_rules": "",
            "ag_rules": ""
        },
        "Collectibles":{
           #"Cherries" : 0,
           #"Strawberries" : 0,
           #"Oranges" : 0,
           #"Apples" : 0,
           #"Melons" : 0,
           "Galaxian" :{
               "id": 25,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
           }
        },
        "Gashapons": {
            "Melon Chest": {
                "id": 14,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Strawberry Chest": {
                "id": 15,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        },
        "Missions": {
            "Collect All Fruits": {
                "id": 26,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Defeat Enemies": {
                "id": 27,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Time Trial": {
                "id": 28,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        }
    },
    "Blade Mountain": {
        "id": 11,
        "Clear": {
            "fm_rules": "",
            "am_rules": "",
            "ag_rules": ""
        },
        "Collectibles":{
           #"Cherries" : 0,
           #"Strawberries" : 0,
           #"Oranges" : 0,
           #"Apples" : 0,
           #"Melons" : 0,
           "Galaxian" :{
               "id": 53,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""

           }
        },
        "Gashapons": {
            "Orange Chest": {
                "id": 16,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Strawberry Chest": {
                "id": 17,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        },
        "Missions": {
            "Collect All Fruits": {
                "id": 29,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Destroy Crates": {
                "id": 30,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Time Trial": {
                "id": 31,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        }
    },
    "Pinky's Revenge": {
        "id": 12,
        "Clear": {
            "fm_rules": "",
            "am_rules": "",
            "ag_rules": ""
        },
        "Collectibles":{},
        "Gashapons": {},
        "Missions": {
            "Don't Die": {
                "id": 32,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Time Trial": {
                "id": 33,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        }
    },
    "Into the Volcano!": {
        "id": 13,
        "Clear": {
            "fm_rules": "",
            "am_rules": "",
            "ag_rules": ""
        },
        "Collectibles":{
           #"Cherries" : 0,
           #"Strawberries" : 0,
           #"Oranges" : 0,
           #"Apples" : 0,
           #"Melons" : 0,
           "Galaxian" :{
               "id": 8,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""

           }
        },
        "Gashapons": {
            "Strawberry Chest": {
                "id": 18,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Melon Chest": {
                "id": 19,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        },
        "Missions": {
            "Collect All Fruits": {
                "id": 34,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Never hang off an edge": { #Should maybe change to mention only in that one room.
                "id": 35,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Time Trial": {
                "id": 36,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        }
    },
    "Volcanic Panic": {
        "id": 14,
        "Clear": {
            "fm_rules": "",
            "am_rules": "",
            "ag_rules": ""
        },
        "Collectibles":{
           #"Cherries" : 0,
           #"Strawberries" : 0,
           #"Oranges" : 0,
           #"Apples" : 0,
           #"Melons" : 0,
           "Galaxian" :{
               "id": 29,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""

           }
        },
        "Gashapons": {
            "Cherry Chest": {
                "id": 20,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Melon Chest": {
                "id": 21,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        },
        "Missions": {
            "Collect All Fruits": {
                "id": 37,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Defeat Enemies": {
                "id": 38,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Time Trial": {
                "id": 39,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        }
    },
    "Magma Opus": {
        "id": 15,
        "Clear": {
            "fm_rules": "",
            "am_rules": "",
            "ag_rules": ""
        },
        "Collectibles":{
           #"Cherries" : 0,
           #"Strawberries" : 0,
           #"Oranges" : 0,
           #"Apples" : 0,
           #"Melons" : 0,
           "Galaxian" :{
               "id": 56,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""

           }
        },
        "Gashapons": {
            "Strawberry Chest": {
                "id": 22,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Melon Chest": {
                "id": 23,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        },
        "Missions": {
            "Collect All Fruits": {
                "id": 40,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Never fall down a slope": {
                "id": 41,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Time Trial": {
                "id": 42,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        }
    },
    "Blinky in the Caldera": {
        "id": 16,
        "Clear": {
            "fm_rules": "",
            "am_rules": "",
            "ag_rules": ""
        },
        "Collectibles": {},
        "Gashapons": {},
        "Missions": {
            "Don't Die": {
                "id": 43,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Time Trial": {
                "id": 44,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        }
    },
    "Scuba Duba": {
        "id": 17,
        "Clear": {
            "fm_rules": "",
            "am_rules": "",
            "ag_rules": ""
        },
        "Collectibles":{
           #"Cherries" : 0,
           #"Strawberries" : 0,
           #"Oranges" : 0,
           #"Apples" : 0,
           #"Melons" : 0,
           "Galaxian" :{
               "id": 27,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""

           }
        },
        "Gashapons": {
            "Strawberry Chest": {
                "id": 24,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Melon Chest": {
                "id": 25,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        },
        "Missions": {
            "Collect All Fruits": {
                "id": 45,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Destroy Crates": {
                "id": 46,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Time Trial": {
                "id": 47,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        }
    },
    "Shark Attack": {
        "id": 18,
        "Clear": {
            "fm_rules": "",
            "am_rules": "",
            "ag_rules": ""
        },
        "Collectibles":{
           #"Cherries" : 0,
           #"Strawberries" : 0,
           #"Oranges" : 0,
           #"Apples" : 0,
           #"Melons" : 0,
           "Galaxian" :{
               "id": 60,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""

           }
        },
        "Gashapons": {
            "Strawberry Chest": {
                "id": 26,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Melon Chest": {
                "id": 27,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        },
        "Missions": {
            "Collect All Fruits": {
                "id": 48,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Never get caught by the Wild Shark": {
                "id": 49,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Time Trial": {
                "id": 50,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        }
    },
    "Yellow Pac-Marine": {
        "id": 19,
        "Clear": {
            "fm_rules": "",
            "am_rules": "",
            "ag_rules": ""
        },
        "Collectibles":{
           #"Cherries" : 4,
           #"Strawberries" : 7,
           #"Oranges" : 3,
           #"Apples" : 7,
           #"Melons" : 4,
           "Galaxian" : {}
        },
        "Gashapons": {
            "Purple": {
                "id": 28,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Red": {
                "id": 29,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        },
        "Missions": {
            "Collect All Fruits": {
                "id": 51,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Defeat Enemies": {
                "id": 52,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Don't Die": {
                "id": 53,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        }
    },
    "Whale on a Sub": {
        "id": 20,
        "Clear": {
            "fm_rules": "",
            "am_rules": "",
            "ag_rules": ""
        },
        "Collectibles": {},
        "Gashapons": {},
        "Missions": {
            "Don't Die": {
                "id": 54,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Time Trial": {
                "id": 55,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        }
    },
    "Haunted Boardwalk": {
        "id": 21,
        "Clear": {
            "fm_rules": "",
            "am_rules": "",
            "ag_rules": ""
        },
        "Collectibles":{
           #"Cherries" : 0,
           #"Strawberries" : 0,
           #"Oranges" : 0,
           #"Apples" : 0,
           #"Melons" : 0,
           "Galaxian" :{
               "id": 42,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""

           }
        },
        "Gashapons": {
            "Apple Chest": {
                "id": 30,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Melon Chest": {
                "id": 31,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        },
        "Missions": {
            "Collect All Fruits": {
                "id": 56,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Score 11,000": {
                "id": 57,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Time Trial": {
                "id": 58,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        }
    },
    "Night Crawling": {
        "id": 22,
        "Clear": {
            "fm_rules": "",
            "am_rules": "",
            "ag_rules": ""
        },
        "Collectibles": {
            # "Cherries" : 4,
            # "Strawberries" : 7,
            # "Oranges" : 3,
            # "Apples" : 7,
            # "Melons" : 4,
            "Galaxian": {}
        },
        "Gashapons": {
            "Melon Chest": {
                "id": 32,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Strawberry Chest": {
                "id": 33,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        },
        "Missions": {
            "Collect All Fruits": {
                "id": 59,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Destroy Crates": {
                "id": 60,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Time Trial": {
                "id": 61,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        }
    },
    "Ghost Bayou": {
        "id": 23,
        "Clear": {
            "fm_rules": "",
            "am_rules": "",
            "ag_rules": ""
        },
        "Collectibles":{
           #"Cherries" : 0,
           #"Strawberries" : 0,
           #"Oranges" : 0,
           #"Apples" : 0,
           #"Melons" : 0,
           "Galaxian" :{
               "id": 173,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""

           }
        },
        "Gashapons": {
            "Apple Chest": {
                "id": 34,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Melon Chest": {
                "id": 35,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        },
        "Missions": {
            "Collect All Fruits": {
                "id": 62,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Defeat Enemies": {
                "id": 63,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Time Trial": {
                "id": 64,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        }
    },
    "Spooky": {
        "id": 24,
        "Clear": {
            "fm_rules": "",
            "am_rules": "",
            "ag_rules": ""
        },
        "Collectibles": {},
        "Gashapons": {},
        "Missions": {
            "Don't Die": {
                "id": 65,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Time Trial": {
                "id": 66,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        }
    },
    "Deadly Poisonous Meadows": {
        "id": 25,
        "Clear": {
            "fm_rules": "",
            "am_rules": "",
            "ag_rules": ""
        },
        "Collectibles": {
            # "Cherries" : 4,
            # "Strawberries" : 7,
            # "Oranges" : 3,
            # "Apples" : 7,
            # "Melons" : 4,
            "Galaxian": {}
        },
        "Gashapons": {
            "Apple Chest": {
                "id": 36,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Orange Chest": {
                "id": 37,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Melon Chest": {
                "id": 38,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        },
        "Missions": {
            "Collect All Fruits": {
                "id": 67,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Destroy Bear Traps": {
                "id": 68,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Time Trial": {
                "id": 69,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        }
    },
    "A Long Poisonous Tongue": {
        "id": 26,
        "Clear": {
            "fm_rules": "",
            "am_rules": "",
            "ag_rules": ""
        },
        "Collectibles": {},
        "Gashapons": {},
        "Missions": {
            "Don't Die": {
                "id": 70,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Time Trial": {
                "id": 71,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        }
    },
    "Harsh Harsh Winds": {
        "id": 27,
        "Clear": {
            "fm_rules": "",
            "am_rules": "",
            "ag_rules": ""
        },
        "Collectibles": {
            # "Cherries" : 4,
            # "Strawberries" : 7,
            # "Oranges" : 3,
            # "Apples" : 7,
            # "Melons" : 4,
            "Galaxian": {}
        },
        "Gashapons": {
            "Strawberry Chest": {
                "id": 39,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Orange Chest": {
                "id": 40,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Melon Chest": {
                "id": 41,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        },
        "Missions": {
            "Collect All Fruits": {
                "id": 72,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Score 20,000": {
                "id": 73,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Time Trial": {
                "id": 74,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
        }
    },
    "Hunter of Darkness": {
        "id": 28,
        "Clear": {
            "fm_rules": "",
            "am_rules": "",
            "ag_rules": ""
        },
        "Collectibles": {},
        "Gashapons": {},
        "Missions": {
            "Don't Die": {
                "id": 75,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Time Trial": {
                "id": 76,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        }
    },
    "Pro Thunder Skater": {
        "id": 29,
        "Clear": {
            "fm_rules": "",
            "am_rules": "",
            "ag_rules": ""
        },
        "Collectibles": {
            # "Cherries" : 4,
            # "Strawberries" : 7,
            # "Oranges" : 3,
            # "Apples" : 7,
            # "Melons" : 4,
            "Galaxian": {}
        },
        "Gashapons": {
            "Strawberry Chest": {
                "id": 42,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Orange Chest": {
                "id": 43,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Melon Chest": {
                "id": 44,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        },
        "Missions": {
            "Collect All Fruits": {
                "id": 77,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Destroy Crates": {
                "id": 78,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Time Trial": {
                "id": 79,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        }
    },
    "Boom! Boom! Clap!": {
        "id": 30,
        "Clear": {
            "fm_rules": "",
            "am_rules": "",
            "ag_rules": ""
        },
        "Collectibles": {},
        "Gashapons": {},
        "Missions": {
            "Don't Die": {
                "id": 80,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Time Trial": {
                "id": 81,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        }
    },
    "Hot! Fire Trouble": {
        "id": 31,
        "Clear": {
            "fm_rules": "",
            "am_rules": "",
            "ag_rules": ""
        },
        "Collectibles": {
            # "Cherries" : 4,
            # "Strawberries" : 7,
            # "Oranges" : 3,
            # "Apples" : 7,
            # "Melons" : 4,
            "Galaxian": {}
        },
        "Gashapons": {
            "Cherry Chest": {
                "id": 45,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Apple Chest": {
                "id": 46,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Melon Chest": {
                "id": 47,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        },
        "Missions": {
            "Collect All Fruits": {
                "id": 82,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Score 25,000": {
                "id": 83,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Time Trial": {
                "id": 84,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        }
    },
    "Burning-Hot Beats": {
        "id": 32,
        "Clear": {
            "fm_rules": "",
            "am_rules": "",
            "ag_rules": ""
        },
        "Collectibles": {},
        "Gashapons": {},
        "Missions": {
            "Don't Die": {
                "id": 85,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Time Trial": {
                "id": 86,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        }
    },
    "Sharks Everywhere": {
        "id": 33,
        "Clear": {
            "fm_rules": "",
            "am_rules": "",
            "ag_rules": ""
        },
        "Collectibles": {
            # "Cherries" : 4,
            # "Strawberries" : 7,
            # "Oranges" : 3,
            # "Apples" : 7,
            # "Melons" : 4,
            "Galaxian": {}
        },
        "Gashapons": {
            "Orange Chest": {
                "id": 48,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Strawberry Chest": {
                "id": 49,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Melon Chest": {
                "id": 50,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        },
        "Missions": {
            "Collect All Fruits": {
                "id": 87,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Score 24,000": {
                "id": 88,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Time Trial": {
                "id": 89,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        }
    },
    "Pac-Marine Battle!": {
        "id": 34,
        "Clear": {
            "fm_rules": "",
            "am_rules": "",
            "ag_rules": ""
        },
        "Collectibles": {},
        "Gashapons": {},
        "Missions": {
            "Don't Die": {
                "id": 90,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Time Trial": {
                "id": 91,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        }
    },
    "Clumsy Bayou": {
        "id": 35,
        "Clear": {
            "fm_rules": "",
            "am_rules": "",
            "ag_rules": ""
        },
        "Collectibles": {
            # "Cherries" : 4,
            # "Strawberries" : 7,
            # "Oranges" : 3,
            # "Apples" : 7,
            # "Melons" : 4,
            "Galaxian": {}
        },
        "Gashapons": {
            "Orange Chest": {
                "id": 51,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Apple Chest": {
                "id": 52,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Melon Chest": {
                "id": 53,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        },
        "Missions": {
            "Collect All Fruits": {
                "id": 92,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Defeat Enemies": {
                "id": 93,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Time Trial": {
                "id": 94,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        }
    },
    "Legendary Story": {
        "id": 36,
        "Clear": {
            "fm_rules": "",
            "am_rules": "",
            "ag_rules": ""
        },
        "Collectibles": {},
        "Gashapons": {},
        "Missions": {
            "Don't Die": {
                "id": 95,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Time Trial": {
                "id": 96,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        }
    },
    "Flying Dark Shadow": {
        "id": 37,
        "Clear": {
            "fm_rules": "",
            "am_rules": "",
            "ag_rules": ""
        },
        "Collectibles": {},
        "Gashapons": {},
        "Missions": {
            "Don't Die": {
                "id": 97,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            },
            "Time Trial": {
                "id": 98,
                "fm_rules": "",
                "am_rules": "",
                "ag_rules": ""
            }
        }
    }
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

filler_data = {
    "1 Pac-Dot": 0,
    "5 Pac-Dots": 1,
    "10 Pac-Dots": 2,
    "100 Points": 3,
    "200 Points": 4,
    "500 Points": 5,
    "1000 Points": 6,
}

trap_data = {
    "Voice line Trap": 0
}
