class Action:
    pass

class EscapeAction(Action):
    pass

class MovementAction(Action):
    def __init__(self, _xmove:int, _ymove:int):
        super().__init__()
        self.xmove = _xmove
        self.ymove = _ymove