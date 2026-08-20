from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance

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
    "dk": Has("Progressive Dolphin Kick"),
    "sdk": Has("Progressive Dolphin Kick", count=2),

    "cs": Has("Cherry Switch"),
    "ss": Has("Strawberry Switch"),
    "os": Has("Orange Switch"),
    "as": Has("Apple Switch"),
    "ms": Has("Melon Switch")
}

hasAllGoldenFruits = HasAll("Golden Cherry", "Golden Strawberry", "Golden Apple", "Golden Orange", "Golden Melon")
hasAllKeys = HasAll("Windy Woods Key", "Thunder Snow Mountain Key", "Fiery Caverns Key", "Dim Underwaters Key", "Ghost Island Key")
hasAllFruitSwitches = HasAll("Cherry Switch", "Strawberry Switch", "Orange Switch", "Apple Switch", "Melon Switch")
canBeatSpooky = (rule_convert["sbb"] & rule_convert["rr"] & rule_convert["fk"]) | (rule_convert["sbb"] & rule_convert["rr"] & rule_convert["dt"])
canBeatTocMan = rule_convert["sbb"] & rule_convert["fk"]

def set_all_rules(world: PMW2RepacWorld) -> None:
    set_entrance_rules(world)
    set_specific_entrance_rules(world)
    set_location_rules(world)
    set_goal(world)

def set_entrance_rules(world: PMW2RepacWorld) -> None:
    if world.options.level_randomizer:
        for level, levelData in data.level_data.items():
            if world.options.goal_boss == 0 and levelData["id"] > data.level_data["Spooky"]["id"]:
                break

            entrance = world.get_entrance("World Map to " + level)
            world.set_rule(entrance, Has(level))
    else:
        level_clear_rules = []
        for level, levelData in data.level_data.items():

            if world.options.goal_boss == 0 and levelData["id"] > data.level_data["Spooky"]["id"]:
                break

            # if level == "Spooky" or level == "Legendary Story" or level == "Flying Dark Shadow":
            #     continue

            # print("Not level randomizer")
            item_rule = True_()
            if levelData["id"] > data.level_data["Legendary Story"]["id"]:
                i = 0
                #world.set_rule(entrance, Has(""))
            elif levelData["id"] > data.level_data["Pac-Marine Battle!"]["id"]:
                item_rule = Has("Ghost Island Key")
            elif levelData["id"] > data.level_data["Burning-Hot Beats"]["id"]:
                item_rule = Has("Dim Underwaters Key")
            elif levelData["id"] > data.level_data["Boom! Boom! Clap!"]["id"]:
                item_rule = Has("Fiery Caverns")
            elif levelData["id"] > data.level_data["Hunter of Darkness"]["id"]:
                item_rule = Has("Thunder Snow Mountain Key")
            elif levelData["id"] > data.level_data["A Long Poisonous Tongue"]["id"]:
                item_rule = Has("Windy Woods Key")
            elif levelData["id"] > data.level_data["Spooky"]["id"]:
                item_rule = hasAllGoldenFruits
            elif levelData["id"] > data.level_data["Whale on a Sub"]["id"]:
                item_rule = Has("Golden Melon")
            elif levelData["id"] > data.level_data["Blinky in the Caldera"]["id"]:
                item_rule = Has("Golden Orange")
            elif levelData["id"] > data.level_data["Pinky's Revenge"]["id"]:
                item_rule = Has("Golden Apple")
            elif levelData["id"] > data.level_data["Inky's Whimsy"]["id"]:
                item_rule = Has("Golden Strawberry")
            elif levelData["id"] > data.level_data["Clyde's Frog"]["id"]:
                item_rule = Has("Golden Cherry")

            for rule in level_clear_rules:
                item_rule = item_rule & rule
            entrance = world.get_entrance("World Map to " + level)

            world.set_rule(entrance, item_rule)

            rules_string = ""
            if level != "Pac-Village":
                for rulesType, rules in levelData["Clear"].items():
                    if rulesType == "fm_rules":
                        rules_string += rules
                    if rulesType == "am_rules" and world.options.logic_difficulty > 0:
                        rules_string += " | " + rules
                    if rulesType == "ag_rules" and world.options.logic_difficulty == 2:
                        rules_string += " | " + rules
                    if rules_string == "": continue

            clear_rule = create_rule_with_strings(world, rules_string, level + " - Clear", False)
            level_clear_rules.append(clear_rule)

            #clear level_clear_rules once certain areas are reached.
            if levelData["id"] % 4 == 0 and levelData["id"] < data.level_data["Spooky"]["id"]:
                level_clear_rules.clear()
            if levelData["id"] == data.level_data["Ghost Bayou"]["id"]:
                level_clear_rules.clear()
            if levelData["id"] % 2 == 0 and levelData["id"] > data.level_data["A Long Poisonous Tongue"]["id"]:
                level_clear_rules.clear()

