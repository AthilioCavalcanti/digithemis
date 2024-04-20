from services import AdvogadoService, ProcessoService
from utils import ValidacaoEntradas


class AdvogadoController:
    def __init__(self):
        self.adv_service = AdvogadoService()
        self.processo_service = ProcessoService()

    def adicionar_advogado(
        self, nome, cpf, oab, email, celular, senha, especialidade
    ):
        try:
            if (
                ValidacaoEntradas.valida_cpf_cnpj(cpf)
                and ValidacaoEntradas.valida_email(email)
                and ValidacaoEntradas.valida_oab(oab)
                and ValidacaoEntradas.valida_telefone(celular)
                and ValidacaoEntradas.valida_senha(senha)
            ):
                self.adv_service.cadastra_advogado(
                    nome, cpf, oab, senha, email, celular
                )
                self.adv_service.adiciona_especialidade_por_cpf(
                    cpf, especialidade
                )

        except Exception as erro:
            raise erro

    def buscar_advogado(self, cpf):
        return self.adv_service.busca_advogado(cpf)

    def listar_advogados(self):
        advogados = []
        for advogado in self.adv_service.lista_advogados():
            advogados.append(
                {
                    'nome': advogado.nome,
                    'oab': advogado.oab,
                    'processos': self.lista_processos_especialidade(
                        self.especialidade_advogado(advogado.cpf)
                    ),
                }
            )
        return advogados

    def atualizar_nome_advogado(self, cpf, nome):
        if nome:
            self.adv_service.atualiza_advogado(cpf, 'nome', nome)

    def atualizar_email_advogado(self, cpf, email):
        if ValidacaoEntradas.valida_email(email):
            self.adv_service.atualiza_advogado(cpf, 'email', email)

    def atualizar_oab_advogado(self, cpf, oab):
        if ValidacaoEntradas.valida_oab(oab):
            self.adv_service.atualiza_advogado(cpf, 'oab', oab)

    def atualizar_telefone_advogado(self, cpf, telefone):
        if ValidacaoEntradas.valida_telefone(telefone):
            self.adv_service.atualiza_advogado(cpf, 'telefone', telefone)

    def atualizar_senha_advogado(self, cpf, senha):
        if ValidacaoEntradas.valida_senha(senha):
            self.atualiza_advogado(cpf, 'senha', senha)

    def verifica_senha(self, cpf, senha):
        if self.adv_service.valida_senha(cpf, senha):
            return True
        return False

    def validar_acesso(self, cpf, senha):
        try:
            if self.adv_service.valida_senha(cpf, senha):
                advogado = self.buscar_advogado(cpf)
                return {
                    'acesso': True,
                    'erro': '',
                    'estado': {
                        'nome': advogado.nome,
                        'cpf': advogado.cpf,
                        'oab': advogado.oab,
                        'email': advogado.email,
                        'contato': advogado.celular,
                        'admin': advogado.admin,
                    },
                }
            else:
                return {
                    'acesso': False,
                    'erro': '',
                    'estado': {},
                }
        except Exception as e:
            return {'acesso': False, 'error': str(e), 'estado': {}}

    def lista_processos_especialidade(self, tipo_especialidade):
        processos = []
        for (
            processo
        ) in self.processo_service.lista_processos_por_especialidade(
            tipo_especialidade
        ):
            processos.append(
                {
                    'numero': processo.num_processo,
                    'comarca': processo.comarca,
                    'vara': processo.vara,
                    'distribuicao': processo.data_distribuicao,
                }
            )
        return processos

    def especialidade_advogado(self, cpf):
        return self.adv_service.especialidade_do_advogado(cpf)
