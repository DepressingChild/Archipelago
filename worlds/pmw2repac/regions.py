from typing import TYPE_CHECKING
from ...BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from world import PMW2RepacWorld

def create_and_connect_regions(world: PMW2RepacWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: PMW2RepacWorld) -> None:
    pacvillage = Region("Pac-Village", world.player, world.multiworld)
    the_bear_basics = Region("The Bear Basics", world.player, world.multiworld)
    canyon_chaos = Region("Canyon Chaos", world.player, world.multiworld)
    pacdot_pond = Region("Pac-Dot Pond", world.player, world.multiworld)
    clydes_frog = Region("Clyde's Frog", world.player, world.multiworld)

    regions = [pacvillage, the_bear_basics, canyon_chaos, pacdot_pond, clydes_frog]


    world.multiworld.regions += regions

def connect_regions(world: PMW2RepacWorld) -> None:
    pacvillage = world.get_region("Pac-Village")
    the_bear_basics = world.get_region("The Bear Basics")
    canyon_chaos = world.get_region("Canyon Chaos")
    pacdot_pond = world.get_region("Pac-Dot Pond")
    clydes_frog = world.get_region("Clyde's Frog")