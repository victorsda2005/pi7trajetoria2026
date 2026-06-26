# Generated from gcode.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .gcodeParser import gcodeParser
else:
    from gcodeParser import gcodeParser

# This class defines a complete generic visitor for a parse tree produced by gcodeParser.

class gcodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by gcodeParser#def.
    def visitDef(self, ctx:gcodeParser.DefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gcodeParser#fimprograma.
    def visitFimprograma(self, ctx:gcodeParser.FimprogramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gcodeParser#statement.
    def visitStatement(self, ctx:gcodeParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gcodeParser#numerolinha.
    def visitNumerolinha(self, ctx:gcodeParser.NumerolinhaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gcodeParser#num3dig.
    def visitNum3dig(self, ctx:gcodeParser.Num3digContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gcodeParser#mfim.
    def visitMfim(self, ctx:gcodeParser.MfimContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gcodeParser#mfunc.
    def visitMfunc(self, ctx:gcodeParser.MfuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gcodeParser#codfunc.
    def visitCodfunc(self, ctx:gcodeParser.CodfuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gcodeParser#coordx.
    def visitCoordx(self, ctx:gcodeParser.CoordxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gcodeParser#coordy.
    def visitCoordy(self, ctx:gcodeParser.CoordyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gcodeParser#coordi.
    def visitCoordi(self, ctx:gcodeParser.CoordiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gcodeParser#coordj.
    def visitCoordj(self, ctx:gcodeParser.CoordjContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gcodeParser#coord.
    def visitCoord(self, ctx:gcodeParser.CoordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gcodeParser#fimdelinha.
    def visitFimdelinha(self, ctx:gcodeParser.FimdelinhaContext):
        return self.visitChildren(ctx)



del gcodeParser