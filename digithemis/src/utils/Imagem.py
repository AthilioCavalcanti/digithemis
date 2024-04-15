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