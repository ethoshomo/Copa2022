from cmath import pi
from itertools import repeat
from numpy import column_stack
from Selecao import Selecao
import pandas as pd


class Grupo():
    def __init__(self) -> None:
        self.grupos = [[] for i in range(8)]

    def formando_grupos(self):
        selecoes = pd.read_csv('selecoes.csv', header=None)

        linhas = selecoes.shape[0]
        colunas = selecoes.shape[1]

        for i in range(linhas):
            for j in range(colunas):
                self.grupos[i].append(Selecao(selecoes[j][i]))


if __name__ == "__main__":
    a = Grupo()
    a.formando_grupos()
