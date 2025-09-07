from src.processes.methods.Method import Method
from PIL import Image

class Bicubica_method(Method):
    def name(self):
        return "bicubica"
    
    def execute(self, img: Image.Image, scale: int)  -> Image.Image:
        w, h = img.size
        return img.resize((w // scale, h // scale), Image.BICUBIC)

    