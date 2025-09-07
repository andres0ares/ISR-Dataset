from abc import ABC, abstractmethod
from PIL import Image

class Method(ABC):
    def generateReport(self):
        print(f" -------------- applying downscale: {self.name()} method --------------")

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def execute(self, img: Image.Image, scale: int)  -> Image.Image:
        pass

    