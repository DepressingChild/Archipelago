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

    items["Nothing"] = data.FILLER_OFFSET

#Need a separate function to create a single item.
def create_item(world: PMW2RepacWorld, name: str) -> PMW2RepacItem:
    item_id = items[name]

    #Once we figure out more items to add, make an offset for them then add them here. The range for if statements is item offset <= item_id < next item offset
    #Levels are progression
    if data.LEVEL_OFFSET <= item_id < data.FILLER_OFFSET: classification = ItemClassification.progression

    else: classification = ItemClassification.filler

    return PMW2RepacItem(name, classification, item_id, world.player)

def create_all_items(world: PMW2RepacWorld) -> None:

    starting_levels = ["Pac-Village", "The Bear Basics"]

    itempool: list[Item] = []

    for level, levelData in data.level_data.items():
        if world.options.level_randomizer:
            if level not in starting_levels:
                itempool.append(world.create_item(level))

    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player)) - len(itempool)
    #Continue adding items, decrement number_of_unfilled_locations when a new item is added.

    #At the end, add filler.
    itempool += [world.create_filler() for _ in range(number_of_unfilled_locations)]

    world.multiworld.itempool += itempool

    #Precollect starting levels
    if world.options.level_randomizer:
        for level in starting_levels:
            world.push_precollected(world.create_item(level))
    else:
        for level in data.level_data.keys():
            world.push_precollected(world.create_item(level))

def get_random_filler_item(world: PMW2RepacWorld) -> str:
    return "Nothing"


