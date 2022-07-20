from DataSet import DataSet

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
        
        oitavas = [[self.grupoA[0].get_nome(), self.grupoB[1].get_nome()],
                   [self.grupoC[0].get_nome(), self.grupoD[1].get_nome()],
                   [self.grupoE[0].get_nome(), self.grupoF[1].get_nome()],
                   [self.grupoG[0].get_nome(), self.grupoH[1].get_nome()],
                   [self.grupoB[0].get_nome(), self.grupoA[1].get_nome()],
                   [self.grupoD[0].get_nome(), self.grupoC[1].get_nome()],
                   [self.grupoF[0].get_nome(), self.grupoE[1].get_nome()],
                   [self.grupoH[0].get_nome(), self.grupoG[1].get_nome()]]
        
        return oitavas
    
    def checando_jogos(self, jogos):
        for i in range(len(jogos)):
            for j in range(2):
                if jogos[i][j] == -1:
                    return False
        return True

if __name__ == '__main__':
    ff = FaseFinal()
    
    oitavas = ff.formando_oitavas()
    
    ds = DataSet()
    
    ds.salvando_oitavas(oitavas, [[2, 1], [2, 1], [2, 1], [2, 1], [2, 1], [2, 1], [2, 1], [2, 1]])
    
    aux = ds.recuperando_oitavas()

    for i in aux:
        print(i)