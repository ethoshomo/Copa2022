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
    
    def verifica_respota(self, resposta: str, perg: Pergunta):
        if resposta == perg.get_gabarito():
            self.perguntas += 10
            
    def teste(self):
        for i in range(8):
            i = self.proxima_pergunta()
            print(i)
        
if __name__ == '__main__':
    q = Quiz()
    q.teste()