def set_specific_entrance_rules(world: PMW2RepacWorld) -> None:
    world.set_rule(world.get_entrance("World Map to Spooky"), hasAllGoldenFruits)

    if world.options.level_randomizer:
        world.set_rule(world.get_entrance("World Map to Spooky"), hasAllGoldenFruits & Has("Spooky"))
    else:
        world.set_rule(world.get_entrance("World Map to Spooky"), hasAllGoldenFruits)

    if world.options.goal_boss == 1:
        if world.options.level_randomizer:
            world.set_rule(world.get_entrance("World Map to Legendary Story"), hasAllGoldenFruits & Has("Legendary Story"))
            world.set_rule(world.get_entrance("World Map to Flying Dark Shadow"), hasAllGoldenFruits & Has("Flying Dark Shadow"))
        else:
            world.set_rule(world.get_entrance("World Map to Legendary Story"), hasAllGoldenFruits)
            world.set_rule(world.get_entrance("World Map to Flying Dark Shadow"), hasAllGoldenFruits)

        world.set_rule(world.get_entrance("World Map to Legendary Story"), hasAllKeys)
        world.set_rule(world.get_entrance("World Map to Flying Dark Shadow"), hasAllGoldenFruits & hasAllKeys)

def set_location_rules(world: PMW2RepacWorld) -> None:
    level_clear_rules = []
    for level, levelData in data.level_data.items():
        for checkSet, checkData in levelData.items():
            if checkSet == "id" or checkSet == "Clear": continue

            for check, ruleData in checkData.items():
                rules_string = ""
                loc = level + " - "
                if checkSet == "Collectibles":
                    loc += check
                else:
                    loc += checkSet[:-1] + " - " + check

                is_all_fruits = check == "Collect All Fruits"

                for rulesType, rules in ruleData.items():
                    if rulesType == "id": continue

                    if rulesType == "fm_rules":
                        rules_string += rules
                    if rulesType == "am_rules" and world.options.logic_difficulty > 0:
                        rules_string += " | " + rules
                    if rulesType == "ag_rules" and world.options.logic_difficulty == 2:
                        rules_string += " | " + rules
                    if rules_string == "": continue

                try:
                    location = world.get_location(loc)
                    world.set_rule(location, create_rule_with_strings(world, rules_string, loc, is_all_fruits))
                except KeyError:
                    pass

        if level == "Pac-Village": continue
        #ik this is duplicated but who cares
        rules_string = ""
        for rulesType, rules in levelData["Clear"].items():

            if rulesType == "fm_rules":
                rules_string += rules
            if rulesType == "am_rules" and world.options.logic_difficulty > 0:
                rules_string += " | " + rules
            if rulesType == "ag_rules" and world.options.logic_difficulty == 2:
                rules_string += " | " + rules
            if rules_string == "": continue

        try:
            loc = level + " - Clear"
            location = world.get_location(loc)
            world.set_rule(location, create_rule_with_strings(world, rules_string, loc, False))
        except KeyError:
            pass

def set_goal(world: PMW2RepacWorld) -> None:
    #Change when we have to collect a goal item
    if world.options.goal_boss.value == 0:
        world.set_completion_rule(hasAllGoldenFruits)
        if world.options.level_randomizer:
            world.set_completion_rule(Has("Spooky") & hasAllGoldenFruits & canBeatSpooky)
    else:
        world.set_completion_rule(hasAllGoldenFruits & hasAllKeys) #use events for this
        if world.options.level_randomizer:
            world.set_completion_rule(HasAll("Spooky", "Legendary Story", "Flying Dark Shadow") & hasAllGoldenFruits & hasAllKeys & canBeatSpooky & canBeatTocMan)

def create_rule_with_strings(world: PMW2RepacWorld, rules_string: str, location: str, is_all_fruits: bool) -> Rule:

    single_rules = []
    final_rule = False_()
    split_rules = rules_string.split(" | ")
    for rule in split_rules:
        single_rule = True_()
        if is_all_fruits:
            single_rule = hasAllFruitSwitches
        if location.__contains__("Gashapon"):
            if location.__contains__("Cherry"):
                rule += "&cs"
            elif location.__contains__("Strawberry"):
                rule += "&ss"
            elif location.__contains__("Orange"):
                rule += "&os"
            elif location.__contains__("Apple"):
                rule += "&as"
            elif location.__contains__("Melon"):
                rule += "&ms"
        moves = rule.split("&")
        for move in moves:
            if move == "": continue
            single_rule = single_rule & rule_convert[move]

        single_rules.append(single_rule)

    #if "NONE" in single_rules: return
    for rule in single_rules:
        final_rule = final_rule | rule

    return final_rule