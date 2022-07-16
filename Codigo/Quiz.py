"""
UNIVERSIDADE DE SÃO PAULO (USP)
PROJETO FINAL DA DISCIPLINA DE PROGRAMAÇÃO ORIENTADA A OBJETOS (POO)
TEMÁTICA: COPA DO MUNDO DE 2022
PROGRAMA DESENVOLVIDO: SHOW DE BOLA!!!
DOCENTE: MÁRCIO DELAMARO
DISCENTES:
    CARLOS FILIPE DE CASTRO LEMOS (12542630)
    JOÃO GABRIEL SASSERON ROBERTO AMORIN (12542564)
    PEDRO HENRIQUE VILELA DO NASCIMENTO (12803492)
    PEDRO GUILHERME DOS REIS TEIXEIRA (12542477)
"""
import random
import pandas as pd
from Pergunta import Pergunta

class Quiz():
    def __init__(self):
        df_perguntas = pd.read_pickle('dataset/Perguntas.pkl')

        colunas = df_perguntas.shape[1]

        self.perguntas = []

        for i in range(colunas):
            self.perguntas.append(Pergunta(df_perguntas[i]))

        random.shuffle(self.perguntas)

        self.pontuacao = 0

    def proxima_pergunta(self):
        return self.perguntas.pop(0)

    def teste(self):
        for i in range(8):
            i = self.proxima_pergunta()
            print(i)

if __name__ == '__main__':
    q = Quiz()
    q.teste()
