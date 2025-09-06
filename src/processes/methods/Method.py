from abc import ABC, abstractmethod

class Method(ABC):
    def generateReport(self):
        print(f" -------------- applying downscale: {self.name()} method --------------")

    @abstractmethod
    def name(self):
        pass

    