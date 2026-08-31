from __future__ import annotations
from typing import TYPE_CHECKING

from . import data
from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import PMW2RepacWorld

class PMW2RepacItem(Item):
    game = "Pac-Man World 2 Re-Pac"

items = {}

def define_items() -> None:

    for level, levelData in data.level_data.items():
        items[level] = levelData["id"] + data.LEVEL_OFFSET

    for costume, costume_id in data.costume_data.items():
        items[costume + " costume"] = costume_id + data.COSTUME_OFFSET

    for golden_fruit, golden_fruit_id in data.golden_fruit_data.items():
        items[golden_fruit] = golden_fruit_id + data.GOLDEN_FRUIT_OFFSET

    for key, key_id in data.key_data.items():
        items[key] = key_id + data.KEY_OFFSET

    for fruit_switch, fruit_switch_id in data.fruit_switch_data.items():
        items[fruit_switch] = fruit_switch_id + data.FRUIT_SWITCH_OFFSET

    for movement, movement_id in data.movement_data.items():
        items[movement] = movement_id + data.MOVEMENT_OFFSET

    #Add item for goal level unlocks

    for filler, filler_id in data.filler_data.items():
        items[filler] = filler_id + data.FILLER_OFFSET

    for trap, trap_id in data.trap_data.items():
        items[trap] = trap_id + data.TRAP_OFFSET

#Need a separate function to create a single item.
def create_item(world: PMW2RepacWorld, name: str) -> PMW2RepacItem:
    item_id = items[name]

    #Once we figure out more items to add, make an offset for them then add them here. The range for if statements is item offset <= item_id < next item offset
    #Levels are progression
    if data.LEVEL_OFFSET <= item_id < data.GOLDEN_FRUIT_OFFSET: classification = ItemClassification.progression

    elif data.GOLDEN_FRUIT_OFFSET <= item_id < data.KEY_OFFSET: classification = ItemClassification.progression

    elif data.KEY_OFFSET <= item_id < data.COSTUME_OFFSET: classification = ItemClassification.progression

    elif data.COSTUME_OFFSET <= item_id < data.FRUIT_SWITCH_OFFSET: classification = ItemClassification.filler

    elif data.FRUIT_SWITCH_OFFSET <= item_id < data.MOVEMENT_OFFSET: classification = ItemClassification.progression

    elif data.MOVEMENT_OFFSET <= item_id < data.FILLER_OFFSET: classification = ItemClassification.progression

    elif data.FILLER_OFFSET <= item_id < data.TRAP_OFFSET: classification = ItemClassification.filler

    else: classification = ItemClassification.trap

    return PMW2RepacItem(name, classification, item_id, world.player)

