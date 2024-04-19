from services import ClienteService
from utils import ValidacaoEntradas


class ClienteController:
    def __init__(self):
        self.cliente = ClienteService()

    def adicionar_cliente(self, nome, cpf_cnpj, email, telefone):
        try:
            if ValidacaoEntradas.valida_cpf_cnpj(
                cpf_cnpj
            ) and ValidacaoEntradas.valida_email(email):
                self.cliente.cadastra_cliente(nome, cpf_cnpj, email, telefone)
        except Exception as erro:
            raise erro
