from pathlib import Path

from alembic.config import Config
from alembic.script import ScriptDirectory
from sqlalchemy import inspect, text
from sqlalchemy.exc import SQLAlchemyError

from app.db.session import engine


class DatabaseMigrationError(RuntimeError):
    """Raised when database schema is not at the latest migration."""



def ensure_database_migrated() -> None:
    """Validate that the DB has Alembic migrations applied up to head."""
    alembic_config = Config(str(Path(__file__).resolve().parents[2] / "alembic.ini"))
    script_directory = ScriptDirectory.from_config(alembic_config)
    expected_heads = set(script_directory.get_heads())

    try:
        with engine.connect() as connection:
            inspector = inspect(connection)
            if "alembic_version" not in inspector.get_table_names():
                raise DatabaseMigrationError(
                    "Base de datos sin migraciones aplicadas. Ejecuta: 'cd backend && alembic upgrade head'."
                )

            current_versions = {
                row[0]
                for row in connection.execute(text("SELECT version_num FROM alembic_version"))
            }
    except SQLAlchemyError as exc:
        raise DatabaseMigrationError(
            "No se pudo validar el estado de migraciones de la base de datos. "
            "Verifica DATABASE_URL y ejecuta 'alembic upgrade head'."
        ) from exc

    if current_versions != expected_heads:
        raise DatabaseMigrationError(
            "Migraciones pendientes detectadas. Ejecuta: 'cd backend && alembic upgrade head'."
        )
