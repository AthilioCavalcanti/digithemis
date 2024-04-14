from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

class Advogado_Especialidade(Base):
    __tablename__ = 'advogados_especialidades'

    id_advogado: Mapped[int] = mapped_column(ForeignKey('advogados.id_advogado'), primary_key=True)    
    id_especialidade: Mapped[int] = mapped_column(ForeignKey('especialidades.id_especialidade'), primary_key=True)

    advogado = relationship('Advogado')
    especialidade = relationship('Especialidade')