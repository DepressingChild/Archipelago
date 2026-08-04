from __future__ import annotations
from typing import TYPE_CHECKING

from . import data
from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import PMW2RepacWorld

class PMW2RepacItem(Item):
    game = "Pac-Man World 2 Re-Pac"

items = {}

def define_items() -> None:

    for level, levelData in data.level_data.items():
        items[level] = levelData["id"] + data.LEVEL_OFFSET

    for costume, costume_id in data.costume_data.items():
        items[costume] = costume_id + data.COSTUME_OFFSET

    for golden_fruit, golden_fruit_id in data.golden_fruit_data.items():
        items[golden_fruit] = golden_fruit_id + data.GOLDEN_FRUIT_OFFSET

    for key, key_id in data.key_data.items():
        items[key] = key_id + data.KEY_OFFSET

    for fruit_switch, fruit_switch_id in data.fruit_switch_data.items():
        items[fruit_switch] = fruit_switch_id + data.FRUIT_SWITCH_OFFSET

    for movement, movement_id in data.movement_data.items():
        items[movement] = movement_id + data.MOVEMENT_OFFSET

    #Add item for goal level unlocks

    #Define single item for each unique filler/trap
    items["Nothing"] = data.FILLER_OFFSET

#Need a separate function to create a single item.
def create_item(world: PMW2RepacWorld, name: str) -> PMW2RepacItem:
    item_id = items[name]

    #Once we figure out more items to add, make an offset for them then add them here. The range for if statements is item offset <= item_id < next item offset
    #Levels are progression
    if data.LEVEL_OFFSET <= item_id < data.GOLDEN_FRUIT_OFFSET: classification = ItemClassification.progression

    elif data.GOLDEN_FRUIT_OFFSET <= item_id < data.KEY_OFFSET: classification = ItemClassification.progression

    elif data.KEY_OFFSET <= item_id < data.COSTUME_OFFSET: classification = ItemClassification.progression

    elif data.COSTUME_OFFSET <= item_id < data.FRUIT_SWITCH_OFFSET: classification = ItemClassification.filler

    elif data.FRUIT_SWITCH_OFFSET <= item_id < data.MOVEMENT_OFFSET: classification = ItemClassification.progression

    elif data.MOVEMENT_OFFSET <= item_id < data.FILLER_OFFSET: classification = ItemClassification.progression

    else: classification = ItemClassification.filler

    return PMW2RepacItem(name, classification, item_id, world.player)

def create_all_items(world: PMW2RepacWorld) -> None:

    starting_levels = {"Pac-Village"}

    itempool: list[Item] = []

    if world.options.level_randomizer:
        excluded_levels = {"Pac-Village", "Spooky", "Legendary Story", "Flying Dark Shadow"}
        if world.options.goal_boss == 0:
            for level in data.level_data.keys():
                if data.level_data[level]["id"] > data.level_data["Spooky"]["id"]:
                    excluded_levels.add(level)

        level_names = sorted(set(data.level_data.keys()) - excluded_levels)
        world.random.shuffle(level_names)
        for _ in range(world.options.random_starting_levels - 1):
            starting_levels.add(level_names.pop())

        for level, levelData in data.level_data.items():
            if level not in starting_levels:
                itempool.append(world.create_item(level))

    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player)) - len(itempool)
    #Continue adding items, decrement number_of_unfilled_locations when a new item is added.
    for golden_fruit in data.golden_fruit_data.keys():
        itempool.append(world.create_item(golden_fruit))
        number_of_unfilled_locations -= 1

    if world.options.goal_boss == 1:
        for key in data.key_data.keys():
            itempool.append(world.create_item(key))
            number_of_unfilled_locations -= 1

    if world.options.fruit_switches:
        for fruit_switch in data.fruit_switch_data.keys():
            itempool.append(world.create_item(fruit_switch))
            number_of_unfilled_locations -= 1

    if world.options.move_randomizer:
        for move in world.options.moves_to_randomize:
            if move == "Butt Bounce" or move == "Super Butt Bounce":
                move = "Progressive Butt Bounce"
            itempool.append(world.create_item(move))
            number_of_unfilled_locations -= 1

    for costume in data.costume_data.keys():
        itempool.append(world.create_item(costume))
        number_of_unfilled_locations -= 1

    #At the end, add filler.
    itempool += [world.create_filler() for _ in range(number_of_unfilled_locations)]

    world.multiworld.itempool += itempool

    #Precollect starting levels
    if world.options.level_randomizer:
        for level in starting_levels:
            world.push_precollected(world.create_item(level))
    # else:
        # for level in data.level_data.keys():
        #     if data.level_data[level]["id"] <= data.level_data["Clyde's Frog"]["id"]:
        #         world.push_precollected(world.create_item(level))

    if world.options.move_randomizer:
        for move in world.options.moves_to_randomize - data.movement_data.keys() - {"Butt Bounce", "Super Butt Bounce"}:
            if move == "Butt Bounce" or move == "Super Butt Bounce":
                move = "Progressive Butt Bounce"
            world.push_precollected(world.create_item(move))

    if world.options.fruit_switches:
        fruit_switches = sorted(data.level_data.keys())
        world.random.shuffle(fruit_switches)
        world.push_precollected(world.create_item(fruit_switches.pop()))

def get_random_filler_item(world: PMW2RepacWorld) -> str:
    return "Nothing"


