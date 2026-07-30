from __future__ import annotations

from typing import TYPE_CHECKING

import data
from ...rule_builder.options import OptionFilter
from ...rule_builder.rules import Has, HasAll, Rule

if TYPE_CHECKING:
    from .world import PMW2RepacWorld


def set_all_rules(world: PMW2RepacWorld) -> None:
    set_location_rules(world)
    set_goal(world)

def set_location_rules(world: PMW2RepacWorld) -> None:
    #placeholder, will get used once fruit switches and/or move rando gets implemented
    i = 1

def set_goal(world: PMW2RepacWorld) -> None:
    #Defeat Spooky! Or Toc-Man when implementation is added.
    i = 1