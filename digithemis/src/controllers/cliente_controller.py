from services import ClienteService, DocumentoService
from utils import ValidacaoEntradas


class ClienteController:
    def __init__(self):
        self.cliente = ClienteService()
        self.doc_service = DocumentoService()

    def adicionar_cliente(self, nome, cpf_cnpj, email, telefone):
        try:
            if ValidacaoEntradas.valida_cpf_cnpj(
                cpf_cnpj
            ) and ValidacaoEntradas.valida_email(email):
                self.cliente.cadastra_cliente(nome, cpf_cnpj, email, telefone)
        except Exception as erro:
            raise erro

    def listar_clientes(self):
        clientes = []
        for c in self.cliente.lista_clientes():
            clientes.append(
                {
                    'nome': c.nome,
                    'cpf_cnpj': c.cpf_cnpj,
                    'documentos': []
                }
            )
        return clientes

    def listar_clientes_especialidade(self, tipo_especialidade):
        clientes = []
        for c in self.cliente.lista_clientes_por_especialidade(tipo_especialidade):
            clientes.append(
                {
                    'nome': c.nome,
                    'cpf_cnpj': c.cpf_cnpj,
                    'documentos': [],
                }
            )
        return clientes
    
    def buscar_cliente(self, cpf_cnpj):
        c = self.cliente.busca_cliente(cpf_cnpj)
        if c.ativo:
            return {
                'nome': c.nome,
                'cpf_cnpj': c.cpf_cnpj,
                'email': c.email,
                'contato': c.telefone,
                'empresa': c.empresa,
            }
        return None
    
    def busca_documentos_cliente(self, cpf_cnpj):
        c = self.cliente.busca_cliente(cpf_cnpj)
        try:
            documentos = self.doc_service.busca_documentos(id_cliente=c.id_cliente)
            lista_docs = []
            if documentos:
                for documento in documentos:
                    lista_docs.append(
                        {
                            'titulo': documento.titulo,
                            'categoria': documento.categoria,
                            'insercao': documento.data_insercao,
                            'arquivo': ''
                        }
                    )
            return lista_docs
        except Exception:
            return []
