from gcodeParser import gcodeParser
from gcodeVisitor import gcodeVisitor as BaseVisitor

class GcodeCoordVisitor(BaseVisitor):

    def __init__(self):
        self.coordenadas = []

        self._current_g = None
        self._current_x = None
        self._current_y = None
        self._current_i = None
        self._current_j = None

    def visitStatement(self, ctx: gcodeParser.StatementContext):
        self._current_g = None
        self._current_x = None
        self._current_y = None
        self._current_i = None
        self._current_j = None

        # visita os filhos para preencher _current_x e _current_y
        self.visitChildren(ctx)

        # só registra se tiver pelo menos X ou Y
        if self._current_x is not None or self._current_y is not None:
            self.coordenadas.append({
                "g": self._current_g,
                "x": self._current_x,
                "y": self._current_y,
                "i": self._current_i,
                "j": self._current_j,
            })

    def visitCodfunc(self, ctx):
        self._current_g = ctx.getText()

    def visitCoordx(self, ctx: gcodeParser.CoordxContext):
        self._current_x = self._parse_coord(ctx.coord())

    def visitCoordy(self, ctx: gcodeParser.CoordyContext):
        self._current_y = self._parse_coord(ctx.coord())

    def visitCoordi(self, ctx):
        self._current_i = self._parse_coord(ctx.coord())

    def visitCoordj(self, ctx):
        self._current_j = self._parse_coord(ctx.coord())

    def _parse_coord(self, coord_ctx: gcodeParser.CoordContext) -> int:
        # cada INT é um dígito; concatena e converte
        return int(coord_ctx.NUMBER().getText())

