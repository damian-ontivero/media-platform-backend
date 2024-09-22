import factory

from contexts.catalog.movies.domain.movie import Movie
from tests.contexts.shared.factory.entity_id_factory import EntityIdFactory


class MovieFactory(factory.Factory):
    class Meta:
        model = Movie

    id = factory.SubFactory(EntityIdFactory)
    title = factory.Faker("name")
    duration = factory.Faker("random_int", min=1, max=300)
