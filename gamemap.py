from tcod.console import Console
import numpy as np

import tiletypes

class Map:
    def __init__(self, width:int, height:int):
        self.width = width
        self.height = height
        self.tiles = np.full((width, height), fill_value=tiletypes.floor, order = "F")
        self.tiles[30:40, 10] = tiletypes.wall
        self.tiles[30:40, 20] = tiletypes.wall
        self.tiles[40, 10:21] = tiletypes.wall
        self.tiles[30, 10:15] = tiletypes.wall
        self.tiles[30, 16:20] = tiletypes.wall

    def within_border(self, x:int, y:int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console: Console) -> None:
        console.tiles_rgb[0:self.width, 0:self.height] = self.tiles["obscured"]