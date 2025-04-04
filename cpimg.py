import cv2
import numpy as np
import os
from datetime import datetime

def comparar_imagens(img1_path, img2_path, output_path):
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)

    if img1 is None or img2 is None:
        print(f"Erro ao carregar: {img1_path} ou {img2_path}")
        return False

    if img1.shape != img2.shape:
        print(f"Tamanhos diferentes: {os.path.basename(img1_path)}")
        return False

    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    diff = cv2.absdiff(gray1, gray2)
    _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

    if np.count_nonzero(thresh) == 0:
        return False  # Sem diferença visível

    # Criar máscara vermelha
    mask = np.zeros_like(img1)
    mask[thresh > 0] = [0, 0, 255]
    highlighted = cv2.addWeighted(img1, 0.8, mask, 0.5, 0)

    cv2.imwrite(output_path, highlighted)
    print(f"[DIFERENÇA] {os.path.basename(output_path)}")
    return True

def processar_comparacoes():
    baseline_dir = "baseline"
    newbaseline_dir = "newbaseline"
    results_base = "results"

    # Criar pasta com timestamp atualizado (com segundos)
    timestamp = datetime.now().strftime("Result_-_%Y.%m.%d_-_%H.%M.%S")
    result_dir = os.path.join(results_base, timestamp)
    os.makedirs(result_dir, exist_ok=True)

    arquivos_baseline = os.listdir(baseline_dir)

    total_comparadas = 0
    total_diferencas = 0

    for nome_arquivo in arquivos_baseline:
        caminho_base = os.path.join(baseline_dir, nome_arquivo)
        caminho_novo = os.path.join(newbaseline_dir, nome_arquivo)

        if not os.path.exists(caminho_novo):
            print(f"[IGNORADO] Não encontrado em newbaseline: {nome_arquivo}")
            continue

        output_path = os.path.join(result_dir, nome_arquivo)
        houve_diferenca = comparar_imagens(caminho_base, caminho_novo, output_path)
        total_comparadas += 1

        if houve_diferenca:
            total_diferencas += 1
        else:
            if os.path.exists(output_path):  
                os.remove(output_path)  # Remove arquivos sem diferença

    print(f"\n✅ Comparação concluída.")
    print(f"Imagens comparadas: {total_comparadas}")
    print(f"Imagens com diferença: {total_diferencas}")
    print(f"Resultados salvos em: {result_dir}\n")

if __name__ == "__main__":
    processar_comparacoes()