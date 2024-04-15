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

def correspondecia_modelos (imagem, template):
    return cv2.matchTemplate(imagem, template, cv2.TM_CCOEFF_NORMED)

def order_points(pts):
    rect = np.zeros((4, 2), dtype = "float32")

    s = pts.sum(axis = 1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]

    diff = np.diff(pts, axis = 1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]

    return rect

def four_point_transform(image, pts):

    rect = order_points(pts)
    (tl, tr, br, bl) = rect

    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))

    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))

    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype = "float32")

    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

    return warped
