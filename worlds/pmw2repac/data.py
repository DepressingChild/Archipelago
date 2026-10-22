#offsets?
LEVEL_OFFSET = 0
GOLDEN_FRUIT_OFFSET = 100
KEY_OFFSET = 200
COSTUME_OFFSET = 300
FRUIT_SWITCH_OFFSET = 400
MOVEMENT_OFFSET = 500

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
        "Checkpoints": {
            1: {},
            2: {
                "fm_rules": "bb",
            },
            3: {},
        },
        "Clear": {
            "checkpoint": 3,
        },
        "Gold Medal": {
            "checkpoint": 3,
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
                "checkpoint": 2,
            },
            "Melon Chest": {
                "id": 1,
                "checkpoint": 3,
                "fm_rules": "sbb&fk | sbb&dt",
                "am_rules": "fk | dt | rr",
            }
        },
        "Missions": {
             #might need reworking
            "Clear Stage": {
                "id": 1,
                "checkpoint": 3,
            },
            "Score 10,000": {
                "id": 2,
                "checkpoint": 3,
                "fm_rules": "ss | os | as | ms",
            },
            "Collect All Fruits": {
                "id": 3,
                "checkpoint": 3,
                "fm_rules": "sbb&fk | sbb&dt",
                "am_rules": "fk | dt | rr",
            }
        }
    },
    "Canyon Chaos": {
        "id": 2,
        "Checkpoints": {
            1: {},
            2: {},
        },
        "Clear": {
            "checkpoint": 2,
            "fm_rules": "bb | fk | dt | rr",
        },
        "Gold Medal": {
            "checkpoint": 2,
            "fm_rules": "bb&fk | bb&dt",
            "am_rules": "bb&rr",
        },
        "Collectibles":{
            #"Cherries" : 4,
            #"Strawberries" : 2,
            #"Oranges" : 3,
            #"Apples" : 4,
            #"Melons" : 6,
            "Galaxian" : {
                "id": 0,
                "checkpoint": 1,
                "fm_rules": "fk | rr | dt",
                "am_rules": "sbb",
            }
        },
        "Gashapons": {
            "Orange Chest": {
                "id": 2,
                "checkpoint": 1,
                "fm_rules": "bb | fk | dt",
            },
            "Melon Chest": {
                "id": 3,
                "checkpoint": 2,
                "fm_rules": "sbb&fk | sbb&dt",
                "am_rules": "bb&fk | bb&dt | bb&rr | bb&f | sbb",
            }
        },
        "Missions": {
            "Collect All Fruits": {
                "id": 4,
                "checkpoint": 2,
                "fm_rules": "sbb&fk | sbb&dt",
                "am_rules": "bb&fk | sbb",
            },
            "Destroy Bear Traps": {
                "id": 5,
                "checkpoint": 2,
                "fm_rules": "bb&fk | bb&dt | sbb",
            },
            "Time Trial": {
                "id": 6,
                "checkpoint": 2,
                "fm_rules": "bb | fk | dt | rr",
            }
        }
    },
    "Pac-Dot Pond": {
        "id": 3,
        "Checkpoints": {
            1: {
                "fm_rules": "bb&rr",
                "am_rules": "sbb",
            },
            2: {},
        },
        "Clear": {
            "checkpoint": 2,
        },
        "Gold Medal": {
            "checkpoint": 2,
        },
        "Collectibles":{
            #"Cherries" : 0,
            #"Strawberries" : 0,
            #"Oranges" : 0,
            #"Apples" : 0,
            #"Melons" : 0,
            "Galaxian" :{
               "id": 1,
                "checkpoint": 1,

            }
        },
        "Gashapons":{
            "Apple Chest": {
                "id": 4,
                "checkpoint": 1,
                "fm_rules": "fk | dt",
                "am_rules": "sbb",
            },
            "Melon Chest": {
                "id": 5,
                "checkpoint": 2,
                "fm_rules": "fk | dt",
                "am_rules": "sbb",
            }
        },
        "Missions":{
            "Collect All Fruits": {
                "id": 7,
                "checkpoint": 2,
                "fm_rules": "fk | dt",
                "am_rules": "sbb",
                "ag_rules": ""
            },
            "Defeat All Enemies": {
                "id": 8,
                "checkpoint": 2,
                "fm_rules": "fk | dt",
                "am_rules": "rr | sbb",
            },
            "Time Trial": {
                "id": 9,
                "checkpoint": 2,
            }
        }
    },
    "Clyde's Frog": {
        "id": 4,
        "Clear": {
            "fm_rules": "bb | fk | dt | rr",
        },
        "Gold Medal": {
            "fm_rules": "bb | fk | dt | rr",
        },
        "Collectibles":{},
        "Gashapons":{},
        "Missions":{
            "Don't Die": {
                "id": 10,
                "fm_rules": "bb | fk | dt | rr",
            },
            "Clear Stage": {
                "id": 11,
                "fm_rules": "bb | fk | dt | rr",
            }
        }
    },
    "B-Doing Woods": {
        "id": 5,
        "Checkpoints": {
            1: {
                "fm_rules": "bb",
            },
            2: {},
            3: {
                "fm_rules": "rr",
                "am_rules": "fk | dt | f | sbb"
            },
            4: {},
            5: {},
        },
        "Clear": {
            "checkpoint": 5,
        },
        "Gold Medal": {
            "checkpoint": 5,
            "fm_rules": "fk",
            "am_rules": "sbb&f | dt | rr",
        },
        "Collectibles":{
            #"Cherries" : 0,
            #"Strawberries" : 0,
            #"Oranges" : 0,
            #"Apples" : 0,
            #"Melons" : 0,
            "Galaxian" :{
               "id": 2,
               "checkpoint": 3,
               "fm_rules": "as",
            }
        },
        "Gashapons":{
            "Strawberry Chest": {
                "id": 6,
                "checkpoint": 4,
                "fm_rules": "fk | dt",
            },
            "Melon Chest": {
                "id": 7,
                "checkpoint": 5,
                "fm_rules": "fk | sbb&dt",
                "am_rules": "dt",
            }
        },
        "Missions":{
            "Collect All Fruits": {
                "id": 12,
                "checkpoint": 5,
                "fm_rules": "fk | sbb&dt",
                "am_rules": "dt",
            },
            "Score 20,000": {
                "id": 13,
                "checkpoint": 5,
                "fm_rules": "fk&ms&os | fk&ms&ss&cs | fk&ms&ss&as | sbb&rr&dt&ms&os | sbb&rr&dt&ms&ss&cs | sbb&rr&dt&ms&ss&as | rr&dt&ms&os&cs | rr&dt&ms&os&ss | rr&dt&ms&os&as | rr&dt&ms&ss&cs&as", #Need to find a better way to create rules like this.
                "am_rules": "dt&ms&os | dt&ms&ss&cs | dt&ms&ss&as | f&cs&ss&as&ms | f&ss&os&ms | f&os&as&ms | sbb&cs&ss&as&ms | sbb&ss&os&ms | sbb&os&as&ms",
                "ag_rules": ""
            },
            "Time Trial": {
                "id": 14,
                "checkpoint": 5,
            }
        }
    },
    "Treewood Forest": {
        "id": 6,
        "Checkpoints": {
            1: {
                "fm_rules": "bb",
            },
            2: {},
            3: {
                "fm_rules": "rr",
                "am_rules": "fk | dt | sbb&f",
            },
            4: {},
            5: {},
            6: {},
        },
        "Clear": {
            "checkpoint": 6,
        },
        "Gold Medal": {
            "checkpoint": 6,
        },
        "Collectibles":{
            #"Cherries" : 0,
            #"Strawberries" : 0,
            #"Oranges" : 0,
            #"Apples" : 0,
            #"Melons" : 0,
            "Galaxian" :{
               "id": 3,
               "checkpoint": 4,
               "fm_rules": "os",
            }
        },
        "Gashapons": {
            "Cherry Chest": {
                "id": 8,
                "checkpoint": 5,
            },
            "Melon Chest": {
                "id": 9,
                "checkpoint": 6,
            }
        },
        "Missions": {
            "Collect All Fruits": {
                "id": 15,
                "checkpoint": 6,
            },
            "Destroy Crates": {
                "id": 16,
                "checkpoint": 6,
            },
            "Time Trial": {
                "id": 17,
                "checkpoint": 6,
            }
        }
    },
    "Butane Pain": {
        "id": 7,
        "Checkpoints": {
            1: {},
            2: {
                "fm_rules": "bb&rr",
                "am_rules": "rr | bb&f | sbb&fk",
            },
            3:{
                "am_rules": "bb",
            },
            4: {},
            5: {
                "am_rules": "dt | sbb&fk&f"
            },
            6: {},
        },
        "Clear": {
            "checkpoint": 6,
        },
        "Gold Medal": {
            "checkpoint": 6,
        },
        "Collectibles":{
            #"Cherries" : 0,
            #"Strawberries" : 0,
            #"Oranges" : 0,
            #"Apples" : 0,
            #"Melons" : 0,
            "Galaxian" :{
                "id": 4,
                "checkpoint": 1,
                "fm_rules": "bb&rr&as",
                "am_rules": "bb&f&as | sbb&fk&as",
            }
        },
        "Gashapons": {
            "Melon Chest": {
                "id": 10,
                "checkpoint": 6,
                "fm_rules": "fk | dt",
            },
            "Strawberry Chest": {
                "id": 11,
                "checkpoint": 5,
                "fm_rules": "f | dt | sbb",
                "am_rules": "NONE",
            }
        },
        "Missions": {
            "Collect All Fruits": {
                "id": 18,
                "checkpoint": 6,
                "fm_rules": "fk | dt",
            },
            "Defeat Enemies": {
                "id": 19,
                "checkpoint": 6,
                "fm_rules": "fk | dt",
                "am_rules": "sbb&rr",
            },
            "Time Trial": {
                "id": 20,
                "checkpoint": 6,
            }
        }
    },
    "Inky's Whimsy": {
        "id": 8,
        "Clear": {
            "fm_rules": "bb&fk",
            "am_rules": "sbb&dt",
        },
        "Gold Medal": {
            "fm_rules": "bb&fk",
            "am_rules": "sbb&dt",
        },
        "Collectibles":{},
        "Gashapons": {},
        "Missions": {
            "Don't Die": {
                "id": 21,
                "fm_rules": "bb&fk",
                "am_rules": "sbb&dt",
            },
            "Time Trial": {
                "id": 22,
                "fm_rules": "bb&fk",
                "am_rules": "sbb&dt",
            }
        }
    },
    "Ice River Run": {
        "id": 9,
        "Checkpoints": {
            1: {},
            2: {},
            3: {},
            4: {},
            5: {},
            6: {},
            7: {},
            8: {},
            9: {},
            10: {},
        },
        "Clear": {
            "checkpoint": 10,
        },
        "Gold Medal": {
            "checkpoint": 10,
            "fm_rules": "rr",
            "am_rules": "NONE",
        },
        "Collectibles":{
            #"Cherries" : 0,
            #"Strawberries" : 0,
            #"Oranges" : 0,
            #"Apples" : 0,
            #"Melons" : 0,
            "Galaxian" :{
                "id": 5,
                "checkpoint": 1,
                "fm_rules": "bb&fk | bb&dt | bb&rr",
                "am_rules": "sbb",
            }
        },
        "Gashapons": {
            "Cherry Chest": {
                "id": 12,
                "checkpoint": 6,
                "fm_rules": "sbb | fk | dt",
                "am_rules": "rr",
            },
            "Melon Chest": {
                "id": 13,
                "checkpoint": 10,
                "fm_rules": "sbb&fk | sbb&dt | sbb&rr",
                "am_rules": "bb&fk | bb&dt | bb&rr | sbb",
            }
        },
        "Missions": {
            "Collect All Fruits": {
                "id": 23,
                "checkpoint": 10,
                "fm_rules": "sbb&fk | sbb&dt",
                "am_rules": "bb&fk | bb&dt | bb&rr | sbb",
            },
            "Destroy Crates": {
                "id": 24,
                "checkpoint": 10,
                "fm_rules": "sbb",
                "am_rules": "fk | dt | rr",
            },
            "Time Trial": {
                "id": 25,
                "checkpoint": 10,

            }
        }
    },
    "Avalanche Alley": {
        "id": 10,
        "Checkpoints": {
            1: {},
            2: {},
            3: {
                "fm_rules": "bb",
            },
            4: {
                "fm_rules": "rr",
                "am_rules": "NONE",
            },
            5: {},
            6: {},
        },
        "Clear": {
            "checkpoint": 6,
        },
        "Gold Medal": {
            "checkpoint": 6,
            "am_rules": "fk",
        },
        "Collectibles":{
            #"Cherries" : 0,
            #"Strawberries" : 0,
            #"Oranges" : 0,
            #"Apples" : 0,
            #"Melons" : 0,
            "Galaxian" :{
                "id": 6,
                "checkpoint": 4,
                "fm_rules": "fk&os | dt&os",
            }
        },
        "Gashapons": {
            "Melon Chest": {
                "id": 14,
                "checkpoint": 6,
                "fm_rules": "fk | dt",
            },
            "Strawberry Chest": {
                "id": 15,
                "checkpoint": 5,
                "fm_rules": "fk | dt",
            }
        },
        "Missions": {
            "Collect All Fruits": {
                "id": 26,
                "checkpoint": 6,
                "fm_rules": "fk | dt",
            },
            "Defeat Enemies": {
                "id": 27,
                "checkpoint": 6,
                "fm_rules": "rr&fk",
                "am_rules": "fk&f | fk&dt",
            },
            "Time Trial": {
                "id": 28,
                "checkpoint": 6,
            }
        }
    },
    "Blade Mountain": {
        "id": 11,
        "Checkpoints": {
            1: {},
            2: {},
            3: {},
            4: {},
            5: {},
            6: {},
        },
        "Clear": {
            "checkpoint": 6,
        },
        "Gold Medal": {
            "checkpoint": 6,
            "fm_rules": "fk | dt",
        },
        "Collectibles":{
            #"Cherries" : 0,
            #"Strawberries" : 0,
            #"Oranges" : 0,
            #"Apples" : 0,
            #"Melons" : 0,
            "Galaxian" :{
                "id": 7,
                "checkpoint": 6,
                "fm_rules": "fk&ms | dt&ms",
            }
        },
        "Gashapons": {
            "Orange Chest": {
                "id": 16,
                "checkpoint": 6,
                "fm_rules": "fk | dt",
            },
            "Strawberry Chest": {
                "id": 17,
                "checkpoint": 6,
                "fm_rules": "fk | dt",
            }
        },
        "Missions": {
            "Collect All Fruits": {
                "id": 29,
                "checkpoint": 6,
                "fm_rules": "fk | dt",
            },
            "Destroy Crates": {
                "id": 30,
                "checkpoint": 6,
                "fm_rules": "fk | dt",
            },
            "Time Trial": {
                "id": 31,
                "checkpoint": 6,
            }
        }
    },
    "Pinky's Revenge": {
        "id": 12,
        "Checkpoints": {
            1: {},
        },
        "Clear": {
            "checkpoint": 1,
            "fm_rules": "bb&fk",
        },
        "Gold Medal": {
            "checkpoint": 1,
            "fm_rules": "bb&fk",
        },
        "Collectibles":{},
        "Gashapons": {},
        "Missions": {
            "Don't Die": {
                "id": 32,
                "checkpoint": 1,
                "fm_rules": "bb&fk",
            },
            "Time Trial": {
                "id": 33,
                "checkpoint": 1,
                "fm_rules": "bb&fk",
            }
        }
    },
    "Into the Volcano!": {
        "id": 13,
        "Checkpoints": {
            1: {},
            2: {},
            3: {},
            4: {
                "fm_rules": "rr",
                "am_rules": "f",
                "ag_rules": "fk",
            },
            5: {},
            6: {},
            7: {
                "fm_rules": "bb",
            },
            8: {},
        },
        "Clear": {
            "checkpoint": 8,
        },
        "Gold Medal": {
            "checkpoint": 8,
            "fm_rules": "fk | dt",
            "am_rules": "rr",
        },
        "Collectibles":{
            #"Cherries" : 0,
            #"Strawberries" : 0,
            #"Oranges" : 0,
            #"Apples" : 0,
            #"Melons" : 0,
            "Galaxian" :{
                "id": 8,
                "checkpoint": 7,
            }
        },
        "Gashapons": {
            "Strawberry Chest": {
                "id": 18,
                "checkpoint": 7,
                "fm_rules": "fk | dt | sbb",
            },
            "Melon Chest": {
                "id": 19,
                "checkpoint": 8,
                "fm_rules": "sbb&fk | sbb&dt&f",
                "am_rules": "sbb&dt",
            }
        },
        "Missions": {
            "Collect All Fruits": {
                "id": 34,
                "checkpoint": 8,
                "fm_rules": "sbb&fk | sbb&dt&f",
                "am_rules": "sbb&dt",
            },
            "Never hang off an edge": { #Should maybe change to mention only in that one room.
                "id": 35,
                "checkpoint": 8,
            },
            "Time Trial": {
                "id": 36,
                "checkpoint": 8,
            }
        }
    },
    "Volcanic Panic": {
        "id": 14,
        "Checkpoints": {
            1: {},
            2: {},
            3: {
                "fm_rules": "rr",
                "am_rules": "fk&f | sbb&f",
            },
            4: {},
            5: {
                "fm_rules": "bb",
            },
            6: {},
            7: {},
            8: {},
            9: {},
            10: {},
            11: {
                "ag_rules": "bb",
            },
        },
        "Clear": {
            "checkpoint": 11,
        },
        "Gold Medal": {
            "checkpoint": 11,
        },
        "Collectibles":{
            #"Cherries" : 0,
            #"Strawberries" : 0,
            #"Oranges" : 0,
            #"Apples" : 0,
            #"Melons" : 0,
            "Galaxian" :{
                "id": 9,
                "checkpoint": 10,
                "fm_rules": "as",
            }
        },
        "Gashapons": {
            "Cherry Chest": {
                "id": 20,
                "checkpoint": 7,
                "fm_rules": "fk | dt",
            },
            "Melon Chest": {
                "id": 21,
                "checkpoint": 11,
                "fm_rules": "sbb&fk | sbb&dt | fk&f | dt&f",
                "am_rules": "fk",
            }
        },
        "Missions": {
            "Collect All Fruits": {
                "id": 37,
                "checkpoint": 11,
                "fm_rules": "sbb&fk | sbb&dt | fk&f",
                "am_rules": "fk",
                "ag_rules": ""
            },
            "Defeat Enemies": {
                "id": 38,
                "checkpoint": 11,
                "fm_rules": "dt",
                "am_rules": "NONE",
            },
            "Time Trial": {
                "id": 39,
                "checkpoint": 11,
            }
        }
    },
    "Magma Opus": {
        "id": 15,
        "Checkpoints": {
            1: {},
            2: {},
            3: {
                "fm_rules": "sbb",
                "am_rules": "bb&fk",
            },
            4: {},
            5: {},
            6: {},
            7: {},
            8: {},
            9: {},
        },
        "Clear": {
            "checkpoint": 9,
        },
        "Gold Medal": {
            "checkpoint": 9,
        },
        "Collectibles":{
           #"Cherries" : 0,
           #"Strawberries" : 0,
           #"Oranges" : 0,
           #"Apples" : 0,
           #"Melons" : 0,
           "Galaxian" :{
               "id": 10,
                "fm_rules": "fk&cs | dt&cs",
           }
        },
        "Gashapons": {
            "Strawberry Chest": {
                "id": 22,
                "checkpoint": 9,
                "fm_rules": "fk | dt",
            },
            "Melon Chest": {
                "id": 23,
                "checkpoint": 9,
            }
        },
        "Missions": {
            "Collect All Fruits": {
                "id": 40,
                "checkpoint": 9,
                "fm_rules": "fk | dt",
            },
            "Never fall down a slope": {
                "id": 41,
                "checkpoint": 9,
            },
            "Time Trial": {
                "id": 42,
                "checkpoint": 9,
            }
        }
    },
    "Blinky in the Caldera": {
        "id": 16,
        "Clear": {
            "fm_rules": "bb",
        },
        "Gold Medal": {
            "fm_rules": "bb&rr",
            "am_rules": "bb",
        },
        "Collectibles": {},
        "Gashapons": {},
        "Missions": {
            "Don't Die": {
                "id": 43,
                "fm_rules": "bb",
            },
            "Time Trial": {
                "id": 44,
                "fm_rules": "bb",
            }
        }
    },
    "Scuba Duba": {
        "id": 17,
        "Checkpoints": {
            1: {},
            2: {},
            3: {
                "fm_rules": "dk",
            },
            4: {},
            5: {},
        },
        "Clear": {
            "checkpoint": 5,
        },
        "Gold Medal": {
            "checkpoint": 5,
        },
        "Collectibles":{
            #"Cherries" : 0,
            #"Strawberries" : 0,
            #"Oranges" : 0,
            #"Apples" : 0,
            #"Melons" : 0,
            "Galaxian" :{
                "id": 11,
                "checkpoint": 4,
                "fm_rules": "as",
            }
        },
        "Gashapons": {
            "Strawberry Chest": {
                "id": 24,
                "checkpoint": 4,
            },
            "Melon Chest": {
                "id": 25,
                "checkpoint": 5,
            }
        },
        "Missions": {
            "Collect All Fruits": {
                "id": 45,
                "checkpoint": 5,
            },
            "Destroy Crates": {
                "id": 46,
                "checkpoint": 5,
            },
            "Time Trial": {
                "id": 47,
                "checkpoint": 5,
            }
        }
    },
    "Shark Attack": {
        "id": 18,
        "Checkpoints": {
            1: {},
            2: {
                "fm_rules": "dk | fk",
            },
            3: {},
            4: {},
            5: {},
            6: {},
            7: {},
        },
        "Clear": {
            "fm_rules": "fk | dk",
            "am_rules": "",
            "ag_rules": ""
        },
        "Gold Medal": {
            "checkpoint": 7,
        },
        "Collectibles":{
            #"Cherries" : 0,
            #"Strawberries" : 0,
            #"Oranges" : 0,
            #"Apples" : 0,
            #"Melons" : 0,
            "Galaxian" :{
                "id": 12,
                "checkpoint": 3,
                "fm_rules": "os | os",

            }
        },
        "Gashapons": {
            "Strawberry Chest": {
                "id": 26,
                "checkpoint": 5,
            },
            "Melon Chest": {
                "id": 27,
                "checkpoint": 7,
            }
        },
        "Missions": {
            "Collect All Fruits": {
                "id": 48,
                "checkpoint": 7,
            },
            "Never get caught by the Wild Shark": {
                "id": 49,
                "checkpoint": 7,
            },
            "Time Trial": {
                "id": 50,
                "checkpoint": 7,
            }
        }
    },
    "Yellow Pac-Marine": {
        "id": 19,
        "Clear": {},
        "Gold Medal": {},
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
            },
            "Red": {
                "id": 29,
            }
        },
        "Missions": {
            "Collect All Fruits": {
                "id": 51,
            },
            "Defeat Enemies": {
                "id": 52,
            },
            "Don't Die": {
                "id": 53,
            }
        }
    },
    "Whale on a Sub": {
        "id": 20,
        "Clear": {},
        "Gold Medal": {},
        "Collectibles": {},
        "Gashapons": {},
        "Missions": {
            "Don't Die": {
                "id": 54,
            },
            "Time Trial": {
                "id": 55,
            }
        }
    },
    "Haunted Boardwalk": {
        "id": 21,
        "Checkpoints": {
            1: {},
            2: {},
            3: {},
            4: {},
            5: {},
            6: {},
        },
        "Clear": {
            "checkpoint": 6,
        },
        "Gold Medal": {
            "checkpoint": 6,
        },
        "Collectibles":{
            #"Cherries" : 0,
            #"Strawberries" : 0,
            #"Oranges" : 0,
            #"Apples" : 0,
            #"Melons" : 0,
            "Galaxian" :{
                "id": 13,
                "checkpoint": 6,
                "fm_rules": "fk&ss | dt&ss",
                "am_rules": "sbb&f&ss",
                "ag_rules": "sbb&ss"

            }
        },
        "Gashapons": {
            "Apple Chest": {
                "id": 30,
                "checkpoint": 6,
                "fm_rules": "fk | dt",
                "am_rules": "sbb&f",
                "ag_rules": "sbb"
            },
            "Melon Chest": {
                "id": 31,
                "checkpoint": 6,
                "fm_rules": "fk | dt",
                "am_rules": "sbb&f",
                "ag_rules": "sbb"
            }
        },
        "Missions": {
            "Collect All Fruits": {
                "id": 56,
                "checkpoint": 6,
                "fm_rules": "fk | dt",
                "am_rules": "sbb&f",
                "ag_rules": "sbb"
            },
            "Score 11,000": {
                "id": 57,
                "checkpoint": 6,
                "fm_rules": "fk&ms&as | fk&ms&ss | dt&ms&as | dt&ms&ss",
                "am_rules": "sbb&f&ms&as | sbb&f&ms&ss",
                "ag_rules": "sbb&ms&as | sbb&ms&ss"
            },
            "Time Trial": {
                "id": 58,
                "checkpoint": 6,
            }
        }
    },
    "Night Crawling": {
        "id": 22,
        "Checkpoints": {
            1: {},
            2: {
                "fm_rules": "bb",
                "am_rules": "rr",
            },
            3: {},
            4: {},
            5: {
                "fm_rules": "bb",
            },
            6: {
                "fm_rules": "rr",
                "am_rules": "dt",
            },
            7: {},
            8: {},
            9: {},
        },
        "Clear": {
            "checkpoint": 9,
        },
        "Gold Medal": {
            "checkpoint": 9,
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
                "checkpoint": 9,
                "fm_rules": "sbb&fk | sbb&dt",
                "am_rules": "fk | f | dt",
            },
            "Strawberry Chest": {
                "id": 33,
                "checkpoint": 8,
                "fm_rules": "fk | dt",
                "am_rules": "sbb",
            }
        },
        "Missions": {
            "Collect All Fruits": {
                "id": 59,
                "checkpoint": 9,
                "fm_rules": "sbb&fk | sbb&dt",
                "am_rules": "dt | fk | f",
            },
            "Destroy Crates": {
                "id": 60,
                "checkpoint": 9,
                "fm_rules": "sbb&fk | sbb&dt",
                "am_rules": "dt | fk",
            },
            "Time Trial": {
                "id": 61,
                "checkpoint": 9,
            }
        }
    },
    "Ghost Bayou": {
        "id": 23,
        "Checkpoints": {
            1: {},
            2: {},
            3: {},
            4: {
                "fm_rules": "bb",
            },
            5: {},
            6: {},
            7: {},
            8: {},
            9: {},
            10: {
                "fm_rules": "rr | f",
                "am_rules": "fk | dt | sbb",
            },
            11: {},
            12: {},
            13: {
                "fm_rules": "rr",
                "am_rules": "dt",
            },
        },
        "Clear": {
            "checkpoint": 13,
        },
        "Gold Medal": {
            "checkpoint": 13,
        },
        "Collectibles":{
            #"Cherries" : 0,
            #"Strawberries" : 0,
            #"Oranges" : 0,
            #"Apples" : 0,
            #"Melons" : 0,
            "Galaxian" :{
                "id": 14,
                "checkpoint": 5,
                "fm_rules": "fk&os | dt&os",
            }
        },
        "Gashapons": {
            "Apple Chest": {
                "id": 34,
                "checkpoint": 12,
                "fm_rules": "fk | dt",
                "am_rules": "sbb",
            },
            "Melon Chest": {
                "id": 35,
                "checkpoint": 13,
                "fm_rules": "sbb&fk&f | sbb&dt&f",
                "am_rules": "dt | fk",
                "ag_rules": ""
            }
        },
        "Missions": {
            "Collect All Fruits": {
                "id": 62,
                "checkpoint": 13,
                "fm_rules": "sbb&fk&f | sbb&dt&f",
                "am_rules": "fk",
                "ag_rules": "dt"
            },
            "Defeat Enemies": {
                "id": 63,
                "checkpoint": 13,
                "fm_rules": "fk | dt",
                "am_rules": "sbb",
            },
            "Time Trial": {
                "id": 64,
                "checkpoint": 13,
            }
        }
    },
    "Spooky": {
        "id": 24,
        "Clear": {
            "fm_rules": "sbb&fk&rr | sbb&dt&rr",
        },
        "Gold Medal": {
            "fm_rules": "sbb&fk&rr | sbb&dt&rr",
        },
        "Collectibles": {},
        "Gashapons": {},
        "Missions": {
            "Don't Die": {
                "id": 65,
                "fm_rules": "sbb&fk&rr | sbb&dt&rr",
            },
            "Time Trial": {
                "id": 66,
                "fm_rules": "sbb&fk&rr | sbb&dt&rr",
            }
        }
    },
    "Deadly Poisonous Meadows": {
        "id": 25,
        "Checkpoints": {
            1: {},
            2: {
                "fm_rules": "bb",
                "am_rules": "rr",
            },
            3: {},
            4: {
                "fm_rules": "rr",
                "am_rules": "NONE",
            },
            5: {},
            6: {},
        },
        "Clear": {
            "checkpoint": 6,
        },
        "Gold Medal": {
            "checkpoint": 6,
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
                "checkpoint": 1,
                "fm_rules": "bb&fk | bb&dt | rr&fk | rr&dt",
                "am_rules": "sbb&f | rr",
            },
            "Orange Chest": {
                "id": 37,
                "checkpoint": 3,
                "fm_rules": "fk | dt | rr | sbb",
            },
            "Melon Chest": {
                "id": 38,
                "checkpoint": 6,
                "fm_rules": "sbb&fk | sbb&dt",
                "am_rules": "fk | dt",
            }
        },
        "Missions": {
            "Collect All Fruits": {
                "id": 67,
                "checkpoint": 6,
                "fm_rules": "sbb&fk | sbb&dt",
                "am_rules": "fk | dt",
                "ag_rules": ""
            },
            "Destroy Bear Traps": {
                "id": 68,
                "checkpoint": 6,
                "fm_rules": "fk | dt | sbb",
            },
            "Time Trial": {
                "id": 69,
                "checkpoint": 6,
            }
        }
    },
    "A Long Poisonous Tongue": {
        "id": 26,
        "Clear": {
            "fm_rules": "bb | rr | fk",
        },
        "Gold Medal": {
            "fm_rules": "bb | rr | fk",
        },
        "Collectibles": {},
        "Gashapons": {},
        "Missions": {
            "Don't Die": {
                "id": 70,
                "fm_rules": "bb | rr | fk",
            },
            "Time Trial": {
                "id": 71,
                "fm_rules": "bb | rr | fk",
            }
        }
    },
    "Harsh Harsh Winds": {
        "id": 27,
        "Checkpoints": {
            1: {},
            2: {
                "fm_rules": "bb&rr",
                "am_rules": "bb&f | sbb&fk",
            },
            3: {},
            4: {},
            5: {},
            6: {
                "am_rules": "dt&f | sbb&fk&f | sbb&fk&dt"
            },
            7: {},
            8: {},
        },
        "Clear": {
            "checkpoint": 8,
        },
        "Gold Medal": {
            "checkpoint": 8,
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
                "checkpoint": 6,
                "fm_rules": "fk | dt",
                "am_rules": "NONE",
                "ag_rules": ""
            },
            "Orange Chest": {
                "id": 40,
                "checkpoint": 5,
                "am_rules": "dt&f | sbb&fk&f | sbb&fk&dt",
            },
            "Melon Chest": {
                "id": 41,
                "checkpoint": 8,
                "fm_rules": "sbb&fk | sbb&dt",
            }
        },
        "Missions": {
            "Collect All Fruits": {
                "id": 72,
                "checkpoint": 8,
                "fm_rules": "sbb&fk | sbb&dt",
            },
            "Score 20,000": {
                "id": 73,
                "fm_rules": "sbb&rr&fk&ms&ss | sbb&rr&dt&ms&ss | bb&rr&fk&ms&ss&cs | bb&rr&dt&ms&ss&cs | bb&rr&fk&ms&as&os&cs | bb&rr&dt&ms&as&os&cs | sbb&rr&fk&ms&os&cs | sbb&rr&dt&ms&os&cs | sbb&rr&fk&ms&os&as | sbb&rr&dt&ms&os&as",
                "am_rules": "sbb&fk&dt&ms&ss | sbb&fk&f&ms&ss | sbb&rr&ms&ss&cs | sbb&rr&ms&as&os&cs | sbb&fk&dt&ms&os&cs | sbb&fk&f&ms&os&cs | sbb&dt&f&ms&os&cs | sbb&fk&dt&ms&os&as | sbb&fk&f&ms&os&as | sbb&dt&f&ms&os&as | bb&dt&f&ms&ss&cs | bb&dt&f&ms&as&ss | bb&dt&f&ms&as&os&cs | bb&dt&f&ms&os&ss",
                "ag_rules": "sbb&rr&fk&ms&os | sbb&rr&dt&ms&os | sbb&fk&dt&ms&os | sbb&fk&f&ms&os | sbb&dt&f&ms&os"
            },
            "Time Trial": {
                "id": 74,
                "checkpoint": 8,
            },
        }
    },
    "Hunter of Darkness": {
        "id": 28,
        "Clear": {
            "fm_rules": "bb&fk",
            "am_rules": "sbb&dt",
        },
        "Gold Medal": {
            "fm_rules": "bb&fk",
            "am_rules": "sbb&dt",
        },
        "Collectibles": {},
        "Gashapons": {},
        "Missions": {
            "Don't Die": {
                "id": 75,
                "fm_rules": "bb&fk",
                "am_rules": "sbb&dt",
            },
            "Time Trial": {
                "id": 76,
                "fm_rules": "bb&fk",
                "am_rules": "sbb&dt",
            }
        }
    },
    "Pro Thunder Skater": {
        "id": 29,
        "Checkpoints": {
            1: {},
            2: {},
            3: {},
            4: {},
            5: {},
            6: {},
        },
        "Clear": {
            "checkpoint": 6,
        },
        "Gold Medal": {
            "checkpoint": 6,
            "fm_rules": "fk | dt",
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
                "checkpoint": 6,
                "fm_rules": "fk | dt",
            },
            "Orange Chest": {
                "id": 43,
                "checkpoint": 6,
                "fm_rules": "fk | dt",
            },
            "Melon Chest": {
                "id": 44,
                "checkpoint": 6,
                "fm_rules": "fk | dt",
            }
        },
        "Missions": {
            "Collect All Fruits": {
                "id": 77,
                "checkpoint": 6,
                "fm_rules": "fk | dt",
            },
            "Destroy Crates": {
                "id": 78,
                "checkpoint": 6,
                "fm_rules": "fk | dt",
            },
            "Time Trial": {
                "id": 79,
                "checkpoint": 6,
                "fm_rules": "fk | dt",
            }
        }
    },
    "Boom! Boom! Clap!": {
        "id": 30,
        "Checkpoints": {
            1: {},
        },
        "Clear": {
            "checkpoint": 1,
            "fm_rules": "bb&fk",
        },
        "Gold Medal": {
            "checkpoint": 1,
            "fm_rules": "bb&fk",
        },
        "Collectibles": {},
        "Gashapons": {},
        "Missions": {
            "Don't Die": {
                "id": 80,
                "checkpoint": 1,
                "fm_rules": "bb&fk",
            },
            "Time Trial": {
                "id": 81,
                "checkpoint": 1,
                "fm_rules": "bb&fk",
            }
        }
    },
    "Hot! Fire Trouble": {
        "id": 31,
        "Checkpoints": {
            1: {},
            2: {},
            3: {
                "fm_rules": "rr",
                "am_rules": "fk&f | sbb&f",
            },
            4: {},
            5: {
                "fm_rules": "bb",
            },
            6: {},
            7: {},
            8: {},
            9: {},
            10: {
                "ag_rules": "bb",
            },
        },
        "Clear": {
            "checkpoint": 10,
        },
        "Gold Medal": {
            "checkpoint": 10,
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
                "checkpoint": 6,
                "fm_rules": "fk | dt",
            },
            "Apple Chest": {
                "id": 46,
                "checkpoint": 9,
                "fm_rules": "fk | dt",
            },
            "Melon Chest": {
                "id": 47,
                "checkpoint": 10,
                "fm_rules": "fk | dt",
            }
        },
        "Missions": {
            "Collect All Fruits": {
                "id": 82,
                "checkpoint": 10,
                "fm_rules": "fk | dt",
            },
            "Score 25,000": {
                "id": 83,
                "checkpoint": 10,
                "fm_rules": "bb&rr&fk&ms&as&ss | bb&rr&fk&ms&os&ss | bb&rr&fk&ms&os&as | bb&rr&dt&ms&as&cs | bb&rr&dt&ms&ss | bb&rr&dt&ms&os",
                "am_rules": "sbb&dt&f&ms&as&cs | bb&fk&f&ms&as&cs | sbb&dt&f&ms&ss | bb&fk&f&ms&ss | sbb&dt&f&ms&os | bb&fk&f&ms&os",
            },
            "Time Trial": {
                "id": 84,
                "checkpoint": 10,
            }
        }
    },
    "Burning-Hot Beats": {
        "id": 32,
        "Clear": {
            "fm_rules": "bb",
        },
        "Gold Medal": {
            "fm_rules": "bb&rr",
            "am_rules": "bb",
        },
        "Collectibles": {},
        "Gashapons": {},
        "Missions": {
            "Don't Die": {
                "id": 85,
                "fm_rules": "bb",
            },
            "Time Trial": {
                "id": 86,
                "fm_rules": "bb",
            }
        }
    },
    "Sharks Everywhere": {
        "id": 33,
        "Checkpoints": {
            1: {},
            2: {
                "fm_rules": "dk | fk",
            },
            3: {},
            4: {},
            5: {},
            6: {},
        },
        "Clear": {
            "checkpoint": 6,
        },
        "Gold Medal": {
            "checkpoint": 6,
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
                "checkpoint": 3,
            },
            "Strawberry Chest": {
                "id": 49,
                "checkpoint": 4,
            },
            "Melon Chest": {
                "id": 50,
                "checkpoint": 6,
            }
        },
        "Missions": {
            "Collect All Fruits": {
                "id": 87,
                "checkpoint": 6,
            },
            "Score 24,000": {
                "id": 88,
                "checkpoint": 6,
                "fm_rules": "ms&as&os | ms&os&ss",
            },
            "Time Trial": {
                "id": 89,
                "checkpoint": 6,
            }
        }
    },
    "Pac-Marine Battle!": {
        "id": 34,
        "Clear": {},
        "Gold Medal": {},
        "Collectibles": {},
        "Gashapons": {},
        "Missions": {
            "Don't Die": {
                "id": 90,
            },
            "Time Trial": {
                "id": 91,
            }
        }
    },
    "Clumsy Bayou": {
        "id": 35,
        "Checkpoints": {
            1: {},
            2: {},
            3: {},
            4: {
                "fm_rules": "bb",
            },
            5: {},
            6: {},
            7: {},
            8: {},
            9: {},
            10: {
                "fm_rules": "rr | f",
                "am_rules": "fk | dt | sbb",
            },
            11: {},
            12: {},
            13: {
                "fm_rules": "rr",
                "am_rules": "dt",
            },
        },
        "Clear": {
            "checkpoint": 13,
        },
        "Gold Medal": {
            "checkpoint": 13,
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
                "checkpoint": 5,
                "fm_rules": "fk | dt",
                "am_rules": "sbb&f",
                "ag_rules": "sbb"
            },
            "Apple Chest": {
                "id": 52,
                "checkpoint": 12,
                "fm_rules": "fk | dt",
            },
            "Melon Chest": {
                "id": 53,
                "checkpoint": 13,
                "fm_rules": "sbb&fk | sbb&dt",
                "am_rules": "rr&fk | rr&dt&f",
                "ag_rules": "dt"
            }
        },
        "Missions": {
            "Collect All Fruits": {
                "id": 92,
                "checkpoint": 13,
                "fm_rules": "sbb&fk | sbb&dt",
                "am_rules": "rr&fk | rr&dt&f",
                "ag_rules": "dt"
            },
            "Defeat Enemies": {
                "id": 93,
                "checkpoint": 13,
                "fm_rules": "sbb&fk | sbb&dt",
                "am_rules": "rr&fk | rr&dt&f",
                "ag_rules": "dt"
            },
            "Time Trial": {
                "id": 94,
                "checkpoint": 13,
            }
        }
    },
    "Legendary Story": {
        "id": 36,
        "Clear": {
            "fm_rules": "sbb&fk&rr | sbb&dt&rr",
            "am_rules": "",
            "ag_rules": ""
        },
        "Gold Medal": {
            "fm_rules": "sbb&fk&rr | sbb&dt&rr",
            "am_rules": "",
            "ag_rules": ""
        },
        "Collectibles": {},
        "Gashapons": {},
        "Missions": {
            "Don't Die": {
                "id": 95,
                "fm_rules": "sbb&fk&rr | sbb&dt&rr",
                "am_rules": "",
                "ag_rules": ""
            },
            "Time Trial": {
                "id": 96,
                "fm_rules": "sbb&fk&rr | sbb&dt&rr",
                "am_rules": "",
                "ag_rules": ""
            }
        }
    },
    "Flying Dark Shadow": {
        "id": 37,
        "Clear": {
            "fm_rules": "sbb&rr&fk",
            "am_rules": "",
            "ag_rules": ""
        },
        "Gold Medal": {
            "fm_rules": "sbb&rr&fk",
            "am_rules": "",
            "ag_rules": ""
        },
        "Collectibles": {},
        "Gashapons": {},
        "Missions": {
            "Don't Die": {
                "id": 97,
                "fm_rules": "sbb&rr&fk",
                "am_rules": "",
                "ag_rules": ""
            },
            "Time Trial": {
                "id": 98,
                "fm_rules": "sbb&rr&fk",
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
    # "Street (Blue)": 4,
    # "Street (Red)": 5,
    # "Street (Pink)": 6,
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
    #"Toc-Man": 27,
    "Pac-Wizard": 28,
    "Orson": 29,
    #"Pac-Land": 30,
    "Spooky": 31,
    #No sonic dlc for you
    # "Holiday (Red)": 33,
    # "Holiday (Green)": 34,
    # "Holiday (Blue)": 35,
    # "Birthday Hat": 36
}

exc_costumes = {
    "excluded_costumes": [4, 5, 6, 27, 30, 32, 33, 34, 35, 36],
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
    "Flutter": 4,
    "Progressive Dolphin Kick": 5
}

filler_data = {
    "1 Pac-Dot": 0,
    "5 Pac-Dots": 1,
    "10 Pac-Dots": 2,
    "100 Points": 3,
    "200 Points": 4,
    "500 Points": 5,
    "1000 Points": 6,
    "Extra Life": 7,
}

trap_data = {
    "Voice line Trap": 0
}
