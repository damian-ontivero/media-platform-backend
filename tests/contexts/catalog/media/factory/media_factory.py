import factory

from contexts.catalog.media.domain.media import Media
from tests.contexts.shared.factory.entity_id_factory import EntityIdFactory


class MediaFactory(factory.Factory):
    class Meta:
        model = Media

    id = factory.SubFactory(EntityIdFactory)
    title = factory.Faker("name")
    size = factory.Faker("random_int", min=1, max=1000)
    duration = factory.Faker("random_int", min=1, max=1000)
    path = factory.Faker("file_path")
