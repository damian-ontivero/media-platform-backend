import faker

from contexts.catalog.media.application.services.media_creator import MediaCreator


async def test_media_create__ok(mock_media_repository, mock_event_bus) -> None:
    mock_media_repository.matching.return_value = None
    creator = MediaCreator(mock_media_repository, mock_event_bus)

    await creator.run(
        id=faker.Faker().uuid4(),
        title=faker.Faker().name(),
        size=1000,
        duration=100,
        path="backend/tests/data/video.mp4",
    )

    mock_media_repository.save.assert_called_once()
    mock_event_bus.publish.assert_called_once()
