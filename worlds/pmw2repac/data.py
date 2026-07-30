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

level_data = {
    "Pac-Village": {
        "id": -1,
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
            "CollectAllFruit": 0
        }
    },
"The Bear Basics": {
        "id": 0,
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
            "Pac-Knight": 1,
            "Pac-Wizard": 2
        },
        "Missions":{
             #might need reworking
            "Clear Stage": 1,
            "Score 10,000": 2,
            "Collect All Fruit": 3
        }
    },
"Canyon Chaos": {
        "id": 1,
        "Collectibles":{
           #"Cherries" : 4,
           #"Strawberries" : 2,
           #"Oranges" : 3,
           #"Apples" : 4,
           #"Melons" : 6,
           #"Galaxian" : 1
        },
        "Gashapons":{
            "Stopwatch": 3,
            "Small PAC-MAN": 4
        },
        "Missions":{
            "Collect All Fruit": 4,
            "Destroy Traps": 5,
            "Time Trial": 6
        }
    },
"Pac-Dot Pond": {
        "id": 2,
        "Collectibles":{
           #"Cherries" : 0,
           #"Strawberries" : 0,
           #"Oranges" : 0,
           #"Apples" : 0,
           #"Melons" : 0,
           #"Galaxian" : 1
        },
        "Gashapons":{
            "Goal Coin": 5,
            "PAC-MAN (Silver)": 6
        },
        "Missions":{
            "Collect All Fruit": 7,
            "Defeat All Enemies": 8,
            "Time Trial": 9
        }
    },
"Clyde's Frog": {
        "id": 3,
        "Collectibles":{
           #"Cherries" : 0,
           #"Strawberries" : 0,
           #"Oranges" : 0,
           #"Apples" : 0,
           #"Melons" : 0,
           #"Galaxian" : 0
        },
        "Gashapons":{
        },
        "Missions":{
            "Don't Die": 10,
            "Time Trial": 11
        }
    }
}