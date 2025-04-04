import cv2
import numpy as np
from PIL import Image, ImageChops

def comparar_imagens(img1_path, img2_path, output_path="diff.png"):
    # Carregar as imagens
    img1 = cv2.imread("/Users/evertonalves/Documents/cpimg/baseline/IMG_5138.PNG")
    img2 = cv2.imread("/Users/evertonalves/Documents/cpimg/newbaseline/IMG_5138.PNG")

    #img1 = cv2.imread("baseline/IMG_5138.PNG")
    #img2 = cv2.imread("newbaseline/IMG_5138.PNG")

    # Verificar se as imagens têm o mesmo tamanho
    if img1.shape != img2.shape:
        print("As imagens têm tamanhos diferentes! Comparação não pode ser feita.")
        return

    # Converter para escala de cinza
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # Calcular a diferença entre as imagens
    diff = cv2.absdiff(gray1, gray2)
    
    # Aplicar um threshold para destacar diferenças
    _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

    # Criar máscara de cor vermelha para destacar diferenças
    mask = np.zeros_like(img1)
    mask[thresh > 0] = [0, 0, 255]  # Vermelho

    # Mesclar a máscara vermelha com a imagem original
    highlighted = cv2.addWeighted(img1, 0.8, mask, 0.5, 0)

    # Salvar a imagem de diferença
    cv2.imwrite(output_path, highlighted)
    print(f"Diferenças destacadas salvas em: {output_path}")

# Teste do script
comparar_imagens("imagem1.png", "imagem2.png", "resultado.png")