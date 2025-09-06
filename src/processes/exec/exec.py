import os
import shutil
from PIL import Image
from ..methods.Method import Method

class Executor:
    def __init__(self, input_path: str, output_path,  methods: list[Method]):
        self.methods = methods
        self.input_path = input_path
        self.output_path = output_path
        # cria o diretório de saída se não existir
        os.makedirs(self.output_path, exist_ok=True)


    def run(self):
        print(f"reading images from {self.input_path} ")

        # lista todos os arquivos do diretório de entrada
        for filename in os.listdir(self.input_path):
            file_path = os.path.join(self.input_path, filename)

            # verifica se é arquivo
            if os.path.isfile(file_path):
                print(f"Processing: {filename}")

                img = Image.open(file_path)
                print(img.format, img.size, img.mode)  # Exemplo: JPEG (1920,1080) RGB

                # copia o arquivo para o output
                dest_path = os.path.join(self.output_path, filename)
                shutil.copy(file_path, dest_path)

        # roda os métodos
        for method in self.methods:
            method.generateReport()

