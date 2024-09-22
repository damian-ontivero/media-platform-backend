from fastapi import status

from contexts.catalog.movies.domain.movie_exceptions import MovieDoesNotExist
from contexts.catalog.series.domain.serie_exceptions import SerieDoesNotExist


EXCEPTION_TO_HTTP_STATUS_CODE = {
    Exception: status.HTTP_500_INTERNAL_SERVER_ERROR,
    PermissionError: status.HTTP_403_FORBIDDEN,
    MovieDoesNotExist: status.HTTP_404_NOT_FOUND,
    SerieDoesNotExist: status.HTTP_404_NOT_FOUND,
    ValueError: status.HTTP_400_BAD_REQUEST,
    TypeError: status.HTTP_400_BAD_REQUEST,
}
