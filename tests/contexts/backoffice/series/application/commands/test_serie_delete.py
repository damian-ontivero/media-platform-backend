import faker
import pytest

from contexts.backoffice.series.application.commands.serie_delete_command import SerieDeleteCommand
from contexts.backoffice.series.application.commands.serie_delete_command_handler import SerieDeleteCommandHandler
from contexts.backoffice.series.application.services.serie_deleter import SerieDeleter
from tests.contexts.backoffice.series.factory.serie_factory import SerieFactory


async def test_serie_delete__ok(mock_serie_repository, mock_event_bus) -> None:
    serie = SerieFactory()
    mock_serie_repository.search.return_value = serie
    deleter = SerieDeleter(mock_serie_repository, mock_event_bus)
    command = SerieDeleteCommand(serie.id.value)
    handler = SerieDeleteCommandHandler(deleter)

    await handler.handle(command)

    mock_serie_repository.delete.assert_called_once_with(serie.id.value)
    mock_event_bus.publish.assert_called_once()


async def test_serie_delete__not_found(mock_serie_repository, mock_event_bus) -> None:
    mock_serie_repository.search.return_value = None
    deleter = SerieDeleter(mock_serie_repository, mock_event_bus)
    command = SerieDeleteCommand(faker.Faker().uuid4())
    handler = SerieDeleteCommandHandler(deleter)

    with pytest.raises(Exception):
        await handler.handle(command)
