from sqlalchemy import String, Index
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base

class Advogado(Base):
    __tablename__ = 'advogados'

    id_advogado: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(50))
    cpf: Mapped[str] = mapped_column(String(11), unique=True)
    oab: Mapped[str] = mapped_column(String(10), unique=True)
    senha: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(255), unique=True)
    celular: Mapped[str] = mapped_column(String(20), nullable=True)
    admin: Mapped[bool] = mapped_column(default=False)

    indice_nome = Index('idx_nome', nome)
    indice_oab = Index('idx_oab', oab)

    def __repr__(self):
        return f'Advogado: {self.nome}; OAB: {self.oab}; E-mail: {self.email}; Celular: {self.celular}'