import uuid

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import MetaData
from sqlalchemy.dialects.postgresql import UUID


naming_convention: dict[str, str] = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_N_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}


class Base(DeclarativeBase):
    """Base class for all models."""
    __abstract__ = True

    metadata = MetaData(naming_convention=naming_convention,)


class IdIntPkMixin:
    """Mixin for SQLAlchemy models with `pk` and `id` columns"""

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)


