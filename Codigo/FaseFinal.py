import re
from time import time
from turtle import Turtle

from matplotlib.contour import QuadContourSet
from DataSet import DataSet
import pandas as pd
import os

class FaseFinal():
    def __init__(self):
        
        self.ds = DataSet()
        self.grupoA = self.ds.recuperando_grupos_lista('Grupo A')
        self.grupoB = self.ds.recuperando_grupos_lista('Grupo B')
        self.grupoC = self.ds.recuperando_grupos_lista('Grupo C')
        self.grupoD = self.ds.recuperando_grupos_lista('Grupo D')
        self.grupoE = self.ds.recuperando_grupos_lista('Grupo E')
        self.grupoF = self.ds.recuperando_grupos_lista('Grupo F')
        self.grupoG = self.ds.recuperando_grupos_lista('Grupo G')
        self.grupoH = self.ds.recuperando_grupos_lista('Grupo H')
        self.jogosA = self.ds.recuperando_jogos('Grupo A')
        self.jogosB = self.ds.recuperando_jogos('Grupo B')
        self.jogosC = self.ds.recuperando_jogos('Grupo C')
        self.jogosD = self.ds.recuperando_jogos('Grupo D')
        self.jogosE = self.ds.recuperando_jogos('Grupo E')
        self.jogosF = self.ds.recuperando_jogos('Grupo F')
        self.jogosG = self.ds.recuperando_jogos('Grupo G')
        self.jogosH = self.ds.recuperando_jogos('Grupo H')
    
    def formando_oitavas(self):
        
        if self.checando_jogos((self.jogosA)) == False:
            self.grupoA[0].set_nome('-')
            self.grupoA[1].set_nome('-')
        
        if self.checando_jogos(self.jogosB) == False:
            self.grupoB[0].set_nome('-')
            self.grupoB[1].set_nome('-')

        if self.checando_jogos(self.jogosC) == False:
            self.grupoC[0].set_nome('-')
            self.grupoC[1].set_nome('-')
        
        if self.checando_jogos(self.jogosD) == False:
            self.grupoD[0].set_nome('-')
            self.grupoD[1].set_nome('-')
        
        if self.checando_jogos(self.jogosE) == False:
            self.grupoE[0].set_nome('-')
            self.grupoE[1].set_nome('-')
        
        if self.checando_jogos(self.jogosF) == False:
            self.grupoF[0].set_nome('-')
            self.grupoF[1].set_nome('-')
            
        if self.checando_jogos(self.jogosG) == False:
            self.grupoG[0].set_nome('-')
            self.grupoG[1].set_nome('-')
        
        if self.checando_jogos(self.jogosH) == False:
            self.grupoH[0].set_nome('-')
            self.grupoH[1].set_nome('-')
        
        times = [self.grupoA[0].get_nome(),
                 self.grupoB[1].get_nome(),
                 self.grupoC[0].get_nome(),
                 self.grupoD[1].get_nome(),
                 self.grupoE[0].get_nome(),
                 self.grupoF[1].get_nome(),
                 self.grupoG[0].get_nome(),
                 self.grupoH[1].get_nome(),
                 self.grupoB[0].get_nome(),
                 self.grupoA[1].get_nome(),
                 self.grupoD[0].get_nome(),
                 self.grupoC[1].get_nome(),
                 self.grupoF[0].get_nome(),
                 self.grupoE[1].get_nome(),
                 self.grupoH[0].get_nome(),
                 self.grupoG[1].get_nome()]
        
        if self.checando_oitavas(times) == True:
            return
        
        oitavas = {0: times[0],
                   1: times[1],
                   2: times[2], 
                   3: times[3],
                   4: times[4], 
                   5: times[5],
                   6: times[6], 
                   7: times[7],
                   8: times[8], 
                   9: times[9],
                   10:times[10], 
                   11:times[11],
                   12:times[12], 
                   13:times[13],
                   14:times[14], 
                   15:times[15]}
        
        df_oitavas = pd.DataFrame(oitavas, index=[0])

        df_oitavas.to_pickle('dataset/Oitavas.pkl')    
        
        self.ds.salvando_oitavas([[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], 
                                  [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]])
    
    def checando_oitavas(self, novos: list):
        if os.path.exists('dataset/Oitavas.pkl'):
            # Leitura dos times antigos
            antigos = pd.read_pickle('dataset/Oitavas.pkl')

            # Comparação
            for i in range(16):
                if antigos[i][0] != novos[i]:
                    return False
            return True
        return False
    
    def checando_jogos(self, jogos):
        for i in range(len(jogos)):
            for j in range(2):
                if jogos[i][j] == -1:
                    return False
        return True

    def formando_quartas(self):
        oitavas = self.ds.recuperando_oitavas()
        df_ff   = pd.read_pickle('dataset/FaseFinalJogos.pkl')
        
        times = [['-'] for i in range(8)]
        
        for i in range(0, 16, 2):
            if oitavas[i][0] != '-' and oitavas[i+1][0] != '-' and df_ff[oitavas[i][0]][oitavas[i+1][0]] != -1 and df_ff[oitavas[i+1][0]][oitavas[i][0]] != -1:
                
                if oitavas[i][2] > oitavas[i+1][2]:
                    times[int(i/2)] = oitavas[i][0]
                    
                elif oitavas[i][2] < oitavas[i+1][2]:
                    times[int(i/2)] = oitavas[i+1][0]
                    
                elif oitavas[i][3] != -1 and oitavas[i+1][3] != -1:
                    if oitavas[i][3] > oitavas[i+1][3]:
                        times[int(i/2)] = oitavas[i][0]
                    else:
                        times[int(i/2)] = oitavas[i+1][0]
        
        if self.checando_quartas(times) == True:
            return
        
        quartas = {0:times[0],
                   1:times[1],
                   2:times[2],
                   3:times[3],
                   4:times[4],
                   5:times[5],
                   6:times[6],
                   7:times[7]}
        
        df_quartas = pd.DataFrame(quartas, index=[0])
        
        df_quartas.to_pickle('dataset/Quartas.pkl')
        
        self.ds.salvando_quartas([[-1, -1, -1, -1], [-1, -1, -1, -1],
                                  [-1, -1, -1, -1], [-1, -1, -1, -1]])
        
    def checando_quartas(self, novos):
        if os.path.exists('dataset/Quartas.pkl'):
            antigos = pd.read_pickle('dataset/Quartas.pkl')
            
            for i in range(8):
                if antigos[i][0] != novos[i]:
                    return False
            return True
        return False
    
    def formando_semifinais(self):
        quartas = self.ds.recuperando_quartas()
        df_ff   = pd.read_pickle('dataset/FaseFinalJogos.pkl')
        
        times = [['-'] for i in range(4)]
        
        for i in range(0, 8, 2):
            if quartas[i][0] != '-' and quartas[i+1][0] != '-' and df_ff[quartas[i][0]][quartas[i+1][0]] != -1 and df_ff[quartas[i+1][0]][quartas[i][0]] != -1:
                
                if quartas[i][2] > quartas[i+1][2]:
                    times[int(i/2)] = quartas[i][0]
                    
                elif quartas[i][2] < quartas[i+1][2]:
                    times[int(i/2)] = quartas[i+1][0]
                    
                elif quartas[i][3] != -1 and quartas[i+1][3] != -1:
                    if quartas[i][3] > quartas[i+1][3]:
                        times[int(i/2)] = quartas[i][0]
                    else:
                        times[int(i/2)] = quartas[i+1][0]
        
        if self.checando_semifinais(times) == True:
            return
        
        semis = {0:times[0],
                 1:times[1],
                 2:times[2],
                 3:times[3]}
        
        df_quartas = pd.DataFrame(semis, index=[0])
        
        df_quartas.to_pickle('dataset/Semifinais.pkl')
        
        self.ds.salvando_semifinais([[-1, -1, -1, -1], [-1, -1, -1, -1],
                                  [-1, -1, -1, -1], [-1, -1, -1, -1]])

    def checando_semifinais(self, novos):
        if os.path.exists('dataset/Semifinais.pkl'):
            antigos = pd.read_pickle('dataset/Semifinais.pkl')
            
            for i in range(4):
                if antigos[i][0] != novos[i]:
                    return False
            return True
        return False

    def formando_finais(self):
        finais = self.ds.recuperando_semifinais()
        df_ff = pd.read_pickle('dataset/FaseFinalJogos.pkl')
        
        times = [['-'] for i in range(4)]
        
        for i in range(0, 4, 2):
            if finais[i][0] != '-' and finais[i+1][0] != '-' and df_ff[finais[i][0]][finais[i+1][0]] != -1 and df_ff[finais[i+1][0]][finais[i][0]] != -1:
                
                if finais[i][2] > finais[i+1][2]:
                    times[int(i/2)] = finais[i][0]
                    times[int(i/2)+2] = finais[i+1][0]
                    
                elif finais[i][2] < finais[i+1][2]:
                    times[int(i/2)] = finais[i+1][0]
                    times[int(i/2)+2] = finais[i][0]
                    
                elif finais[i][3] != -1 and finais[i+1][3] != -1:
                    if finais[i][3] > finais[i+1][3]:
                        times[int(i/2)] = finais[i][0]
                        times[int(i/2)+2] = finais[i+1][0]
                    else:
                        times[int(i/2)] = finais[i+1][0]
                        times[int(i/2)+2] = finais[i][0]
        
        if self.checando_finais(times) == True:
            return
        
        finais = {0:times[0],
                 1:times[1],
                 2:times[2],
                 3:times[3]}
        
        df_finais = pd.DataFrame(finais, index=[0])
        
        df_finais.to_pickle('dataset/Finais.pkl')
        
        self.ds.salvando_finais([[-1, -1, -1, -1], [-1, -1, -1, -1],
                                  [-1, -1, -1, -1], [-1, -1, -1, -1]])
        
    def checando_finais(self, novos):
        if os.path.exists('dataset/Finais.pkl'):
            antigos = pd.read_pickle('dataset/Finais.pkl')
            
            for i in range(4):
                if antigos[i][0] != novos[i]:
                    return False
            return True
        return False
    
if __name__ == '__main__':
    ff = FaseFinal()
    ff.formando_quartas()
    
    ds = DataSet()
    ds.salvando_semifinais([[100, 1, 1, 0], [2, 1, 1, 0]])
    
    ff.formando_finais()