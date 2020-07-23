from typing import Set, Iterable, Any, Optional
from tcod.context import Context
from tcod.console import Console
from actions import EscapeAction, MovementAction
from cursor import Cursor
from input_handlers import EventHandler

class Engine:

    def __init__(self, event_handler: EventHandler, cursor: Cursor):
        self.event_handler = event_handler
        self.cursor = cursor

    def handle_events(self, events: Iterable[Any]) -> None:
        for event in events:
            action = self.event_handler.dispatch(event)

            if action is None:
                continue

            if isinstance(action, MovementAction):
                self.cursor.move(dx=action.dx, dy=action.dy)
            elif isinstance(action, EscapeAction):
                raise SystemExit()

    def render(self, console: Console, context: Context) -> None:
        
        console.print(self.cursor.x, self.cursor.y, self.cursor.character, fg = self.cursor.color)
        context.present(console)
        console.clear()

