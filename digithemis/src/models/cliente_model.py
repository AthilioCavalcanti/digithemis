from sqlalchemy import String, Index
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base

class Cliente(Base):
    __tablename__ = 'clientes'

    id_cliente: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(50))
    cpf_cnpj: Mapped[str] = mapped_column(String(14), unique=True)
    email: Mapped[str] = mapped_column(String(255))
    telefone: Mapped[str] = mapped_column(String(20), nullable=True)
    empresa: Mapped[bool] = mapped_column(default=False)
    ativo: Mapped[bool] = mapped_column(default=True)

    indice_nome = Index('idx_nome_cliente', nome)
    indice_cpf_cnpj = Index('idx_cpf_cnpj', cpf_cnpj)

    def __repr__(self):
        return f'Cliente: {self.nome}; CPF: {self.cpf_cnpj}; E-mail: {self.email}; Celular: {self.telefone}'