from typing import TYPE_CHECKING

from data import level_data, GASHAPON_OFFSET, MISSION_OFFSET
from ...BaseClasses import ItemClassification, Location
from . import items

if TYPE_CHECKING:
    from .world import PMW2RepacWorld

class PMW2RepacLocation(Location):
    game = "Pac-Man World 2 Re-Pac"


def create_locations(world: PMW2RepacWorld) -> None:

    for level in level_data.keys():
        region = world.get_region(level)

        for gashapon in level_data["gashapons"]:
            location = PMW2RepacLocation(world.player, gashapon, gashapon.value + GASHAPON_OFFSET, level)
            region.add_location(location)

        for mission in level_data["missions"]:
            location = PMW2RepacLocation(world.player, mission, mission.value + MISSION_OFFSET, level)
            region.add_location(location)



