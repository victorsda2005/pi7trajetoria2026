# Generated from gcode.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,16,102,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,4,0,30,8,0,11,0,12,0,31,1,0,1,0,1,1,1,1,1,1,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,68,8,2,1,3,1,3,1,3,1,4,1,
        4,1,4,1,4,1,5,1,5,1,6,1,6,1,6,3,6,82,8,6,1,7,1,7,1,8,1,8,1,8,1,9,
        1,9,1,9,1,10,1,10,1,10,1,11,1,11,1,11,1,12,1,12,1,13,1,13,1,13,0,
        0,14,0,2,4,6,8,10,12,14,16,18,20,22,24,26,0,2,1,0,5,7,1,0,12,13,
        94,0,29,1,0,0,0,2,35,1,0,0,0,4,67,1,0,0,0,6,69,1,0,0,0,8,72,1,0,
        0,0,10,76,1,0,0,0,12,81,1,0,0,0,14,83,1,0,0,0,16,85,1,0,0,0,18,88,
        1,0,0,0,20,91,1,0,0,0,22,94,1,0,0,0,24,97,1,0,0,0,26,99,1,0,0,0,
        28,30,3,4,2,0,29,28,1,0,0,0,30,31,1,0,0,0,31,29,1,0,0,0,31,32,1,
        0,0,0,32,33,1,0,0,0,33,34,3,2,1,0,34,1,1,0,0,0,35,36,3,6,3,0,36,
        37,3,10,5,0,37,3,1,0,0,0,38,39,3,6,3,0,39,40,3,14,7,0,40,41,3,16,
        8,0,41,42,3,18,9,0,42,43,3,26,13,0,43,68,1,0,0,0,44,45,3,6,3,0,45,
        46,3,14,7,0,46,47,3,16,8,0,47,48,3,18,9,0,48,49,3,20,10,0,49,50,
        3,22,11,0,50,51,3,26,13,0,51,68,1,0,0,0,52,53,3,6,3,0,53,54,3,14,
        7,0,54,55,3,16,8,0,55,56,3,26,13,0,56,68,1,0,0,0,57,58,3,6,3,0,58,
        59,3,14,7,0,59,60,3,18,9,0,60,61,3,26,13,0,61,68,1,0,0,0,62,63,3,
        6,3,0,63,64,3,12,6,0,64,65,3,26,13,0,65,68,1,0,0,0,66,68,3,26,13,
        0,67,38,1,0,0,0,67,44,1,0,0,0,67,52,1,0,0,0,67,57,1,0,0,0,67,62,
        1,0,0,0,67,66,1,0,0,0,68,5,1,0,0,0,69,70,5,1,0,0,70,71,5,14,0,0,
        71,7,1,0,0,0,72,73,5,14,0,0,73,74,5,14,0,0,74,75,5,14,0,0,75,9,1,
        0,0,0,76,77,5,2,0,0,77,11,1,0,0,0,78,82,5,3,0,0,79,80,5,4,0,0,80,
        82,5,16,0,0,81,78,1,0,0,0,81,79,1,0,0,0,82,13,1,0,0,0,83,84,7,0,
        0,0,84,15,1,0,0,0,85,86,5,8,0,0,86,87,3,24,12,0,87,17,1,0,0,0,88,
        89,5,9,0,0,89,90,3,24,12,0,90,19,1,0,0,0,91,92,5,10,0,0,92,93,3,
        24,12,0,93,21,1,0,0,0,94,95,5,11,0,0,95,96,3,24,12,0,96,23,1,0,0,
        0,97,98,5,14,0,0,98,25,1,0,0,0,99,100,7,1,0,0,100,27,1,0,0,0,3,31,
        67,81
    ]

