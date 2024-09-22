from contexts.shared.domain.domain_exception import DomainException


class MovieDomainException(DomainException):
    pass


class MovieDoesNotExist(MovieDomainException):
    def __init__(self, movie_id: str) -> None:
        super().__init__(f"Movie with id {movie_id!r} does not exist.")


class MovieAlreadyExists(MovieDomainException):
    def __init__(self, title: str) -> None:
        super().__init__(f"Movie with title {title!r} already exists.")
