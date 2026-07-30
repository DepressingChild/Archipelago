from __future__ import annotations
from typing import TYPE_CHECKING

from data import level_data, LEVEL_OFFSET, FILLER_OFFSET
from ...BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import PMW2RepacWorld

class PMW2RepacItem(Item):
    game = "Pac-Man World 2 Re-Pac"

items = {}

def define_items(world: PMW2RepacWorld) -> None:

    for level, data in level_data.items():
        items[level] = data["id"] + LEVEL_OFFSET

    items["Nothing"] = FILLER_OFFSET

#Need a separate function to create a single item.
def create_item(world: PMW2RepacWorld, name: str) -> PMW2RepacItem:
    item_id = items[name]

    #Once we figure out more items to add, make an offset for them then add them here. The range for if statements is item offset <= item_id < next item offset
    #Levels are progression
    if LEVEL_OFFSET <= item_id < FILLER_OFFSET: classification = ItemClassification.progression

    else: classification = ItemClassification.filler

    return PMW2RepacItem(name, classification, item_id, world.player)

def create_all_items(world: PMW2RepacWorld) -> None:

    starting_levels = ["Pac-Village", "The Bear Basics"]

    itempool: list[Item] = []

    for level, data in level_data.items():
        if level not in starting_levels:
            itempool.append(create_item(world, level))

    #Continue adding items

    #At the end, add filler.
    number_of_filler_items = len(world.multiworld.get_unfilled_locations(world.player)) - len(itempool)
    itempool += [world.create_filler() for _ in range(number_of_filler_items)]

    #Precollect starting levels
    for level in starting_levels:
        world.push_precollected(world.create_item(level))

def get_random_filler_item(world: PMW2RepacWorld) -> str:
    return "Nothing"


