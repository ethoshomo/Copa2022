from DataSet import DataSet
import pandas as pd
import os

class FaseFinal():
    def __init__(self):
        
        ds = DataSet()
        self.grupoA = ds.recuperando_grupos_lista('Grupo A')
        self.grupoB = ds.recuperando_grupos_lista('Grupo B')
        self.grupoC = ds.recuperando_grupos_lista('Grupo C')
        self.grupoD = ds.recuperando_grupos_lista('Grupo D')
        self.grupoE = ds.recuperando_grupos_lista('Grupo E')
        self.grupoF = ds.recuperando_grupos_lista('Grupo F')
        self.grupoG = ds.recuperando_grupos_lista('Grupo G')
        self.grupoH = ds.recuperando_grupos_lista('Grupo H')
        self.jogosA = ds.recuperando_jogos('Grupo A')
        self.jogosB = ds.recuperando_jogos('Grupo B')
        self.jogosC = ds.recuperando_jogos('Grupo C')
        self.jogosD = ds.recuperando_jogos('Grupo D')
        self.jogosE = ds.recuperando_jogos('Grupo E')
        self.jogosF = ds.recuperando_jogos('Grupo F')
        self.jogosG = ds.recuperando_jogos('Grupo G')
        self.jogosH = ds.recuperando_jogos('Grupo H')
    
    def checando_oitavas(self, novos: list):
        if os.path.exists('dataset/Oitavas.pkl'):
            # Leitura dos times antigos
            oitavas = pd.read_pickle('dataset/Oitavas.pkl')
            antigos = []
            for i in range(16):
                antigos.append(oitavas[i][0])

            # Comparação
            for i in range(16):
                if antigos[i] != novos[i]:
                    return False
            
            return True
            
        return False
    
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
        
        df_oitavas = pd.DataFrame(oitavas, index=[0, 1])

        df_oitavas.to_pickle('dataset/Oitavas.pkl')    
        
        ds = DataSet()
        ds.salvando_oitavas([[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], 
                             [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]])
           
    def checando_jogos(self, jogos):
        for i in range(len(jogos)):
            for j in range(2):
                if jogos[i][j] == -1:
                    return False
        return True

if __name__ == '__main__':
    ff = FaseFinal()
    ff.formando_oitavas()
    
    ds = DataSet()
    ds.salvando_oitavas([[1, 1, 1, 0], [1, 1, 1, 0] ,[1, 1, 1, 0], [1, 1, 1, 0],
                        [1, 1, 1, 0], [1, 1, 1, 0], [1, 1, 1, 0], [1, 1, 1, 0]])
    aux = ds.recuperando_oitavas()
    aux1 = ds.recuperando_oitavas_str()
    for i in aux:
        print(i)
        
    print()
    
    for i in aux1:
        print(i)