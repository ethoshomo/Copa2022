from Selecao import Selecao
import pandas as pd

class Grupo():
    def __init__(self, grupo: str):
        df_selecoes   = pd.read_pickle('dataset/Selecoes.plk')
        self.selecao1 = Selecao(df_selecoes[grupo][0])
        self.selecao2 = Selecao(df_selecoes[grupo][1])
        self.selecao3 = Selecao(df_selecoes[grupo][2])
        self.selecao4 = Selecao(df_selecoes[grupo][3])
        self.selecao1.set_colocacao(2)
        self.selecao2.set_colocacao(3)
        self.selecao3.set_colocacao(4)
        self.selecao4.set_colocacao(5)

    def teste(self):
        print(self.selecao1)
        print(self.selecao2)
        print(self.selecao3)
        print(self.selecao4)
        print()
        
    def organizando_grupos(self):
        lista_grupos = [self.selecao1, self.selecao2, self.selecao3, self.selecao4]
        
        lista_grupos.sort(key=lambda x: x.saldo_de_gols, reverse=True)
        lista_grupos.sort(key=lambda x: x.pontos       , reverse=True)
        
        self.selecao1.set_colocacao(lista_grupos.index(self.selecao1)+2)
        self.selecao2.set_colocacao(lista_grupos.index(self.selecao2)+2)
        self.selecao3.set_colocacao(lista_grupos.index(self.selecao3)+2)
        self.selecao4.set_colocacao(lista_grupos.index(self.selecao4)+2)

            
if __name__ == "__main__":
    gA = Grupo('GrupoA')
    
    gA.teste()
    gA.selecao1.att_jogo(2,1)
    gA.teste()
    
    
    # gB = Grupo('GrupoB')
    # gB.teste()
    
    # gB = Grupo('GrupoC')
    # gB.teste()
    
    # gC = Grupo('GrupoD')
    # gC.teste()
    
    # gC = Grupo('GrupoE')
    # gC.teste()