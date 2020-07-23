from typing import Tuple

import numpy as np

graphic_dtype = np.dtype([("character", np.int32), ("fg", "3B"), ("bg", "3B")])

tile_dtype = np.dtype([("can_walk", np.bool), ("transparent", np.bool), ("obscured", graphic_dtype)])

def gen_tile(*, can_walk:int, transparent:int, obscured:Tuple[int, Tuple[int, int, int], Tuple[int, int, int]]) -> np.ndarray:
    return np.array((can_walk, transparent, obscured), dtype=tile_dtype)


grass = gen_tile(can_walk=True, transparent=True, obscured=(ord("\""), (130, 180, 0),(0, 0, 0)))
floor = gen_tile(can_walk=True, transparent=True, obscured=(ord("="), (86, 57, 0),(0, 0, 0)))
wall = gen_tile(can_walk=False, transparent=False, obscured=(ord("#"), (120, 120, 120),(0, 0, 0)))