class gcodeParser ( Parser ):

    grammarFileName = "gcode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'N'", "'M30'", "'M02'", "'M01'", "'G01'", 
                     "'G00'", "'G02'", "'X'", "'Y'", "'I'", "'J'", "'\\r\\n'", 
                     "'\\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "NUMBER", "WS", "STRING" ]

    RULE_def = 0
    RULE_fimprograma = 1
    RULE_statement = 2
    RULE_numerolinha = 3
    RULE_num3dig = 4
    RULE_mfim = 5
    RULE_mfunc = 6
    RULE_codfunc = 7
    RULE_coordx = 8
    RULE_coordy = 9
    RULE_coordi = 10
    RULE_coordj = 11
    RULE_coord = 12
    RULE_fimdelinha = 13

    ruleNames =  [ "def", "fimprograma", "statement", "numerolinha", "num3dig", 
                   "mfim", "mfunc", "codfunc", "coordx", "coordy", "coordi", 
                   "coordj", "coord", "fimdelinha" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    NUMBER=14
    WS=15
    STRING=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class DefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fimprograma(self):
            return self.getTypedRuleContext(gcodeParser.FimprogramaContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gcodeParser.StatementContext)
            else:
                return self.getTypedRuleContext(gcodeParser.StatementContext,i)


        def getRuleIndex(self):
            return gcodeParser.RULE_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDef" ):
                listener.enterDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDef" ):
                listener.exitDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDef" ):
                return visitor.visitDef(self)
            else:
                return visitor.visitChildren(self)




    def def_(self):

        localctx = gcodeParser.DefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 28
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 31 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 33
            self.fimprograma()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FimprogramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numerolinha(self):
            return self.getTypedRuleContext(gcodeParser.NumerolinhaContext,0)


        def mfim(self):
            return self.getTypedRuleContext(gcodeParser.MfimContext,0)


        def getRuleIndex(self):
            return gcodeParser.RULE_fimprograma

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFimprograma" ):
                listener.enterFimprograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFimprograma" ):
                listener.exitFimprograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFimprograma" ):
                return visitor.visitFimprograma(self)
            else:
                return visitor.visitChildren(self)




    def fimprograma(self):

        localctx = gcodeParser.FimprogramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_fimprograma)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.numerolinha()
            self.state = 36
            self.mfim()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numerolinha(self):
            return self.getTypedRuleContext(gcodeParser.NumerolinhaContext,0)


        def codfunc(self):
            return self.getTypedRuleContext(gcodeParser.CodfuncContext,0)


        def coordx(self):
            return self.getTypedRuleContext(gcodeParser.CoordxContext,0)


        def coordy(self):
            return self.getTypedRuleContext(gcodeParser.CoordyContext,0)


        def fimdelinha(self):
            return self.getTypedRuleContext(gcodeParser.FimdelinhaContext,0)


        def coordi(self):
            return self.getTypedRuleContext(gcodeParser.CoordiContext,0)


        def coordj(self):
            return self.getTypedRuleContext(gcodeParser.CoordjContext,0)


        def mfunc(self):
            return self.getTypedRuleContext(gcodeParser.MfuncContext,0)


        def getRuleIndex(self):
            return gcodeParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = gcodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 67
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.numerolinha()
                self.state = 39
                self.codfunc()
                self.state = 40
                self.coordx()
                self.state = 41
                self.coordy()
                self.state = 42
                self.fimdelinha()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.numerolinha()
                self.state = 45
                self.codfunc()
                self.state = 46
                self.coordx()
                self.state = 47
                self.coordy()
                self.state = 48
                self.coordi()
                self.state = 49
                self.coordj()
                self.state = 50
                self.fimdelinha()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 52
                self.numerolinha()
                self.state = 53
                self.codfunc()
                self.state = 54
                self.coordx()
                self.state = 55
                self.fimdelinha()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 57
                self.numerolinha()
                self.state = 58
                self.codfunc()
                self.state = 59
                self.coordy()
                self.state = 60
                self.fimdelinha()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 62
                self.numerolinha()
                self.state = 63
                self.mfunc()
                self.state = 64
                self.fimdelinha()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 66
                self.fimdelinha()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumerolinhaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(gcodeParser.NUMBER, 0)

        def getRuleIndex(self):
            return gcodeParser.RULE_numerolinha

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumerolinha" ):
                listener.enterNumerolinha(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumerolinha" ):
                listener.exitNumerolinha(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumerolinha" ):
                return visitor.visitNumerolinha(self)
            else:
                return visitor.visitChildren(self)




    def numerolinha(self):

        localctx = gcodeParser.NumerolinhaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_numerolinha)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(gcodeParser.T__0)
            self.state = 70
            self.match(gcodeParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Num3digContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(gcodeParser.NUMBER)
            else:
                return self.getToken(gcodeParser.NUMBER, i)

        def getRuleIndex(self):
            return gcodeParser.RULE_num3dig

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNum3dig" ):
                listener.enterNum3dig(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNum3dig" ):
                listener.exitNum3dig(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNum3dig" ):
                return visitor.visitNum3dig(self)
            else:
                return visitor.visitChildren(self)




    def num3dig(self):

        localctx = gcodeParser.Num3digContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_num3dig)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(gcodeParser.NUMBER)
            self.state = 73
            self.match(gcodeParser.NUMBER)
            self.state = 74
            self.match(gcodeParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MfimContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gcodeParser.RULE_mfim

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMfim" ):
                listener.enterMfim(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMfim" ):
                listener.exitMfim(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMfim" ):
                return visitor.visitMfim(self)
            else:
                return visitor.visitChildren(self)




    def mfim(self):

        localctx = gcodeParser.MfimContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_mfim)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(gcodeParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MfuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(gcodeParser.STRING, 0)

        def getRuleIndex(self):
            return gcodeParser.RULE_mfunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMfunc" ):
                listener.enterMfunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMfunc" ):
                listener.exitMfunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMfunc" ):
                return visitor.visitMfunc(self)
            else:
                return visitor.visitChildren(self)




    def mfunc(self):

        localctx = gcodeParser.MfuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_mfunc)
        try:
            self.state = 81
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.match(gcodeParser.T__2)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 79
                self.match(gcodeParser.T__3)
                self.state = 80
                self.match(gcodeParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CodfuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gcodeParser.RULE_codfunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCodfunc" ):
                listener.enterCodfunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCodfunc" ):
                listener.exitCodfunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCodfunc" ):
                return visitor.visitCodfunc(self)
            else:
                return visitor.visitChildren(self)




    def codfunc(self):

        localctx = gcodeParser.CodfuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_codfunc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 224) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CoordxContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def coord(self):
            return self.getTypedRuleContext(gcodeParser.CoordContext,0)


        def getRuleIndex(self):
            return gcodeParser.RULE_coordx

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCoordx" ):
                listener.enterCoordx(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCoordx" ):
                listener.exitCoordx(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCoordx" ):
                return visitor.visitCoordx(self)
            else:
                return visitor.visitChildren(self)




    def coordx(self):

        localctx = gcodeParser.CoordxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_coordx)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(gcodeParser.T__7)
            self.state = 86
            self.coord()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CoordyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def coord(self):
            return self.getTypedRuleContext(gcodeParser.CoordContext,0)


        def getRuleIndex(self):
            return gcodeParser.RULE_coordy

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCoordy" ):
                listener.enterCoordy(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCoordy" ):
                listener.exitCoordy(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCoordy" ):
                return visitor.visitCoordy(self)
            else:
                return visitor.visitChildren(self)




    def coordy(self):

        localctx = gcodeParser.CoordyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_coordy)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(gcodeParser.T__8)
            self.state = 89
            self.coord()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CoordiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def coord(self):
            return self.getTypedRuleContext(gcodeParser.CoordContext,0)


        def getRuleIndex(self):
            return gcodeParser.RULE_coordi

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCoordi" ):
                listener.enterCoordi(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCoordi" ):
                listener.exitCoordi(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCoordi" ):
                return visitor.visitCoordi(self)
            else:
                return visitor.visitChildren(self)




    def coordi(self):

        localctx = gcodeParser.CoordiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_coordi)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(gcodeParser.T__9)
            self.state = 92
            self.coord()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CoordjContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def coord(self):
            return self.getTypedRuleContext(gcodeParser.CoordContext,0)


        def getRuleIndex(self):
            return gcodeParser.RULE_coordj

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCoordj" ):
                listener.enterCoordj(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCoordj" ):
                listener.exitCoordj(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCoordj" ):
                return visitor.visitCoordj(self)
            else:
                return visitor.visitChildren(self)




    def coordj(self):

        localctx = gcodeParser.CoordjContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_coordj)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(gcodeParser.T__10)
            self.state = 95
            self.coord()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CoordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(gcodeParser.NUMBER, 0)

        def getRuleIndex(self):
            return gcodeParser.RULE_coord

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCoord" ):
                listener.enterCoord(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCoord" ):
                listener.exitCoord(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCoord" ):
                return visitor.visitCoord(self)
            else:
                return visitor.visitChildren(self)




    def coord(self):

        localctx = gcodeParser.CoordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_coord)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(gcodeParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FimdelinhaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gcodeParser.RULE_fimdelinha

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFimdelinha" ):
                listener.enterFimdelinha(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFimdelinha" ):
                listener.exitFimdelinha(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFimdelinha" ):
                return visitor.visitFimdelinha(self)
            else:
                return visitor.visitChildren(self)




    def fimdelinha(self):

        localctx = gcodeParser.FimdelinhaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_fimdelinha)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            _la = self._input.LA(1)
            if not(_la==12 or _la==13):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





