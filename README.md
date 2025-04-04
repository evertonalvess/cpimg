# Comparador de Imagens - CPIMG

Este projeto compara imagens entre duas pastas (`baseline` e `newbaseline`) e gera uma pasta de resultados contendo apenas as imagens que apresentaram diferenças visíveis.

## 📌 Funcionalidades

- **Comparação automática** entre imagens das pastas `baseline` e `newbaseline`.
- **Destaque de diferenças** em vermelho.
- **Armazenamento dos resultados** na pasta `results`, com um novo diretório gerado a cada execução.
- **Exclusão automática** de imagens sem diferenças, mantendo apenas os arquivos alterados.

## 📁 Estrutura de Pastas

```
cpimg/
│── baseline/        # Imagens corretas (versão de referência)
│── newbaseline/     # Novas imagens a serem comparadas
│── results/         # Resultados das comparações
│   ├── Result_-_aaaa.mm.dd_-_hh.mm.ss/  # Pasta gerada automaticamente
│       ├── IMG_5138.PNG  # Exemplo de imagem com diferenças
│── cpimg.py         # Script de comparação
│── README.md        # Documentação
```

## 🚀 Como Usar

### 1️⃣ **Pré-requisitos**

- Python 3 instalado
- Bibliotecas necessárias:
  ```bash
  pip install opencv-python numpy
  ```

### 2️⃣ **Organize suas imagens**

Coloque as imagens na estrutura correta:

- `` → Contém as imagens corretas
- `` → Contém as novas imagens (com o mesmo nome das imagens em `baseline`)

### 3️⃣ **Execute o script**

No terminal, rode o seguinte comando:

```bash
python3 cpimg.py
```

### 4️⃣ **Verifique os resultados**

Após a execução, uma nova pasta será criada dentro de `results/`, com o nome no formato:

```
Result_-_aaaa.mm.dd_-_hh.mm.ss/
```

Apenas as imagens com diferenças serão salvas nesta pasta.

## ⚙️ Como Funciona

1. O script varre a pasta `baseline/` e busca imagens com o mesmo nome na pasta `newbaseline/`.
2. Se as imagens forem de tamanhos diferentes, a comparação é ignorada.
3. As imagens são convertidas para escala de cinza e comparadas.
4. As diferenças são destacadas em vermelho.
5. Apenas as imagens com diferenças são salvas na pasta `results/Result_-_aaaa.mm.dd_-_hh.mm.ss/`.

## 🛠 Tecnologias Utilizadas

- **Python 3**
- **OpenCV** (para manipulação de imagens)
- **NumPy** (para cálculos de diferenças)
- **OS e Datetime** (para organização dos arquivos)

## 📌 Exemplo de Saída

Se `IMG_5138.PNG` tiver diferenças, o resultado ficará assim:

```
results/
└── Result_-_2025.04.03_-_16.30.15/
       ├── IMG_5138.PNG
```

## 📄 Licença

Este projeto é de uso livre. Sinta-se à vontade para modificar e melhorar! 🚀

