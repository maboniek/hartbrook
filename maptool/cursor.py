import tcod

class Cursor:

    x: int
    y: int
    character = ""
    color: tcod.color

    def __init__(self, _x:int, _y:int, _character:str, _color: tcod.color):
        self.x = _x
        self.y = _y
        self.character = _character
        self.color = _color
    
    def move(self, dx:int, dy:int):
        self.x += dx
        self.y += dy
    
    def placeTile(self, tx:int, ty:int, console:tcod.console):
        

