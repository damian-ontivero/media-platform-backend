from dataclasses import dataclass

from contexts.shared.domain.command_bus.command import Command


@dataclass(frozen=True)
class MediaUpdateCommand(Command):
    id: str
    title: str
    file_name: str
    file: bytes
