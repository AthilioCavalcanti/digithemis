from pdf2image import convert_from_path
import os

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

# Exemplo de uso:
pdf_path = "Documentos\Contrato 01.pdf"
output_folder = "C:\\Users\\Windows10\\Desktop\\OCR\\Imagem_PDF"

converter_pdf_para_imagens(pdf_path, output_folder)