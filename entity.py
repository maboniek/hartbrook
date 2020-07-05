import tcod

class Entity:

    x: int
    y: int
    character = ""
    color: tcod.color

    def __init__(self, _x:int, _y:int, _character:str, _color: tcod.color):
        self.x = _x
        self.y = _y
        self.character = _character
        self.color = _color
    
    def move(self, xmove:int, ymove:int):
        self.x += xmove
        self.y += ymove