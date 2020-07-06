
import tcod

from entity import Entity

from typing import Tuple

from engine import Engine
from input_handlers import EventHandler


def main() -> None:
    screen_width = 100
    screen_height = 80

    #define tileset
    tileset = tcod.tileset.load_tilesheet(
        "terminal.png", 16, 16, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    player = Entity(1, 1, "@", (0, 255, 213))
    creature = Entity(5, 5, "W", (255, 0, 0))
    entities = {player, creature}

    engine = Engine(entities = entities, event_handler = event_handler, player = player)

    #init terminal window
    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset = tileset,
        title = "Hartbrook",
        vsync = True
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order = "F")
        while True: 

            engine.render(console = root_console)
            
            events = tcod.event.Wait()

            engine.handle_events(events)


if __name__ == "__main__":
    main()
