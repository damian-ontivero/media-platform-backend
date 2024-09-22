from fastapi import status

from contexts.backoffice.media.domain.media_exceptions import MediaAlreadyExists
from contexts.backoffice.media.domain.media_exceptions import MediaDoesNotExist
from contexts.backoffice.movies.domain.movie_exceptions import MovieAlreadyExists
from contexts.backoffice.movies.domain.movie_exceptions import MovieDoesNotExist
from contexts.backoffice.series.domain.serie_exceptions import SerieAlreadyExists
from contexts.backoffice.series.domain.serie_exceptions import SerieDoesNotExist


EXCEPTION_TO_HTTP_STATUS_CODE = {
    Exception: status.HTTP_500_INTERNAL_SERVER_ERROR,
    PermissionError: status.HTTP_403_FORBIDDEN,
    MediaDoesNotExist: status.HTTP_404_NOT_FOUND,
    MediaAlreadyExists: status.HTTP_422_UNPROCESSABLE_ENTITY,
    MovieDoesNotExist: status.HTTP_404_NOT_FOUND,
    MovieAlreadyExists: status.HTTP_422_UNPROCESSABLE_ENTITY,
    SerieDoesNotExist: status.HTTP_404_NOT_FOUND,
    SerieAlreadyExists: status.HTTP_422_UNPROCESSABLE_ENTITY,
    ValueError: status.HTTP_400_BAD_REQUEST,
    TypeError: status.HTTP_400_BAD_REQUEST,
}
