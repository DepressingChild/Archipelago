from __future__ import annotations

from typing import TYPE_CHECKING

from . import data, items
from BaseClasses import ItemClassification, Location

if TYPE_CHECKING:
    from .world import PMW2RepacWorld

locations = {}

class PMW2RepacLocation(Location):
    game = "Pac-Man World 2 Re-Pac"

def create_all_locations(world: PMW2RepacWorld) -> None:
    create_locations(world)
    create_events(world)

def define_locations() -> None:
    for level, levelData in data.level_data.items():
        if levelData["id"] > 0:
            locations[level + " - Clear"] = levelData["id"] + data.LEVEL_OFFSET

        for gashapon, gashapon_id in levelData["Gashapons"].items():
            locations[level + " - Gashapon - " + gashapon] = gashapon_id + data.GASHAPON_OFFSET

        for mission, mission_id in levelData["Missions"].items():
            locations[level + " - Mission - " + mission] = mission_id + data.MISSION_OFFSET

def create_locations(world: PMW2RepacWorld) -> None:
    for level, levelData in data.level_data.items():

        region = world.get_region(level)
        if world.options.goal_boss == 0 and levelData["id"] > data.level_data["Spooky"]["id"]:
            break

        if levelData["id"] > 0:

            location = PMW2RepacLocation(world.player, level + " - Clear", levelData["id"] + data.LEVEL_OFFSET, region)
            region.locations.append(location)

        for gashapon, gashapon_id in levelData["Gashapons"].items():
                location = PMW2RepacLocation(world.player, level + " - Gashapon - " + gashapon, gashapon_id + data.GASHAPON_OFFSET, region)
                region.locations.append(location)

        for mission, mission_id in levelData["Missions"].items():
            location = PMW2RepacLocation(world.player, level + " - Mission - "  + mission, mission_id + data.MISSION_OFFSET, region)
            region.locations.append(location)

        #Add galaxian locations

        #Add fruit locations

def create_events(world: PMW2RepacWorld) -> None:
    i = 1
    #spooky = world.get_region("Spooky")
    #spooky.add_event("Defeat Spooky", "Spooky Defeated", location_type=PMW2RepacLocation, item_type=items.PMW2RepacItem)
    #spooky2 = world.get_region("Legendary Story")
    #spooky2.add_event("Defeat Spooky 2", "Spooky 2 Defeated", location_type=PMW2RepacLocation, item_type=items.PMW2RepacItem)


