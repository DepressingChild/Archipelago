from collections.abc import Mapping
from typing import Any

from ..AutoWorld import World
from . import items, locations, regions, rules, web_world
from . import options as opts

class PMW2RepacWorld(World):
    """Pac-Man World 2. Re-Pac!"""

    game = "Pac-Man World 2 Re-Pac"

    web = web_world.PMW2RepacWebWorld()

    options_dataclass = opts.PMW2RepacOptions
    options: opts.PMW2RepacOptions

    locations.define_locations()
    items.define_items()

    location_name_to_id = locations.locations
    item_name_to_id = items.items

    origin_region_name =  "World Map"

    def create_regions(self) -> None:
        regions.create_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.PMW2RepacItem:
        return items.create_item(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        return self.options.as_dict("goal_boss", "mission_checks", "gashapon_checks", "galaxian_checks", "gold_medal_checks","level_randomizer", "random_starting_levels", "move_randomizer", "moves_to_randomize", "logic_difficulty", "fruit_switches", "exclude_goal_locations", "pac_dot_weight", "points_weight", "trap_weight")