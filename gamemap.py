from tcod.console import Console
import numpy as np
import json

import tiletypes

class Map:

    def __init__(self, width:int, height:int):
        self.width = width
        self.height = height
        self.tiles = np.full((width, height), fill_value=tiletypes.floor, order = "F")

    def within_border(self, x:int, y:int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console: Console) -> None:
        console.tiles_rgb[0:self.width, 0:self.height] = self.tiles["obscured"]

    def load_map(self, mappath):
        with open(mappath) as mapfile:
            map_obj = json.load(mapfile)
        for x in range(0, map_obj["width"]):
            for y in range(0, map_obj["height"]):
                if map_obj["mapgrid"][y][x] == map_obj["tile_id"]["grass"]:
                    self.tiles[x, y] = tiletypes.grass
                elif map_obj["mapgrid"][y][x] == map_obj["tile_id"]["wall"]:
                    self.tiles[x, y] = tiletypes.wall
