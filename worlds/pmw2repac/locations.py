from __future__ import annotations

from typing import TYPE_CHECKING

from . import data
from BaseClasses import ItemClassification, Location

if TYPE_CHECKING:
    from .world import PMW2RepacWorld

locations = {}

class PMW2RepacLocation(Location):
    game = "Pac-Man World 2 Re-Pac"

def define_locations() -> None:
    for level, levelData in data.level_data.items():
        if levelData["id"] > 0:
            locations[level + " - Clear"] = levelData["id"] + data.LEVEL_OFFSET

        for gashapon, gashapon_id in levelData["Gashapons"].items():
            locations[level + " - " + gashapon] = gashapon_id + data.GASHAPON_OFFSET

        for mission, mission_id in levelData["Missions"].items():
            locations[level + " - " + mission] = mission_id + data.MISSION_OFFSET

def create_locations(world: PMW2RepacWorld) -> None:
    for level, levelData in data.level_data.items():

        region = world.get_region(level)

        if level != "Pac-Village":
            location = PMW2RepacLocation(world.player, level + " - Clear", levelData["id"] + data.LEVEL_OFFSET, region)
            region.locations.append(location)

        for gashapon, gashapon_id in levelData["Gashapons"].items():
            location = PMW2RepacLocation(world.player, level + " - " + gashapon, gashapon_id + data.GASHAPON_OFFSET, region)
            region.locations.append(location)

        for mission, mission_id in levelData["Missions"].items():
            location = PMW2RepacLocation(world.player, level + " - "  + mission, mission_id + data.MISSION_OFFSET, region)
            region.locations.append(location)



