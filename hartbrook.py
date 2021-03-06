
import tcod

from entity import Entity
from engine import Engine
from gamemap import Map

from typing import Tuple

from input_handlers import EventHandler

def main() -> None:
    screen_width = 100
    screen_height = 80

    mapwidth = 100
    mapheight = 80

    #define tileset
    #tileset = tcod.tileset.load_tilesheet(
    #    "terminal.png", 16, 16, tcod.tileset.CHARMAP_TCOD
    #)

    event_handler = EventHandler()

    player = Entity(35, 35, "@", (0, 255, 213))
    creature = Entity(35, 15, "S", (255, 0, 0))
    entities = {creature, player}
    gamemap = Map(mapwidth, mapheight)

    engine = Engine(entities = entities, event_handler = event_handler, gamemap = gamemap, player = player)

    #init terminal window
    with tcod.context.new_terminal(
        150,
        120,
        #tileset = tileset,
        title = "Hartbrook",
        vsync = True
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order = "F")
        while True: 

            engine.render(console = root_console, context = context)
            
            events = tcod.event.wait()

            engine.handle_events(events)

if __name__ == "__main__":
    main()
