import faker
import pytest

from contexts.backoffice.movies.application.commands.movie_update_command import MovieUpdateCommand
from contexts.backoffice.movies.application.commands.movie_update_command_handler import MovieUpdateCommandHandler
from contexts.backoffice.movies.application.services.movie_updater import MovieUpdater
from contexts.backoffice.movies.domain.movie_exceptions import MovieDoesNotExist
from tests.contexts.backoffice.media.factory.media_factory import MediaFactory
from tests.contexts.backoffice.movies.factory.movie_factory import MovieFactory


async def test_movie_update__ok(mock_movie_repository, mock_query_bus, mock_event_bus) -> None:
    movie = MovieFactory()
    media = MediaFactory()
    mock_movie_repository.search.return_value = movie
    mock_movie_repository.matching.return_value = None
    mock_query_bus.ask.return_value = media
    updater = MovieUpdater(mock_movie_repository, mock_query_bus, mock_event_bus)
    command = MovieUpdateCommand(
        id=movie.id.value, title=faker.Faker().name(), synopsis=faker.Faker().text(), media_id=media.id.value
    )
    handler = MovieUpdateCommandHandler(updater)

    await handler.handle(command)

    mock_movie_repository.save.assert_called_once_with(movie)
    mock_event_bus.publish.assert_called_once()


async def test_movie_update__not_found(mock_movie_repository, mock_query_bus, mock_event_bus) -> None:
    media = MediaFactory()
    mock_movie_repository.search.return_value = None
    mock_query_bus.ask.return_value = media
    updater = MovieUpdater(mock_movie_repository, mock_query_bus, mock_event_bus)
    command = MovieUpdateCommand(
        id=faker.Faker().uuid4(), title=faker.Faker().name(), synopsis=faker.Faker().text(), media_id=media.id.value
    )
    handler = MovieUpdateCommandHandler(updater)

    with pytest.raises(MovieDoesNotExist):
        await handler.handle(command)
