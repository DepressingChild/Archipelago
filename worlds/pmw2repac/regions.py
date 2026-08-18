from __future__ import annotations

from typing import TYPE_CHECKING

from . import data
from BaseClasses import Region, Entrance

if TYPE_CHECKING:
    from world import PMW2RepacWorld

def create_regions(world: PMW2RepacWorld) -> None:

    world_map = Region("World Map", world.player, world.multiworld)
    world.multiworld.regions.append(world_map)

    for level, levelData in data.level_data.items():
        if world.options.goal_boss == 0 and levelData["id"] > data.level_data["Spooky"]["id"]:
            break

        region = Region(level, world.player, world.multiworld)
        world.multiworld.regions.append(region)

        entrance = "World Map to " + level
        world_map.connect(region, entrance)

        if world.options.level_randomizer == 0:
            world.multiworld.register_indirect_condition(region, entrance)
