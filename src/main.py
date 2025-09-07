from src.processes.exec.exec import Executor
from src.presentation.args import args

def main():

    [input, output, scale, methods] = args().getArgs()

    _exec = Executor(input, output, scale,  methods)
    _exec.run()


main()