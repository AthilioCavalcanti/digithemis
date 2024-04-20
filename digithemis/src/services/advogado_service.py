from config import ConexaoDB
from errors import RegistroExistenteError, RegistroNaoExistenteError
from models import Advogado, Especialidade, AdvogadoEspecialidade
from utils import Seguranca


class AdvogadoService:
    def __init__(self) -> None:
        self.conexao = ConexaoDB()

    def cadastra_advogado(self, nome, cpf, oab, senha, email, celular):
        with self.conexao as con:
            try:
                advogado_exite = self.busca_advogado(cpf) is not None
                if advogado_exite:
                    raise RegistroExistenteError('Advogado já está cadastrado')
                else:
                    advogado = Advogado(
                        nome=nome,
                        cpf=cpf,
                        oab=oab,
                        senha=Seguranca.criptografa_senha(senha),
                        email=email,
                        celular=celular,
                    )
                    con.session.add(advogado)
                    con.session.commit()
            except Exception as erro:
                con.session.rollback()
                raise erro

    def busca_advogado(self, cpf):
        with self.conexao as con:
            advogado = con.session.query(Advogado).filter_by(cpf=cpf).first()
            return advogado

    def lista_advogados(self):
        with self.conexao as con:
            advogados = con.session.query(Advogado).all()
            return advogados

    def atualiza_advogado(self, cpf, campo, valor):
        with self.conexao as con:
            try:
                advogado = self.busca_advogado(cpf)
                campos = ['nome', 'oab', 'email', 'celular', 'senha']
                if advogado:
                    if campo in campos:
                        if campo == 'senha':
                            valor = Seguranca.criptografa_senha(valor)

                        con.session.query(Advogado).filter(
                            Advogado.cpf == cpf
                        ).update({campo: valor})
                    else:
                        raise ValueError('Campo inválido')
                    con.session.commit()
                else:
                    raise RegistroNaoExistenteError(
                        'Advogado não foi encontrado'
                    )
            except Exception as erro:
                con.session.rollback()
                raise erro

    def remove_advogado(self, cpf):
        with self.conexao as con:
            try:
                advogado = self.busca_advogado(cpf)
                if advogado:
                    con.session.delete(advogado)
                    con.session.commit()
                else:
                    raise RegistroNaoExistenteError(
                        'Advogado não foi encontrado'
                    )
            except Exception as erro:
                con.session.rollback()
                raise erro

    def valida_senha(self, cpf, senha):
        with self.conexao as con:
            try:
                advogado = (
                    con.session.query(Advogado).filter_by(cpf=cpf).first()
                )
                if advogado:
                    if Seguranca.verifica_senha(senha, advogado.senha):
                        return True
                return False
            except Exception as e:
                raise e

    def adiciona_especialidade_por_cpf(self, cpf_advogado, nome_especialidade):
        with self.conexao as con:
            try:
                advogado = self.busca_advogado(cpf_advogado)
                if not advogado:
                    raise RegistroNaoExistenteError('Advogado não encontrado')

                especialidade = (
                    con.session.query(Especialidade)
                    .filter_by(tipo=nome_especialidade)
                    .first()
                )

                adv_especialidade = AdvogadoEspecialidade(
                    id_advogado=advogado.id_advogado,
                    id_especialidade=especialidade.id_especialidade,
                )

                con.session.add(adv_especialidade)
                con.session.commit()
            except Exception as erro:
                con.session.rollback()
                raise erro
            
    def especialidade_do_advogado(self, cpf_advogado):
        with self.conexao as con:
            try:
                advogado = (
                    con.session.query(Advogado)
                    .filter_by(cpf=cpf_advogado)
                    .first()
                )

                if not advogado:
                    return None

                especialidade = (
                    con.session.query(Especialidade)
                    .join(AdvogadoEspecialidade)
                    .filter(AdvogadoEspecialidade.id_advogado == advogado.id_advogado)
                    .first()
                )

                return especialidade.tipo if especialidade else None

            except Exception as erro:
                raise erro
