# Generated from gcode.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .gcodeParser import gcodeParser
else:
    from gcodeParser import gcodeParser

# This class defines a complete listener for a parse tree produced by gcodeParser.
class gcodeListener(ParseTreeListener):

    # Enter a parse tree produced by gcodeParser#def.
    def enterDef(self, ctx:gcodeParser.DefContext):
        pass

    # Exit a parse tree produced by gcodeParser#def.
    def exitDef(self, ctx:gcodeParser.DefContext):
        pass


    # Enter a parse tree produced by gcodeParser#fimprograma.
    def enterFimprograma(self, ctx:gcodeParser.FimprogramaContext):
        pass

    # Exit a parse tree produced by gcodeParser#fimprograma.
    def exitFimprograma(self, ctx:gcodeParser.FimprogramaContext):
        pass


    # Enter a parse tree produced by gcodeParser#statement.
    def enterStatement(self, ctx:gcodeParser.StatementContext):
        pass

    # Exit a parse tree produced by gcodeParser#statement.
    def exitStatement(self, ctx:gcodeParser.StatementContext):
        pass


    # Enter a parse tree produced by gcodeParser#numerolinha.
    def enterNumerolinha(self, ctx:gcodeParser.NumerolinhaContext):
        pass

    # Exit a parse tree produced by gcodeParser#numerolinha.
    def exitNumerolinha(self, ctx:gcodeParser.NumerolinhaContext):
        pass


    # Enter a parse tree produced by gcodeParser#num3dig.
    def enterNum3dig(self, ctx:gcodeParser.Num3digContext):
        pass

    # Exit a parse tree produced by gcodeParser#num3dig.
    def exitNum3dig(self, ctx:gcodeParser.Num3digContext):
        pass


    # Enter a parse tree produced by gcodeParser#mfim.
    def enterMfim(self, ctx:gcodeParser.MfimContext):
        pass

    # Exit a parse tree produced by gcodeParser#mfim.
    def exitMfim(self, ctx:gcodeParser.MfimContext):
        pass


    # Enter a parse tree produced by gcodeParser#mfunc.
    def enterMfunc(self, ctx:gcodeParser.MfuncContext):
        pass

    # Exit a parse tree produced by gcodeParser#mfunc.
    def exitMfunc(self, ctx:gcodeParser.MfuncContext):
        pass


    # Enter a parse tree produced by gcodeParser#codfunc.
    def enterCodfunc(self, ctx:gcodeParser.CodfuncContext):
        pass

    # Exit a parse tree produced by gcodeParser#codfunc.
    def exitCodfunc(self, ctx:gcodeParser.CodfuncContext):
        pass


    # Enter a parse tree produced by gcodeParser#coordx.
    def enterCoordx(self, ctx:gcodeParser.CoordxContext):
        pass

    # Exit a parse tree produced by gcodeParser#coordx.
    def exitCoordx(self, ctx:gcodeParser.CoordxContext):
        pass


    # Enter a parse tree produced by gcodeParser#coordy.
    def enterCoordy(self, ctx:gcodeParser.CoordyContext):
        pass

    # Exit a parse tree produced by gcodeParser#coordy.
    def exitCoordy(self, ctx:gcodeParser.CoordyContext):
        pass


    # Enter a parse tree produced by gcodeParser#coordi.
    def enterCoordi(self, ctx:gcodeParser.CoordiContext):
        pass

    # Exit a parse tree produced by gcodeParser#coordi.
    def exitCoordi(self, ctx:gcodeParser.CoordiContext):
        pass


    # Enter a parse tree produced by gcodeParser#coordj.
    def enterCoordj(self, ctx:gcodeParser.CoordjContext):
        pass

    # Exit a parse tree produced by gcodeParser#coordj.
    def exitCoordj(self, ctx:gcodeParser.CoordjContext):
        pass


    # Enter a parse tree produced by gcodeParser#coord.
    def enterCoord(self, ctx:gcodeParser.CoordContext):
        pass

    # Exit a parse tree produced by gcodeParser#coord.
    def exitCoord(self, ctx:gcodeParser.CoordContext):
        pass


    # Enter a parse tree produced by gcodeParser#fimdelinha.
    def enterFimdelinha(self, ctx:gcodeParser.FimdelinhaContext):
        pass

    # Exit a parse tree produced by gcodeParser#fimdelinha.
    def exitFimdelinha(self, ctx:gcodeParser.FimdelinhaContext):
        pass



del gcodeParser