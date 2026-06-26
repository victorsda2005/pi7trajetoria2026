import math
import numpy as np


class GeradorTrajetoria:

    def __init__(self):

        self.x_atual = 0
        self.y_atual = 0

        self.tabela = []

    ###########################################################
    ## Polinômio de quinta ordem
    ###########################################################

    def quintico(self, tf, n):

        t = np.linspace(0, tf, n)

        A = np.array([
            [tf**5, tf**4, tf**3],
            [5*tf**4, 4*tf**3, 3*tf**2],
            [20*tf**3, 12*tf**2, 6*tf]
        ])

        b = np.array([1,0,0])

        a5,a4,a3 = np.linalg.solve(A,b)

        tau = a5*t**5 + a4*t**4 + a3*t**3

        return tau

    ###########################################################
    ## Reta
    ###########################################################

    def reta(self, x_final, y_final,
             tf=14,
             n=25):

        x0 = self.x_atual
        y0 = self.y_atual

        tau = self.quintico(tf,n)

        for s in tau:

            x = x0 + (x_final-x0)*s
            y = y0 + (y_final-y0)*s

            self.tabela.append((x,y))

        self.x_atual = x_final
        self.y_atual = y_final

    ###########################################################
    ## Arco horário (G02)
    ###########################################################

    def arco(self,
             x_final,
             y_final,
             i,
             j,
             tf=7,
             n=25):

        x0 = self.x_atual
        y0 = self.y_atual

        cx = x0 + i
        cy = y0 + j

        raio = math.sqrt((x0-cx)**2 + (y0-cy)**2)

        theta0 = math.atan2(y0-cy,
                            x0-cx)

        theta1 = math.atan2(y_final-cy,
                            x_final-cx)

        # Movimento horário
        while theta1 > theta0:
            theta1 -= 2*math.pi

        tau = self.quintico(tf,n)

        for s in tau:

            theta = theta0 + (theta1-theta0)*s

            x = cx + raio*math.cos(theta)
            y = cy + raio*math.sin(theta)

            self.tabela.append((x,y))

        self.x_atual = x_final
        self.y_atual = y_final

    ###########################################################

    def gerar(self, movimentos):

        for mov in movimentos:

            # Mantém a coordenada anterior caso X ou Y não sejam informados
            x = mov["x"] if mov["x"] is not None else self.x_atual
            y = mov["y"] if mov["y"] is not None else self.y_atual

            if mov["g"] == "G00":

                self.x_atual = x
                self.y_atual = y

                self.tabela.append((x, y))

            elif mov["g"] == "G01":

                self.reta(
                    x,
                    y
                )

            elif mov["g"] == "G02":

                self.arco(
                    x,
                    y,
                    mov["i"],
                    mov["j"]
                )

        return self.tabela