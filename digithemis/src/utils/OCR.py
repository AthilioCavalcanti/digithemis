import cv2
import numpy as np
import pytesseract

def ler_imagem(caminho):
    # Carrega a imagem
    img = cv2.imread(caminho)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

def converter_imagem_para_string(imagem):
    # Converte a imagem em escala de cinza
    img_gray = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)
    # Realiza o OCR na imagem
    texto_reconhecido = pytesseract.image_to_string(img_gray, lang='por')
    return texto_reconhecido

def procurar_string(texto, string_procurada):
    if string_procurada in texto:
        return True
    else:
        return False