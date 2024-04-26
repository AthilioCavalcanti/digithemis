from services import ClienteService, DocumentoService
from utils import ValidacaoEntradas, GerenciamentoDiretorios
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
                {'nome': c.nome, 'cpf_cnpj': c.cpf_cnpj, 'documentos': []}
            )
        return clientes

    def listar_clientes_especialidade(self, tipo_especialidade):
        clientes = []
        for c in self.cliente.lista_clientes_por_especialidade(
            tipo_especialidade
        ):
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
            documentos = self.doc_service.busca_documentos(
                id_cliente=c.id_cliente
            )
            lista_docs = []
            if documentos:
                for documento in documentos:
                    lista_docs.append(
                        {
                            'titulo': documento.titulo,
                            'categoria': documento.categoria,
                            'insercao': documento.data_insercao,
                            'arquivo': '',
                        }
                    )
            return lista_docs
        except Exception:
            return []

    def salvar_documentos_cliente(self, cpf_cnpj, lista_arquivos):
        c = self.cliente.busca_cliente(cpf_cnpj)
        primeiro_nome_cliente = self._obter_primeiro_nome_cliente_sem_acentos(
            c.nome
        )
        for infos_arquivo in lista_arquivos:
            try:
                arquivo = os.path.basename(infos_arquivo['caminho'])
                _, extensao = os.path.splitext(arquivo)

                classificacao = infos_arquivo['tipo']
                titulo_base = f'{classificacao}_{primeiro_nome_cliente}'

                documento_existente = self.doc_service.buscar_documento_por_titulo(titulo_base)
                if documento_existente:
                    num = 0
                    while documento_existente:
                        num += 1
                        titulo = f"{titulo_base}_{num}"
                        documento_existente = self.doc_service.buscar_documento_por_titulo(titulo)
                else:
                    titulo = titulo_base

                with open(infos_arquivo['caminho'], 'rb') as arquivo:
                    self.doc_service.insere_documento(
                        c.id_cliente, titulo, extensao, arquivo.read()
                    )
            except Exception:
                raise Exception('Erro ao salvar arquivos')

        if lista_arquivos:
            diretorio_base = os.path.expanduser('~/digithemis')

            diretorio_cliente = self._remover_acentos(c.nome)
            caminho_diretorio_cliente = os.path.join(
                diretorio_base, diretorio_cliente
            )

            if not os.path.exists(caminho_diretorio_cliente):
                os.makedirs(caminho_diretorio_cliente)
                print(f"Pasta '{diretorio_cliente}' criada em '{diretorio_base}'")

            GerenciamentoDiretorios.mover_arquivos_e_renomear(
                lista_arquivos, caminho_diretorio_cliente, primeiro_nome_cliente
            )

    def _obter_primeiro_nome_cliente_sem_acentos(self, nome_completo):
        primeiro_nome = nome_completo.split()[0].lower()
        primeiro_nome_sem_acentos = self._remover_acentos(primeiro_nome)
        return primeiro_nome_sem_acentos

    def _remover_acentos(self, s):
        return ''.join(
            c
            for c in unicodedata.normalize('NFD', s)
            if unicodedata.category(c) != 'Mn'
        )
