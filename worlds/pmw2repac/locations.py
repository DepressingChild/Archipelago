from __future__ import annotations

from typing import TYPE_CHECKING

from data import level_data, GASHAPON_OFFSET, MISSION_OFFSET, LEVEL_OFFSET
from ...BaseClasses import ItemClassification, Location
from . import items

if TYPE_CHECKING:
    from .world import PMW2RepacWorld

class PMW2RepacLocation(Location):
    game = "Pac-Man World 2 Re-Pac"


def create_locations(world: PMW2RepacWorld) -> None:
    for level, data in level_data.items():

        region = world.get_region(level)

        if level != "Pac-Village":
            location = PMW2RepacLocation(world.player, level + " - Clear", data["id"] + LEVEL_OFFSET, region)
            region.add_location(location)

        for gashapon, gashapon_id in data["gashapons"].items():
            location = PMW2RepacLocation(world.player, level + " - " + gashapon, gashapon_id + GASHAPON_OFFSET, region)
            region.add_location(location)

        for mission, mission_id in data["missions"].items():
            location = PMW2RepacLocation(world.player, level + " - "  + mission, mission_id + MISSION_OFFSET, region)
            region.add_location(location)



