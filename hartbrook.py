import tcod

from entity import Entity

from typing import Tuple

from actions import EscapeAction, MovementAction
from input_handlers import EventHandler


def main() -> None:
    screen_width = 100
    screen_height = 80

    player = Entity(1, 1, "@", (0, 255, 213))

    #define tileset
    tileset = tcod.tileset.load_tilesheet(
        "terminal.png", 16, 16, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    #init terminal window
    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset = tileset,
        title = "Hartbrook",
        vsync = True
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order = "F")
        
        for event in tcod.event.wait():

            action = event_handler.dispatch(event)

            if action is None:
                continue
            
            if isinstance(action, MovementAction):
                player.move(xmove=action.xmove, ymove=action.xmove)
            
            elif isinstance(action, EscapeAction):
                raise SystemExit()

if __name__ == "__main__":
    main()
