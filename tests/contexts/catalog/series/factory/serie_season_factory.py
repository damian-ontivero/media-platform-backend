import factory

from contexts.catalog.series.domain.serie_season import SerieSeason
from tests.contexts.catalog.series.factory.serie_episode_factory import SerieEpisodeFactory
from tests.contexts.shared.factory.entity_id_factory import EntityIdFactory


class SerieSeasonFactory(factory.Factory):
    class Meta:
        model = SerieSeason

    id = factory.SubFactory(EntityIdFactory)
    number = factory.Faker("random_int")
    episodes = factory.List([factory.SubFactory(SerieEpisodeFactory) for _ in range(3)])
