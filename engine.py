from typing import Set, Iterable, Any, Optional
from tcod.context import Context
from tcod.console import Console
from actions import EscapeAction, MovementAction
from entity import Entity
from gamemap import Map
from input_handlers import EventHandler

class Engine:

    def __init__(self, entities: Set[Entity], event_handler: EventHandler, gamemap: Map, player: Entity):
        self.entities = entities
        self.event_handler = event_handler
        self.player = player
        self.gamemap = gamemap
        gamemap.load_map("maps/hub.json")

    def handle_events(self, events: Iterable[Any]) -> None:
        for event in events:
            action = self.event_handler.dispatch(event)

            if action is None:
                continue

            if isinstance(action, MovementAction):
                if self.gamemap.tiles["can_walk"][self.player.x + action.dx, self.player.y + action.dy]:
                    self.player.move(dx=action.dx, dy=action.dy)
            elif isinstance(action, EscapeAction):
                raise SystemExit()

    def render(self, console: Console, context: Context) -> None:
        self.gamemap.render(console)
        for entity in self.entities:
            console.print(entity.x, entity.y, entity.character, fg = entity.color)
        context.present(console)
        console.clear()

