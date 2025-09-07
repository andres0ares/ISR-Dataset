from src.processes.methods.Method import Method
from PIL import Image

class Vizinho_Mais_Proximo_method(Method):
    def name(self):
        return "Vizinho mais proximo"
    
    def execute(self, img: Image.Image, scale: int)  -> Image.Image:
        w, h = img.size
        return img.resize((w // scale, h // scale), Image.NEAREST)

    