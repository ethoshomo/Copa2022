from DataSet import DataSet
import pandas as pd

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
        
        oitavas = {0:[self.grupoA[0].get_nome()],
                   1:[self.grupoB[1].get_nome()],
                   2:[self.grupoC[0].get_nome()], 
                   3:[self.grupoD[1].get_nome()],
                   4:[self.grupoE[0].get_nome()], 
                   5:[self.grupoF[1].get_nome()],
                   6:[self.grupoG[0].get_nome()], 
                   7:[self.grupoH[1].get_nome()],
                   8:[self.grupoB[0].get_nome()], 
                   9:[self.grupoA[1].get_nome()],
                   10:[self.grupoD[0].get_nome()], 
                   11:[self.grupoC[1].get_nome()],
                   12:[self.grupoF[0].get_nome()], 
                   13:[self.grupoE[1].get_nome()],
                   14:[self.grupoH[0].get_nome()], 
                   15:[self.grupoG[1].get_nome()]}
        
        df_oitavas = pd.DataFrame(oitavas, index=[0, 1])

        df_oitavas.to_pickle('dataset/Oitavas.pkl')    
        
        ds = DataSet()
        ds.salvando_oitavas([[-1, -1], [-1, -1], [-1, -1], [-1, -1], 
                             [-1, -1], [-1, -1], [-1, -1], [-1, -1]])
           
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
    aux = ds.recuperando_oitavas()
    
    for i in aux:
        print(i)