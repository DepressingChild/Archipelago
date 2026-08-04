from dataclasses import dataclass

from Options import Choice, OptionGroup, OptionSet, Range, Toggle, PerGameCommonOptions, DeathLink

class GoalBoss(Choice):
    """
    Choose a goal boss. Spooky goal will not include post-game levels & items.
    """

    display_name = "Goal Boss"
    option_Spooky = 0
    option_TocMan = 1

class LevelRandomizer(Toggle):
    """
    Levels get randomized into the item pool instead of unlocking them with Golden Fruits or Keys.
    """

    display_name = "Level Randomizer"

class RandomStartingLevels(Range):
    """
    If level_randomizer is enabled, you can choose how many levels you start with.
    Does nothing if level_randomizer is disabled.
    """

    display_name = "Number of Starting Levels"
    range_start = 1
    range_end = 5
    default = 3

class MoveRandomizer(Toggle):
    """
    Movement abilities will get randomized into the item pool.
    If level_randomizer is disabled, you will receive Butt Bounce at the start to prevent a restrictive start.
    """

    display_name = "Move Randomizer"

class MovesToRandomize(OptionSet):
    """
    If move_randomizer is enabled, you can choose which moves get randomized into the item pool.
    Moves not listed are given at the start.

    Note: It is recommended to start with Butt Bounce.

    Does nothing if move_randomizer is disabled.
    """

    display_name = "Moves to Randomize"
    default = ["Super Butt Bounce", "Flip Kick", "Rev Roll", "Pac-Dot Attack", "Flutter"]

class FruitSwitches(Toggle):
    """
    Adds fruit switches to the items pool. Disables fruit of that type until the respective switch is found.
    1 fruit switch will be enabled at the start.
    """
    display_name = "Fruit Switches"

#class Fruitsanity(Toggle):
    #"""
    #Every fruit is a check. Adds x checks
    #"""

    #display_name = "Fruitsanity"

@dataclass
class PMW2RepacOptions(PerGameCommonOptions):
    goal_boss: GoalBoss
    level_randomizer: LevelRandomizer
    random_starting_levels: RandomStartingLevels
    move_randomizer: MoveRandomizer
    moves_to_randomize: MovesToRandomize
    fruit_switches: FruitSwitches
    #fruitsanity: Fruitsanity

#Stuff below is for the website.
options_groups = [

]

option_presets = {

}