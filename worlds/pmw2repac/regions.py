from typing import TYPE_CHECKING

from data import level_data
from ...BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from world import PMW2RepacWorld

def create_regions(world: PMW2RepacWorld) -> None:

    world_map = Region("World Map", world.player, world.multiworld)
    world.multiworld.add_region(world_map)

    for level in level_data.keys():
        region = Region(level, world.player, world.multiworld)
        world.multiworld.add_region(region)

        #Also sets a rule to make sure the stage is out of logic if you don't have it unlocked.
        world_map.connect(region, "World Map to " + level, lambda state: state.has(level, world.player))
