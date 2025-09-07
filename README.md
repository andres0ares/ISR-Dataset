# ISR-Dataset

Este dataset foi construído para o treinamento e avaliação de modelos de Image Super-Resolution (ISR), cujo objetivo é aumentar a resolução de imagens de baixa qualidade, recuperando detalhes e aproximando-se da versão original em alta resolução (HR).  

O pipeline recebe como entrada um diretório contendo imagens em alta resolução (HR) e gera automaticamente as versões em baixa resolução (LR) aplicando diferentes métodos de downscale.

## Como executar:   

### Caminhos   

caminho do output: ex.: --input ./input/   
caminho de imput: ex.: --output ./dataset/   

### Fator de downscale

--scale 4

### Metodos de downscale:

bicubica: --bicubica   
bilinear: --bilinear   
vizinho mais proximo: --mais_proximo   

### Exemplo completo

python -m src.main --input ./input/ --output ./dataset/ --scale 4 --bicubica --bilinear --mais_proximo 

---

## 📂 Estrutura do Dataset

Após a execução, o dataset fica organizado da seguinte forma:

dataset/  
│── HR/ # imagens originais em alta resolução  
│ ├── img_001.png  
│ └── ...  
│  
│── LR/ # imagens em baixa resolução (geradas)  
│ ├── img_001.png  
│ ├── img_002.png  
│ ├── img_003.png  
│ └── ...  

## 🤔 Por que gerar várias versões LR?  

Cada método de downscale degrada a imagem de forma diferente, simulando diversos cenários reais de perda de qualidade:  

Vizinho mais próximo (mais_proximo) → causa pixelização, comum em ampliações simples.  
Bilinear (bilinear) → gera borrões leves, simulando compressões básicas.    
Bicúbica (bicubica) → produz borrões mais suaves, semelhante a algoritmos usados em softwares de edição.
  
#### 👉 Ter múltiplas versões LR para a mesma HR permite que o modelo aprenda a reconstruir imagens de diferentes tipos de degradação.
Isso aumenta a robustez e a generalização do modelo, tornando-o mais capaz de lidar com imagens reais que podem ter sido degradadas de formas variadas.
