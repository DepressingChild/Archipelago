from __future__ import annotations

from typing import TYPE_CHECKING

from . import data
from BaseClasses import Region, Entrance

if TYPE_CHECKING:
    from world import PMW2RepacWorld

def create_and_connect_all_regions(world: PMW2RepacWorld) -> None:
    create_regions(world)
    create_checkpoint_regions(world)
    connect_specific_regions(world)

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

        # if world.options.level_randomizer == 0:
        #     world.multiworld.register_indirect_condition(region, entrance)

def create_checkpoint_regions(world: PMW2RepacWorld) -> None:

    for level, levelData in data.level_data.items():
        if world.options.goal_boss == 0 and levelData["id"] > data.level_data["Spooky"]["id"]: #we hate pac-village
            break
        if levelData["id"] == 0:
            continue

        for checkSet,  checkData in levelData.items():
            if checkSet == "Checkpoints":
                recursive_connect_checkpoints(world, level, len(checkData.keys()), 0)

def recursive_connect_checkpoints(world: PMW2RepacWorld, level: str, num_checkpoints: int, idx: int) -> None:
    if idx == num_checkpoints: return

    region = Region(level + " Checkpoint " + str((idx + 1)), world.player, world.multiworld)
    world.multiworld.regions.append(region)

    entrance: str
    reg = level
    if idx == 0:
        entrance = level + " to Checkpoint 1"
    else:
        entrance = level + " Checkpoint " + str(idx) + " to Checkpoint " + str((idx + 1))
        reg += " Checkpoint " + str(idx)
    world.get_region(reg).connect(region, entrance)
    recursive_connect_checkpoints(world, level, num_checkpoints, idx + 1)

def connect_specific_regions(world: PMW2RepacWorld) -> None:
    if world.options.logic_difficulty == 2:
        vp_c0 = world.get_region("Volcanic Panic")
        vp_c8 = world.get_region("Volcanic Panic Checkpoint 8")
        vp_c0.connect(vp_c8, "Volcanic Panic Checkpoint 0 to Checkpoint 8")

        hft_c0 = world.get_region("Hot! Fire Trouble")
        hft_c7 = world.get_region("Hot! Fire Trouble Checkpoint 7")
        hft_c0.connect(hft_c7, "Hot! Fire Trouble Checkpoint 0 to Checkpoint 7")
