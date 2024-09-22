import factory

from contexts.backoffice.series.domain.serie_episode import SerieEpisode
from tests.contexts.shared.factory.entity_id_factory import EntityIdFactory


class SerieEpisodeFactory(factory.Factory):
    class Meta:
        model = SerieEpisode

    id = factory.SubFactory(EntityIdFactory)
    number = factory.Faker("random_int")
    title = factory.Faker("name")
    synopsis = factory.Faker("text")
    media_id = factory.SubFactory(EntityIdFactory)
