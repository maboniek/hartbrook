import tcod
from actions import EscapeAction, MovementAction
from input_handlers import EventHandler
import entity
from typing import Tuple



def main() -> None:
    screen_width = 100
    screen_height = 80

    player = entity.Entity(int(5), int(5), "@", (0, 255, 213))

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
        while True:
            #print player character
            root_console.print(x = player.x, y = player.y, string=player.character, fg=player.color)

            #refresh console contents
            context.present(root_console)
            
            #clear console contents
            root_console.clear()

            #wait for event (input)
            for event in tcod.event.wait():
                
                #store event in variable
                action = event_handler.dispatch(event)

                if action is None:
                    continue

                if isinstance(action, MovementAction):
                    player.move(dx = action.dx, dy = action.dy)
                elif isinstance(action, EscapeAction):
                    raise SystemExit()

if __name__ == "__main__":
    main()
