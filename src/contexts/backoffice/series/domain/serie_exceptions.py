from contexts.shared.domain.domain_exception import DomainException


class SerieDomainException(DomainException):
    pass


class SerieDoesNotExist(SerieDomainException):
    def __init__(self, serie_id: str) -> None:
        super().__init__(f"Serie with id {serie_id!r} does not exist.")


class SerieAlreadyExists(SerieDomainException):
    def __init__(self, title: str) -> None:
        super().__init__(f"Serie with title {title!r} already exists.")
