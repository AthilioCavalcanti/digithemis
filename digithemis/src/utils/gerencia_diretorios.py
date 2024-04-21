import os
import shutil


class GerenciamentoDiretorios:
    @staticmethod
    def criar_diretorio(nome_diretorio):
        caminho_base = os.path.expanduser("~/")  

        caminho_diretorio = os.path.join(caminho_base, nome_diretorio)
        if not os.path.exists(caminho_diretorio):
            os.makedirs(caminho_diretorio)

    @staticmethod
    def mover_arquivos_para_pasta(lista_caminhos, pasta_destino):
        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)

        for caminho_arquivo in lista_caminhos:
            if os.path.isfile(caminho_arquivo):
                nome_arquivo = os.path.basename(caminho_arquivo)
                novo_caminho = os.path.join(pasta_destino, nome_arquivo)
                shutil.move(caminho_arquivo, novo_caminho)