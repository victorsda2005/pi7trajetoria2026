import os
from antlr4 import *

from gcodeLexer import gcodeLexer
from gcodeParser import gcodeParser

from gcodecustomvisitor import GcodeCoordVisitor
from gerador_trajetoria import GeradorTrajetoria


def main():

    ####################################################
    # Lê o arquivo G-code
    ####################################################

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    arquivo = os.path.join(BASE_DIR, "codigoreta.gcode")

    input_stream = FileStream(arquivo)

    ####################################################
    # Lexer
    ####################################################

    lexer = gcodeLexer(input_stream)

    ####################################################
    # Token Stream
    ####################################################

    tokens = CommonTokenStream(lexer)

    ####################################################
    # Parser
    ####################################################

    parser = gcodeParser(tokens)

    ####################################################
    # Árvore Sintática
    ####################################################

    tree = parser.def_()

    ####################################################
    # Visitor
    ####################################################

    visitor = GcodeCoordVisitor()

    visitor.visit(tree)

    ####################################################
    # Lista de movimentos
    ####################################################

    movimentos = visitor.coordenadas

    print("Movimentos encontrados:\n")

    for mov in movimentos:
        print(mov)

    ####################################################
    # Geração da trajetória
    ####################################################

    gerador = GeradorTrajetoria()

    tabela = gerador.gerar(movimentos)

    ####################################################
    # Exibe a tabela
    ####################################################

    print("\nTabela de pontos:\n")

    for ponto in tabela:
        print(ponto)


if __name__ == "__main__":
    main()