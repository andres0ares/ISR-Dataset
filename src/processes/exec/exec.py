import os
import shutil
from PIL import Image
from src.processes.methods.Method import Method

class Executor:
    def __init__(self, input_path: str, output_path, scale: int, methods: list[Method]):

        self.methods = methods
        self.input_path = input_path
        self.output_path = output_path
        self.scale = scale

        # cria o diretório de saída se não existir
        os.makedirs(self.output_path + "HR/", exist_ok=True)
        os.makedirs(self.output_path + "LR/", exist_ok=True)

    def total_digits(self) -> int:
        exts = (".png", ".jpg", ".jpeg")
        return len(str(len([f for f in os.listdir(self.input_path) if f.lower().endswith(exts)]) + len(self.methods)))


    def run(self):

        print(f"reading images from {self.input_path} ")
        count = 0
        digits = self.total_digits()

        # lista todos os arquivos do diretório de entrada
        for filename in os.listdir(self.input_path):
            file_path = os.path.join(self.input_path, filename)

            # verifica se é arquivo
            if os.path.isfile(file_path):

                print(f"Processing: {filename}")
                img = Image.open(file_path)
                print(img.format, img.size, img.mode)  # Exemplo: JPEG (1920,1080) RGB

                for method in self.methods:
                    count += 1
                    method.generateReport()
                    img_out = method.execute(img, self.scale)
                    img_out.save(os.path.join(self.output_path + "LR/", f"img_{count:0{digits}d}.png"))
                    img.save(os.path.join(self.output_path + "HR/", f"img_{count:0{digits}d}.png"))


