from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle, DeathLink

class LevelRandomizer(Toggle):
    """
    Levels get randomized into the item pool.
    """

    display_name = "Level Randomizer"

@dataclass
class PMW2RepacOptions(PerGameCommonOptions):
    level_randomizer: LevelRandomizer

#Stuff below is for the website.
options_groups = [

]

option_presets = {

}