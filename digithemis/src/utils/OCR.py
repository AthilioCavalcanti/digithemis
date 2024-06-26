import cv2
import numpy as np
import pytesseract
import os
from .Imagem import (
    Converte_cinza,
    filtro_bilateral,
    segmentar,
    contornos_internos,
    corretor_rotacao,
)
from .PDF_Leitor import converter_pdf_para_lista_imagens


def ler_imagem(caminho):
    # Carrega a imagem
    img = cv2.imread(caminho)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img


def converter_imagem_para_string(imagem):
    # Converte a imagem em escala de cinza
    img_gray = Converte_cinza(imagem)
    # Aplica Filtro Bilateral
    img_filtro = filtro_bilateral(img_gray)
    # segmentação por binarização e Otsu
    img_seg = segmentar(img_filtro)
    # Realiza o OCR na imagem
    texto_reconhecido = pytesseract.image_to_string(img_seg, lang='por')
    return texto_reconhecido


def procurar_string(texto, string_procurada):
    if string_procurada in texto:
        return True
    else:
        return False


def buscar_palavra_em_pdf_imagens(diretorio, palavra_procurada):
    arquivos_com_palavra = []
    for raiz, _, arquivos in os.walk(diretorio):
        for arquivo in arquivos:
            caminho_arquivo = os.path.join(raiz, arquivo)

            if arquivo.lower().endswith(('.jpg', '.jpeg', '.png')):
                imagem = cv2.imread(caminho_arquivo)
                texto = converter_imagem_para_string(imagem)
                classificacao = classificar_documento(texto)
                if procurar_string(texto, palavra_procurada):
                    arquivos_com_palavra.append(
                        {'tipo': classificacao, 'caminho': caminho_arquivo}
                    )

            elif arquivo.lower().endswith('.pdf'):
                imagens_pdf = converter_pdf_para_lista_imagens(caminho_arquivo)
                for img in imagens_pdf:
                    imagem_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    texto = converter_imagem_para_string(imagem_rgb)
                    classificacao = classificar_documento(texto)
                    if procurar_string(texto, palavra_procurada):
                        arquivos_com_palavra.append(
                            {'tipo': classificacao, 'caminho': caminho_arquivo}
                        )
                        break
    return arquivos_com_palavra


def classificar_documento(texto):
    primeira_palavra = texto.split()[0]

    if primeira_palavra.lower() == 'procuração':
        return 'procuracao'
    elif primeira_palavra.lower() == 'contrato':
        return 'contrato'
    elif primeira_palavra.lower() == 'processo':
        return 'processo'
    else:
        return 'desconhecido'
