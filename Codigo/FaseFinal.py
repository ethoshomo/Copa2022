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
        
        times = [['-'] for i in range(8)]
        
        for i in range(0, 16, 2):
            if oitavas[i][0] != '-' and oitavas[i+1][0] != '-':
                
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
        
        times = [['-'] for i in range(4)]
        
        for i in range(0, 8, 2):
            if quartas[i][0] != '-' and quartas[i+1][0] != '-':
                
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
        semis = self.ds.recuperando_semifinais()
        
        times = [['-'] for i in range(4)]
        
        for i in range(0, 4, 2):
            if semis[i][0] != '-' and semis[i+1][0] != '-':
                
                if semis[i][2] > semis[i+1][2]:
                    times[int(i/2)] = semis[i][0]
                    times[int(i/2)+2] = semis[i+1][0]
                    
                    
                elif semis[i][2] < semis[i+1][2]:
                    times[int(i/2)] = semis[i+1][0]
                    times[int(i/2)+1] = semis[i][0]
                    
                elif semis[i][3] != -1 and semis[i+1][3] != -1:
                    if semis[i][3] > semis[i+1][3]:
                        times[int(i/2)] = semis[i][0]
                        times[int(i/2)+2] = semis[i+1][0]
                    else:
                        times[int(i/2)] = semis[i+1][0]
                        times[int(i/2)+2] = semis[i][0]
       
        if self.checando_finais(times) == True:
            return
        
        semis = {0:times[0],
                   1:times[1],
                   2:times[2],
                   3:times[3]}
        
        df_semis = pd.DataFrame(semis, index=[0])
        
        df_semis.to_pickle('dataset/Finais.pkl')
        
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
    ds = DataSet()
    
    ff.formando_oitavas()
    # ds.salvando_oitavas([[7, 7, 1, 0], [3, 1, 0, 1], [3, 1, 0, 1], [3, 1, 0, 1],
                        # [3, 1, 0, 1], [3, 1, 0, 1], [3, 1, 0, 1], [3, 1, 0, 1]])
    oitavas = ds.recuperando_oitavas()
    for i in oitavas:
        print(i)
    print('\n')
    
    ff.formando_quartas()
    # ds.salvando_quartas([[3, 1, 0, 1], [3, 1, 0, 1],
                        # [3, 1, 0, 1], [3, 1, 0, 1]])
    quartas = ds.recuperando_quartas()
    for i in quartas:
        print(i)
    print('\n')
    
    ff.formando_semifinais()
    # ds.salvando_semifinais([[3, 1, 1, 0], [3, 1, 1, 0]])
    semifinais = ds.recuperando_semifinais()
    for i in semifinais:
        print(i)
    print('\n')
        
    ff.formando_finais()
    # ds.salvando_finais([[3, 1, 1, 0], [3, 1, 1, 0]])
    finais = ds.recuperando_finais()
    for i in finais:
        print(i)
    print('\n\n')
    
    teste = ds.recuperando_quartassemis()
    for i in teste:
        print(i)
