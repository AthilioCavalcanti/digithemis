import cv2
import numpy as np
import matplotlib.pyplot as plt

def plot_image(img, cmap=None):
    plt.imshow(img, cmap=cmap)
    plt.xticks([])
    plt.yticks([])

def Converte_cinza(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def filtro_bilateral(image):
    return cv2.bilateralFilter(image, d=9, sigmaColor=75, sigmaSpace=75)

def segmentar(imagem):
    _, imagem_segmentada = cv2.threshold(imagem, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return imagem_segmentada

def contornos_internos(imagem):
    contours, _ = cv2.findContours(imagem, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    outline_contours = img.copy()
    imagem_contorno = cv2.drawContours(outline_contours, contours, contourIdx=-1, color=(0, 255, 0))
    return imagem_contorno

def contornos_borda(imagem):
    contours, _ = cv2.findContours(imagem, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    all_contours = cv2.cvtColor(imagem, cv2.COLOR_GRAY2RGB)  # Convertendo para RGB
    contornos_borda = cv2.drawContours(all_contours, contours, -1, (0, 255, 0), 3)
    return contornos_borda