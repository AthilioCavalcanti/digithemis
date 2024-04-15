from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class Especialidade(Base):
    __tablename__ = 'especialidades'

    id_especialidade: Mapped[int] = mapped_column(primary_key=True)
    tipo: Mapped[str] = mapped_column(String(50))

    def __repr__(self):
        return f'Especialidade: {self.tipo}'
