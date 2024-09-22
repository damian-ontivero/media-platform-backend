import os

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker


class PostgresSession:
    """
    PostgresSession class to create a session with the database.
    """

    @staticmethod
    def create_session(
        username: str = os.getenv("POSTGRES_USER", ""),
        password: str = os.getenv("POSTGRES_PASS", ""),
        host: str = os.getenv("POSTGRES_HOST", ""),
        port: str = os.getenv("POSTGRES_PORT", ""),
        database: str = os.getenv("POSTGRES_DATABASE", ""),
        autocommit: bool = False,
        verbose: bool = False,
    ):
        engine = create_engine(f"postgresql://{username}:{password}@{host}:{port}/{database}", echo=verbose)

        return sessionmaker(bind=engine, autocommit=autocommit)


class Base(DeclarativeBase):
    """
    Base class for all ORM classes to inherit from.
    """

    pass
