import factory

from contexts.backoffice.series.domain.serie import Serie
from tests.contexts.backoffice.series.factory.serie_season_factory import SerieSeasonFactory
from tests.contexts.shared.factory.entity_id_factory import EntityIdFactory


class SerieFactory(factory.Factory):
    class Meta:
        model = Serie

    id = factory.SubFactory(EntityIdFactory)
    title = factory.Faker("name")
    synopsis = factory.Faker("text")
    seasons = factory.List([factory.SubFactory(SerieSeasonFactory) for _ in range(3)])
