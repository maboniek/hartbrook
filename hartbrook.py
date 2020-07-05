import tcod
import entity



def main() -> None:
    screen_width = 100
    screen_height = 80

    #define tileset
    tileset = tcod.tileset.load_tilesheet(
        "terminal.png", 16, 16, tcod.tileset.CHARMAP_TCOD
    )

    #init terminal window
    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset = tileset,
        title = "Hartbrook",
        vsync = True
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order = "F")

if __name__ == "__main__":
    main()
