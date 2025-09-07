import argparse
from typing import Union
from src.processes.methods.bicubica_method import Bicubica_method
from src.processes.methods.bilinear_method import Bilinear_method
from src.processes.methods.vizinho_mais_proximo_method import Vizinho_Mais_Proximo_method
from src.processes.methods.Method import Method

class args:
    def getArgs(self) -> Union[str, str, int, list[Method]]: 

        parser = argparse.ArgumentParser(description="Exemplo de script com parâmetros")

        parser.add_argument("--input", type=str, required=True, help="Diretório de imagens HR")
        parser.add_argument("--output", type=str, required=True, help="Diretório para salvar LR")
        parser.add_argument("--scale", type=int, default=4, help="Fator de downscale (ex: 2, 4, 8)")
        parser.add_argument("--bicubica", action="store_true", help="Ativa o método bicúbico")
        parser.add_argument("--bilinear", action="store_true", help="Ativa o método bilinear")
        parser.add_argument("--mais_proximo", action="store_true", help="Ativa o método vizinho mais proximo")

        args = parser.parse_args()
        methods = []

        if(args.bicubica):
            bicubica = Bicubica_method()
            methods.append(bicubica)

        if(args.bilinear):
            bilinear = Bilinear_method()
            methods.append(bilinear)

        if(args.mais_proximo):
            proximo = Vizinho_Mais_Proximo_method()
            methods.append(proximo)


        return [args.input, args.output, args.scale, methods]

