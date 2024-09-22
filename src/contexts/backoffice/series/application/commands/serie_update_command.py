from dataclasses import dataclass

from contexts.shared.domain.command_bus.command import Command


@dataclass(frozen=True)
class SerieUpdateCommand(Command):
    id: str
    title: str
    synopsis: str
    seasons: list[dict]