def create_all_items(world: PMW2RepacWorld) -> None:

    starting_levels = ["Pac-Village"]

    itempool: list[Item] = []

    if world.options.level_randomizer:

        # For whatever reason, this segment has a chance to create a duplicate level
        # Running this same segment in a separate Python script does NOT produce these issues. Why? idfk.

        #Exclude levels from random starting levels
        #beatable_starting_levels = []

        if world.options.move_randomizer:
            if world.options.moves_to_randomize.__contains__("Butt Bounce") and world.options.moves_to_randomize.__contains__("Super Butt Bounce"):
                beatable_starting_levels = ["Ice River Run", "Blade Mountain", "Yellow Pac-Marine", "Whale on a Sub", "Haunted Boardwalk", "Pro Thunder Skater", "Pac-Marine Battle!"]
            else:
                beatable_starting_levels = ["The Bear Basics", "Canyon Chaos", "Clyde's Frog", "Ice River Run", "Blade Mountain", "Blinky in the Caldera", "Yellow Pac-Marine", "Whale on a Sub", "Haunted Boardwalk", "A Long Poisonous Tongue", "Pro Thunder Skater", "Burning-Hot Beats", "Pac-Marine Battle!"]
        else:
            excluded_levels = ["Pac-Village", "Spooky", "Legendary Story", "Flying Dark Shadow"]
            if world.options.goal_boss == 0:
                for level in data.level_data.keys():
                    if data.level_data[level]["id"] > data.level_data["Spooky"]["id"]:
                        excluded_levels.append(level)
            beatable_starting_levels = list(set(data.level_data.keys()) - set(excluded_levels))

        # for level in beatable_starting_levels:
        #     if world.options.goal_boss == 0 and data.level_data[level]["id"] > data.level_data["Spooky"]["id"]:
        #         beatable_starting_levels.remove(level)

        # Loop above does not work. idk why.
        world.random.shuffle(beatable_starting_levels)
        i = 0
        for level in beatable_starting_levels:
            if i >= world.options.random_starting_levels: break
            if world.options.goal_boss == 0 and data.level_data[level]["id"] > data.level_data["Spooky"]["id"]:
                continue
            else:
                starting_levels.append(level)
                i += 1

        for level in data.level_data.keys():
            if world.options.goal_boss == 0 and data.level_data[level]["id"] > data.level_data["Spooky"]["id"]:
                continue
            if level not in starting_levels:
                itempool.append(world.create_item(level))
    else:
        if world.options.move_randomizer:
            if world.options.moves_to_randomize.__contains__("Butt Bounce") and world.options.moves_to_randomize.__contains__("Super Butt Bounce"):
                world.options.moves_to_randomize.value.remove("Butt Bounce")

    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player)) - len(itempool)
    #Continue adding items, decrement number_of_unfilled_locations when a new item is added.
    for golden_fruit in data.golden_fruit_data.keys():
        itempool.append(world.create_item(golden_fruit))
        number_of_unfilled_locations -= 1

    if world.options.goal_boss == 1:
        for key in data.key_data.keys():
            itempool.append(world.create_item(key))
            number_of_unfilled_locations -= 1

    if world.options.fruit_switches:
        for fruit_switch in data.fruit_switch_data.keys():
            itempool.append(world.create_item(fruit_switch))
            number_of_unfilled_locations -= 1

    if world.options.move_randomizer:
        for move in world.options.moves_to_randomize:
            if move == "Butt Bounce" or move == "Super Butt Bounce":
                move = "Progressive Butt Bounce"
            if move == "Dolphin Kick" or move == "Super Dolphin Kick":
                move = "Progressive Dolphin Kick"
            itempool.append(world.create_item(move))
            number_of_unfilled_locations -= 1

    leftover_costumes = list(data.costume_data.keys())
    world.random.shuffle(leftover_costumes)
    for costume in leftover_costumes:
        if number_of_unfilled_locations <= 0: break
        itempool.append(world.create_item(costume + " costume"))
        leftover_costumes.remove(costume)
        number_of_unfilled_locations -= 1

    #At the end, add filler.
    itempool += [world.create_filler() for _ in range(number_of_unfilled_locations)]

    world.multiworld.itempool += itempool

    #Precollect starting levels
    if world.options.level_randomizer:
        for level in starting_levels:
            world.push_precollected(world.create_item(level))

    if world.options.move_randomizer:
        moves = set(data.movement_data.keys())
        moves.remove("Progressive Butt Bounce")
        moves.remove("Progressive Dolphin Kick")
        moves.add("Butt Bounce")
        moves.add("Super Butt Bounce")
        moves.add("Dolphin Kick")
        moves.add("Super Dolphin Kick")
        for move in moves:
            if move not in world.options.moves_to_randomize:
                if move == "Butt Bounce" or move == "Super Butt Bounce":
                    move = "Progressive Butt Bounce"
                if move == "Dolphin Kick" or move == "Super Dolphin Kick":
                    move = "Progressive Dolphin Kick"
                world.push_precollected(world.create_item(move))
    else:
        moves = set(data.movement_data.keys())
        moves.remove("Progressive Butt Bounce")
        moves.remove("Progressive Dolphin Kick")
        for move in moves:
            world.push_precollected(world.create_item(move))
        for _ in range(2):
            world.push_precollected(world.create_item("Progressive Butt Bounce"))
            world.push_precollected(world.create_item("Progressive Dolphin Kick"))


    if world.options.fruit_switches:
        fruit_switches = sorted(data.fruit_switch_data.keys())
        world.random.shuffle(fruit_switches)
        world.push_precollected(world.create_item(fruit_switches.pop()))
    else:
        for switch in data.fruit_switch_data.keys():
            world.push_precollected(world.create_item(switch))

    for costume in leftover_costumes:
        world.push_precollected(world.create_item(costume + " costume"))

def get_random_filler_item(world: PMW2RepacWorld) -> str:

    if world.random.randint(0, 99) < world.options.trap_weight:
        chance = 100 / len(data.trap_data)
        return world.random.choices(population=list(data.trap_data.keys()))[0]

    #Could change to make these individual option choices

    pacdot1 = world.options.pac_dot_weight * 0.5
    pacdot5 = world.options.pac_dot_weight * 0.3
    pacdot10 = world.options.pac_dot_weight * 0.2

    score100 = world.options.points_weight * .4
    score200 = world.options.points_weight * .3
    score500 = world.options.points_weight * .2
    score1000 = world.options.points_weight * .1

    weights = pacdot1 + pacdot5 + pacdot10 + score100 + score200 + score500 + score1000

    # If trap chance fails, send a filler item.
    if weights > 0:
        return world.random.choices(population=list(data.filler_data.keys()), weights=[pacdot1, pacdot5, pacdot10, score100, score200, score500, score1000], k=1)[0]


    # If all chances fail, send nothing.
    return "Nothing"


