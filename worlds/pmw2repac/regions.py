from __future__ import annotations

from typing import TYPE_CHECKING

from . import data
from BaseClasses import Region, Entrance

if TYPE_CHECKING:
    from world import PMW2RepacWorld

def create_regions(world: PMW2RepacWorld) -> None:

    world_map = Region("World Map", world.player, world.multiworld)
    world.multiworld.regions.append(world_map)

    for level in data.level_data.keys():
        region = Region(level, world.player, world.multiworld)
        world.multiworld.regions.append(region)

        world_map.connect(region, "World Map to " + level)
