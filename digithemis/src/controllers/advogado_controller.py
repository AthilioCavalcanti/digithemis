from services import AdvogadoService
from utils import ValidacaoEntradas


class AdvogadoController:
    def __init__(self):
        self.adv_service = AdvogadoService()

    def adicionar_advogado(self, nome, cpf, oab, email, celular, senha):
        pass

    def buscar_advogado(self, cpf):
        return self.adv_service.busca_advogado(cpf)

    def atualizar_nome_advogado(self, cpf, nome):
        if nome:
            self.adv_service.atualiza_advogado(cpf, 'nome', nome)

    def atualizar_email_advogado(self, cpf, email):
        if ValidacaoEntradas.valida_email(email):
            self.adv_service.atualiza_advogado(cpf, 'email', email)

    def atualizar_oab_advogado(self, cpf, oab):
        if ValidacaoEntradas.valida_oab:
            self.adv_service.atualiza_advogado(cpf, 'oab', oab)

    def atualizar_telefone_advogado(self, cpf, telefone):
        if telefone:
            self.adv_service.atualiza_advogado(cpf, 'telefone', telefone)

    def atualiza_senha_advogado(self, cpf, senha):
        if ValidacaoEntradas.valida_senha(senha):
            self.atualiza_senha_advogado(cpf, senha)

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
