import factory

from contexts.catalog.series.domain.serie import Serie
from tests.contexts.catalog.series.factory.serie_season_factory import SerieSeasonFactory
from tests.contexts.shared.factory.entity_id_factory import EntityIdFactory


class SerieFactory(factory.Factory):
    class Meta:
        model = Serie

    id = factory.SubFactory(EntityIdFactory)
    title = factory.Faker("name")
    seasons = factory.List([factory.SubFactory(SerieSeasonFactory) for _ in range(3)])
