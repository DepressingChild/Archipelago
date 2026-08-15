from __future__ import annotations

from typing import TYPE_CHECKING

from . import data
from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule, True_, False_

if TYPE_CHECKING:
    from .world import PMW2RepacWorld

rule_convert = {
    "bb": Has("Progressive Butt Bounce"),
    "sbb": Has("Progressive Butt Bounce", count=2),
    "fk": Has("Flip Kick"),
    "rr": Has("Rev Roll"),
    "dt": Has("Pac-Dot Attack"),
    "f": Has("Flutter"),

    "cs": Has("Cherry Switch"),
    "ss": Has("Strawberry Switch"),
    "os": Has("Orange Switch"),
    "as": Has("Apple Switch"),
    "ms": Has("Melon Switch")
}

hasAllGoldenFruits = HasAll("Golden Cherry", "Golden Strawberry", "Golden Apple", "Golden Orange", "Golden Melon")
hasAllKeys = HasAll("Windy Woods Key", "Thunder Snow Mountain Key", "Fiery Caverns Key", "Dim Underwaters Key", "Ghost Island Key")
hasAllFruitSwitches = HasAll("Cherry Switch", "Strawberry Switch", "Orange Switch", "Apple Switch", "Melon Switch")

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
            if world.options.goal_boss == 0 and levelData["id"] > data.level_data["Spooky"]["id"]:
                break

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
    for level, levelData in data.level_data.items():
        for checkSet, checkData in levelData.items():
            if checkSet == "id" or "Clear": continue

            for check, ruleData in checkData.items():
                for rulesType, rules in ruleData.items():
                    if rulesType == "id": continue
                    location = level + " - "
                    if checkSet == "Collectibles":
                        location += check
                    else:
                        location += checkSet[:-1] + " - " + check
                        is_all_fruits = check == "Collect All Fruits"
                        set_rule_with_strings(world, rules, rulesType, location, is_all_fruits)

        if level == "Pac-Village": continue
        for rulesType, rules in levelData["Clear"].items():
            location = level + " - Clear"
            set_rule_with_strings(world, rules, rulesType, location, False)






def set_goal(world: PMW2RepacWorld) -> None:
    #Change when we have to collect a goal item
    if world.options.goal_boss.value == 0:
        world.set_completion_rule(hasAllGoldenFruits)
        if world.options.level_randomizer:
            world.set_completion_rule(Has("Spooky"))
    else:
        world.set_completion_rule(hasAllGoldenFruits & hasAllKeys) #use events for this
        if world.options.level_randomizer:
            world.set_completion_rule(HasAll("Spooky", "Legendary Story", "Flying Dark Shadow"))

def set_rule_with_strings(world: PMW2RepacWorld, rules: str, rules_type: str, location: str, is_all_fruits: bool) -> None:
    rules_string = ""
    if rules_type == "fm_rules":
        rules_string += rules
    if rules_type == "am_rules" and world.options.logic_difficulty > 0:
        rules_string += " | " + rules
    if rules_type == "ag_rules" and world.options.logic_difficulty == 2:
        rules_string += " | " + rules
    if rules_string == "": return

    single_rules = []
    final_rule = False_()
    split_rules = rules_string.split(" | ")
    for rule in split_rules:
        single_rule = True_()
        if is_all_fruits:
            single_rule = hasAllFruitSwitches
        moves = rule.split("&")
        for move in moves:
            if move == "": continue
            single_rule = single_rule & rule_convert[move]
        single_rules.append(single_rule)

    if "NONE" in single_rules: return
    for rule in single_rules:
        final_rule = final_rule | rule
    # print(location)
    # print(final_rule)
    world.set_rule(world.get_location(location), final_rule)