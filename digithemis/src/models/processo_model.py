from sqlalchemy import String, Index, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

class Processo(Base):
    __tablename__ = 'processos'

    id_processo: Mapped[int] = mapped_column(primary_key=True)
    num_processo: Mapped[str] = mapped_column(String(30))
    comarca: Mapped[str] = mapped_column(String(50), nullable=True)
    vara: Mapped[str] = mapped_column(String(20), nullable=True)
    gratuidade_justica: Mapped[bool] = mapped_column(default=False)
    id_especialidade: Mapped[int] = mapped_column(ForeignKey('especialidades.id_especialidade'))
    data_distribuicao: Mapped[Date] = mapped_column(Date)
    ativo: Mapped[bool] = mapped_column(default=True)

    especialidade = relationship('Especialidade')

    indice_comarca = Index('idx_comarca', comarca)

    def __repr__(self):
        return f'Número do Processo: {self.num_processo}; Comarca: {self.comarca}; Vara: {self.vara}'