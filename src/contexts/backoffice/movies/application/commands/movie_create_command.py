from dataclasses import dataclass

from contexts.shared.domain.command_bus.command import Command


@dataclass(frozen=True)
class MovieCreateCommand(Command):
    title: str
    synopsis: str
    media_id: str
