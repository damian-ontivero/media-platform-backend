from dataclasses import dataclass

from contexts.shared.domain.command_bus.command import Command


@dataclass(frozen=True)
class MovieUpdateCommand(Command):
    id: str
    title: str
    synopsis: str
    media_id: str
