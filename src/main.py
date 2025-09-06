from processes.downscale.downscale import Downscale
from processes.methods.bicubica.bicubica_modelo import Bicubica_method
from processes.exec.exec import Executor

def main():

    
    bicubica = Bicubica_method()
    methods = [bicubica]

    _exec = Executor("./input/", "./output/", methods)
    _exec.run()


main()