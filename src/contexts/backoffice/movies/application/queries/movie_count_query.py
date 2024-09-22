from dataclasses import dataclass

from contexts.shared.domain.query_bus.query import Query


@dataclass(frozen=True)
class MovieCountQuery(Query):
    pass
