from services import ClienteService, DocumentoService
from utils import ValidacaoEntradas
import os
import unicodedata


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
        
    def salvar_documentos_cliente(self, cpf_cnpj, lista_caminhos_arquivos):
        c = self.cliente.busca_cliente(cpf_cnpj)
        for caminho_arquivo in lista_caminhos_arquivos:
            try:
                # Obter o nome do arquivo a partir do caminho
                titulo = os.path.basename(caminho_arquivo)
                # Extrair a categoria do arquivo (você pode adaptar essa parte conforme necessário)
                categoria = os.path.splitext(titulo)[1].replace(".", "")
                
                # Ler o arquivo
                with open(caminho_arquivo, 'rb') as arquivo:
                    # Chamar a função insere_documento para salvar no banco
                    self.insere_documento(c.id_cliente, titulo, categoria, arquivo.read())
            except Exception as erro:
                print(f"Erro ao salvar o arquivo {caminho_arquivo}: {str(erro)}")

    def salvar_documentos_cliente(self, cpf_cnpj, lista_caminhos_arquivos):
        c = self.cliente.busca_cliente(cpf_cnpj)
        for caminho_arquivo in lista_caminhos_arquivos:
            try:
                arquivo = os.path.basename(caminho_arquivo)
                _, extensao = os.path.splitext(arquivo)

                primeiro_nome_cliente = self.obter_primeiro_nome_cliente_sem_acentos(c.nome)

                classificacao = self.classificar_documento(arquivo)
                with open(caminho_arquivo, 'rb') as arquivo:
                    titulo = f"{classificacao}_{primeiro_nome_cliente}"
                    
                    self.insere_documento(c.id_cliente, titulo, extensao, arquivo.read())
            except Exception as erro:
                print(f"Erro ao salvar o arquivo {caminho_arquivo}: {str(erro)}")

    def obter_primeiro_nome_cliente_sem_acentos(self, nome_completo):
        primeiro_nome = nome_completo.split()[0]
        primeiro_nome_sem_acentos = self.remover_acentos(primeiro_nome)
        return primeiro_nome_sem_acentos

    def remover_acentos(self, s):
        return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')
    
    
