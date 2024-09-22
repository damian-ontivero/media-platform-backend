from dataclasses import dataclass

from contexts.shared.domain.query_bus.query import Query


@dataclass(frozen=True)
class MediaSearchByCriteriaQuery(Query):
    filter: dict
    sort: list[dict]
    page_size: int
    page_number: int
