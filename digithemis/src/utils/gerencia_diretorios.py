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

    @staticmethod
    def mover_arquivos_e_renomear(lista_arquivos, pasta_destino, nome_cliente):
        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)

        for arquivo_info in lista_arquivos:
            try:
                caminho_arquivo = arquivo_info['caminho']
                nome_arquivo = os.path.basename(caminho_arquivo)
                _, extensao = os.path.splitext(nome_arquivo)

                nome_arquivo_final = f"{arquivo_info['tipo']}_{nome_cliente}{extensao}"

                arquivo_destino = os.path.join(pasta_destino, nome_arquivo_final)
                contador = 1
                while os.path.exists(arquivo_destino):
                    nome_arquivo_final = f"{arquivo_info['tipo']}_{nome_cliente}_{contador}{extensao}"
                    arquivo_destino = os.path.join(pasta_destino, nome_arquivo_final)
                    contador += 1
                
                shutil.move(caminho_arquivo, arquivo_destino)
            except Exception as erro:
                print(f"Erro ao mover o arquivo {caminho_arquivo}: {str(erro)}")
