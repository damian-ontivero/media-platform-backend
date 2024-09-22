from contexts.shared.domain.domain_exception import DomainException


class MediaDomainException(DomainException):
    pass


class MediaDoesNotExist(MediaDomainException):
    def __init__(self, media_id: str):
        super().__init__(f"Media with id {media_id} does not exist")


class MediaAlreadyExists(MediaDomainException):
    def __init__(self, title: str):
        super().__init__(f"Media with title {title} already exists")
