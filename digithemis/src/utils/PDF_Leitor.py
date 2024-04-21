from pdf2image import convert_from_path
import os
import numpy as np

def converter_pdf_para_imagens(pdf_path, output_folder):
    # Verificar se o diretório de saída existe, caso contrário, criar
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Converter páginas do PDF em imagens JPEG
    imagens = convert_from_path(pdf_path)

    # Salvar as imagens em formato JPEG
    for i, imagem in enumerate(imagens):
        imagem_path = os.path.join(output_folder, f"pagina_{i+1}.jpg")
        imagem.save(imagem_path, "JPEG")

    print("Conversão concluída. Imagens salvas em:", output_folder)

def converter_pdf_para_lista_imagens(pdf_path):
    imagens = convert_from_path(pdf_path)

    imagens_np = [np.array(imagem) for imagem in imagens]

    return imagens_np
