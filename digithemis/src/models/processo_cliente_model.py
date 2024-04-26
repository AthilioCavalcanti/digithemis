from sqlalchemy import Index, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class ProcessoCliente(Base):
    __tablename__ = 'processos_clientes'

    id_processo: Mapped[int] = mapped_column(
        ForeignKey('processos.id_processo'), primary_key=True
    )
    id_cliente: Mapped[int] = mapped_column(
        ForeignKey('clientes.id_cliente'), primary_key=True
    )

    processo = relationship('Processo')
    cliente = relationship('Cliente')

    indice_cliente = Index('idx_cliente_processo', id_cliente)
    indice_processo = Index('idx_processo_cliente', id_processo)
