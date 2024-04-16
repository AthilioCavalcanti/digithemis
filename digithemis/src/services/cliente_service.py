from config import ConexaoDB
from errors import RegistroExistenteError, RegistroNaoExistenteError
from models import Cliente


class ClienteService:
    def __init__(self) -> None:
        self.conexao = ConexaoDB()

    def cadastra_cliente(self, nome, cpf_cnpj, email, telefone):
        empresa = True if len(cpf_cnpj) > 11 else False
        with self.conexao as con:
            try:
                cliente_existe = self.busca_cliente(cpf_cnpj) is not None
                if cliente_existe:
                    raise RegistroExistenteError('Cliente já está cadastrado')
                else:
                    cliente = Cliente(
                        nome=nome,
                        cpf_cnpj=cpf_cnpj,
                        email=email,
                        telefone=telefone,
                        empresa=empresa,
                    )
                    con.session.add(cliente)
                    con.session.commit()
            except Exception as erro:
                con.session.rollback()
                raise erro

    def busca_cliente(self, cpf_cnpj):
        with self.conexao as con:
            cliente = (
                con.session.query(Cliente).filter_by(cpf_cnpj=cpf_cnpj).first()
            )
            return cliente

    def lista_clientes(self):
        with self.conexao as con:
            clientes = (
                con.session.query(Cliente).filter(Cliente.ativo == True).all()
            )
            return clientes

    def atualiza_cliente(self, cpf_cnpj, campo, valor):
        with self.conexao as con:
            try:
                cliente = self.busca_cliente(cpf_cnpj)
                campos = ['nome', 'email', 'telefone']
                if cliente:
                    if campo in campos:
                        con.session.query(Cliente).filter(
                            Cliente.cpf_cnpj == cpf_cnpj
                        ).update({campo: valor})
                    else:
                        raise ValueError('Campo inválido')
                    con.session.commit()
                else:
                    raise RegistroNaoExistenteError(
                        'Cliente não foi encontrado'
                    )
            except Exception as erro:
                con.session.rollback()
                raise erro

    def remove_cliente(self, cpf_cnpj):
        with self.conexao as con:
            try:
                cliente = self.busca_cliente(cpf_cnpj)
                if cliente and cliente.ativo:
                    con.session.query(Cliente).filter(
                        Cliente.cpf_cnpj == cpf_cnpj
                    ).update({'ativo': False})
                    con.session.commit()
                else:
                    raise RegistroNaoExistenteError(
                        'Cliente não foi encontrado'
                    )
            except Exception as erro:
                con.session.rollback()
                raise erro
