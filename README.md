# ISR-Dataset

##Argumentos:

### Caminhos

caminho do output: ex.: --input ./input/
caminho de imput: ex.: --output ./dataset/

### Fator de downscale

--scale 4

### Metodos de downscale:

bicubica: --bicubica
bilinear: --bilinear
vizinho mais proximo: --mais_proximo

### exemplo completo

python -m src.main --input ./input/ --output ./dataset/ --scale 4 --bicubica --bilinear --mais_proximo 
