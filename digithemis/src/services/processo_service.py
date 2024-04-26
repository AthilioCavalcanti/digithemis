from config import ConexaoDB
from errors import RegistroExistenteError, RegistroNaoExistenteError
from models import Processo, ProcessoCliente, Cliente, Especialidade


class ProcessoService:
    def __init__(self) -> None:
        self.conexao = ConexaoDB()

    def cadastra_processo(
        self,
        num_processo,
        comarca,
        vara,
        id_especialidade,
        data_distribuicao,
        gratuidade_justica=False,
    ):
        with self.conexao as con:
            try:
                processo_existe = self.busca_processo(num_processo) is not None
                if processo_existe:
                    raise RegistroExistenteError('Processo já está cadastrado')
                else:
                    processo = Processo(
                        num_processo=num_processo,
                        comarca=comarca,
                        vara=vara,
                        gratuidade_justica=gratuidade_justica,
                        id_especialidade=id_especialidade,
                        data_distribuicao=data_distribuicao,
                    )
                    con.session.add(processo)
                    con.session.commit()
            except Exception as erro:
                con.session.rollback()
                raise erro

    def lista_processos(self, ativo=True):
        with self.conexao as con:
            processos = (
                con.session.query(Processo)
                .filter(Processo.ativo == ativo)
                .all()
            )
            return processos

    def busca_processo(self, num_processo):
        with self.conexao as con:
            processo = (
                con.session.query(Processo)
                .filter_by(num_processo=num_processo)
                .first()
            )
            return processo

    def atualiza_processo(self, num_processo, campo, valor):
        with self.conexao as con:
            try:
                processo = self.busca_processo(num_processo)
                campos = ['comarca', 'vara', 'gratuidade_justica']
                if processo:
                    if campo in campos:
                        con.session.query(Processo).filter(
                            Processo.num_processo == num_processo
                        ).update({campo: valor})
                    else:
                        raise ValueError('Campo inválido')
                    con.session.commit()
                else:
                    raise RegistroNaoExistenteError(
                        'Processo não foi encontrado'
                    )
            except Exception as erro:
                con.session.rollback()
                raise erro

    def remove_processo(self, num_processo):
        with self.conexao as con:
            try:
                processo = self.busca_processo(num_processo)
                if processo and processo.ativo:
                    con.session.query(Processo).filter(
                        Processo.num_processo == num_processo
                    ).update({'ativo': False})
                    con.session.commit()
                else:
                    raise RegistroNaoExistenteError(
                        'Processo não foi encontrado'
                    )
            except Exception as erro:
                con.session.rollback()
                raise erro

    def busca_processo_por_cliente(self, nome_cliente):
        with self.conexao as con:
            try:
                cliente = (
                    con.session.query(Cliente)
                    .filter(Cliente.nome == nome_cliente)
                    .first()
                )

                lista_processo_cliente = (
                    con.session.query(ProcessoCliente)
                    .filter(ProcessoCliente.id_cliente == cliente.id_cliente)
                    .all()
                )

                processos = []

                for obj_processo in lista_processo_cliente:
                    processo = (
                        con.session.query(Processo)
                        .filter(
                            Processo.id_processo == obj_processo.id_processo
                        )
                        .first()
                    )
                    processos.append(processo)

                return processos
            except Exception as erro:
                return ['Deu ruim']
            

    def adiciona_processo_cliente(self, cpf_cliente, num_processo):
        with self.conexao as con:
            try:
                cliente = (
                    con.session.query(Cliente)
                    .filter_by(cpf_cnpj=cpf_cliente)
                    .first()
                )
                processo = (
                    con.session.query(Processo)
                    .filter_by(num_processo=num_processo)
                    .first()
                )

                if not cliente:
                    raise RegistroNaoExistenteError('Cliente não encontrado')

                if not processo:
                    raise RegistroNaoExistenteError('Processo não encontrado')

                processo_cliente = ProcessoCliente(
                    id_cliente=cliente.id_cliente,
                    id_processo=processo.id_processo
                )
                con.session.add(processo_cliente)
                con.session.commit()
            except RegistroNaoExistenteError as erro:
                raise erro
                
            except Exception as erro:
                con.session.rollback()
                raise erro
            
    def lista_processos_por_especialidade(self, nome_especialidade):
        with self.conexao as con:
            try:
                especialidade = (
                    con.session.query(Especialidade)
                    .filter_by(tipo=nome_especialidade)
                    .first()
                )

                if not especialidade:
                    return []

                processos = (
                    con.session.query(Processo)
                    .filter_by(id_especialidade=especialidade.id_especialidade, ativo=True)
                    .all()
                )

                return processos
            except Exception as erro:
                raise erro
