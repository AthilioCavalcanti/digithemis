from sqlalchemy import String, Index, LargeBinary, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

class Documento(Base):
    __tablename__ = 'documentos'

    id_documento: Mapped[int] = mapped_column(primary_key=True)
    id_cliente: Mapped[int] = mapped_column(ForeignKey('clientes.id_cliente'))
    titulo: Mapped[str] = mapped_column(String(100), nullable=True)
    categoria: Mapped[str] = mapped_column(String(20))
    arquivo: Mapped[LargeBinary] = mapped_column(type_=LargeBinary)

    cliente = relationship('Cliente')

    indice_titulo = Index('idx_titulo', titulo)
    indice_categoria = Index('idx_categoria', categoria)
    indice_cliente = Index('idx_id_cliente', id_cliente)

    def __repr__(self):
        return f'ID: {self.id_documento}; Cliente: {self.cliente.nome}'