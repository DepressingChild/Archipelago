from __future__ import annotations

from typing import TYPE_CHECKING

from . import data
from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule

if TYPE_CHECKING:
    from .world import PMW2RepacWorld


def set_all_rules(world: PMW2RepacWorld) -> None:
    set_entrance_rules(world)
    set_location_rules(world)
    set_goal(world)

def set_entrance_rules(world: PMW2RepacWorld) -> None:



    if world.options.level_randomizer:
        for level in data.level_data.keys():
            entrance = world.get_entrance("World Map to " + level)
            world.set_rule(entrance, Has(level))
    else:
        for level, levelData in data.level_data.items():
            entrance = world.get_entrance("World Map to " + level)

            if levelData["id"] > data.level_data["Legendary Story"]["id"]:
                i = 0
                #world.set_rule(entrance, Has(""))
            elif levelData["id"] > data.level_data["Pac-Marine Battle!"]["id"]:
                world.set_rule(entrance, Has("Ghost Island Key"))
            elif levelData["id"] > data.level_data["Burning-Hot Beats"]["id"]:
                world.set_rule(entrance, Has("Dim Underwaters Key"))
            elif levelData["id"] > data.level_data["Boom! Boom! Clap!"]["id"]:
                world.set_rule(entrance, Has("Fiery Caverns Key"))
            elif levelData["id"] > data.level_data["Hunter of Darkness"]["id"]:
                world.set_rule(entrance, Has("Thunder Snow Mountain Key"))
            elif levelData["id"] > data.level_data["A Long Poisonous Tongue"]["id"]:
                world.set_rule(entrance, Has("Windy Woods Key"))
            elif levelData["id"] > data.level_data["Spooky"]["id"]:
                world.set_rule(entrance, HasAll("Golden Cherry", "Golden Strawberry", "Golden Apple", "Golden Orange", "Golden Melon")) #will change this to event soon
            elif levelData["id"] > data.level_data["Whale on a Sub"]["id"]:
                world.set_rule(entrance, Has("Golden Melon"))
            elif levelData["id"] > data.level_data["Blinky in the Caldera"]["id"]:
                world.set_rule(entrance, Has("Golden Orange"))
            elif levelData["id"] > data.level_data["Pinky's Revenge"]["id"]:
                world.set_rule(entrance, Has("Golden Apple"))
            elif levelData["id"] > data.level_data["Inky's Whimsy"]["id"]:
                world.set_rule(entrance, Has("Golden Strawberry"))
            elif levelData["id"] > data.level_data["Clyde's Frog"]["id"]:
                world.set_rule(entrance, Has("Golden Cherry"))


def set_location_rules(world: PMW2RepacWorld) -> None:
    #placeholder
    i = 1

def set_goal(world: PMW2RepacWorld) -> None:
    #Defeat Spooky! Or Toc-Man when implementation is added.

    #Change when we have to collect a goal item
    if world.options.goal_boss.value == 0:
        world.set_completion_rule(HasAll("Golden Cherry", "Golden Strawberry", "Golden Apple", "Golden Orange", "Golden Melon"))
    else:
        world.set_completion_rule(HasAll("Golden Cherry", "Golden Strawberry", "Golden Apple", "Golden Orange", "Golden Melon")) #use events for this