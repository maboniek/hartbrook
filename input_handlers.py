import tcod.event

from typing import Optional

from actions import Action, EscapeAction, MovementAction

class EventHandler(tcod.event.EventDispatch[Action]):
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    def ev_keydown(self, event:tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None

        key = event.sym

        if key == tcod.event.K_UP:
            action = MovementAction(_xmove = 0, _ymove = -1)
        elif key == tcod.event.K_DOWN:
            action = MovementAction(_xmove = 0, _ymove = 1)
        elif key == tcod.event.K_LEFT:
            action = MovementAction(_xmove = -1, _ymove = 0)
        elif key == tcod.event.K_RIGHT:
            action = MovementAction(_xmove = 1, _ymove = 0)
        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction()

        return action