import pandas as pd

from Grupo import Grupo

class DataSet():
    def __init__(self):
        self.df_selecoes = pd.read_pickle('dataset/Selecoes.plk')
    
    def salvando_grupo(self, grupo :str, jogos: list):
        nome_grupo = grupo.replace(' ', '')
        
        df_jogos = self.criando_DataFrame(nome_grupo)

        # Quantos gols a seleção df_selecoes[grupo][1] fez em df_selecoes[grupo][0] e vice-versa 
        # JOGO 1
        df_jogos[self.df_selecoes[nome_grupo][1]][self.df_selecoes[nome_grupo][0]] = jogos[0][0]
        df_jogos[self.df_selecoes[nome_grupo][0]][self.df_selecoes[nome_grupo][1]] = jogos[0][1]
        
        # JOGO 2
        df_jogos[self.df_selecoes[nome_grupo][3]][self.df_selecoes[nome_grupo][2]] = jogos[1][0]
        df_jogos[self.df_selecoes[nome_grupo][2]][self.df_selecoes[nome_grupo][3]] = jogos[1][1]
        
        # JOGO 3
        df_jogos[self.df_selecoes[nome_grupo][2]][self.df_selecoes[nome_grupo][0]] = jogos[2][0]
        df_jogos[self.df_selecoes[nome_grupo][0]][self.df_selecoes[nome_grupo][2]] = jogos[2][1]
        
        # JOGO 4
        df_jogos[self.df_selecoes[nome_grupo][1]][self.df_selecoes[nome_grupo][3]] = jogos[3][0]
        df_jogos[self.df_selecoes[nome_grupo][3]][self.df_selecoes[nome_grupo][1]] = jogos[3][1]
        
        # JOGO 5
        df_jogos[self.df_selecoes[nome_grupo][0]][self.df_selecoes[nome_grupo][3]] = jogos[4][0]
        df_jogos[self.df_selecoes[nome_grupo][3]][self.df_selecoes[nome_grupo][0]] = jogos[4][1]
        
        # JOGO 6
        df_jogos[self.df_selecoes[nome_grupo][2]][self.df_selecoes[nome_grupo][1]] = jogos[5][0]
        df_jogos[self.df_selecoes[nome_grupo][1]][self.df_selecoes[nome_grupo][2]] = jogos[5][1]
        
        nome = 'dataset/' + nome_grupo + '.pkl'
        
        df_jogos.to_pickle(nome)
    
    def recuperando_jogos(self, grupo: str):
        nome_grupo = grupo.replace(' ', '')
        
        jogos = [['-','-'] for i in range(6)]
        nome = 'dataset/' + nome_grupo + '.pkl'
        df_jogos = pd.read_pickle(nome)
        
        # Faz o caminho inverso e recupera os dados dos jogos
        # JOGO 1
        jogos[0][0] = df_jogos[self.df_selecoes[nome_grupo][1]][self.df_selecoes[nome_grupo][0]] 
        jogos[0][1] = df_jogos[self.df_selecoes[nome_grupo][0]][self.df_selecoes[nome_grupo][1]] 
        
        # JOGO 2
        jogos[1][0] = df_jogos[self.df_selecoes[nome_grupo][3]][self.df_selecoes[nome_grupo][2]] 
        jogos[1][1] = df_jogos[self.df_selecoes[nome_grupo][2]][self.df_selecoes[nome_grupo][3]] 
    
        # JOGO 3
        jogos[2][0] = df_jogos[self.df_selecoes[nome_grupo][2]][self.df_selecoes[nome_grupo][0]] 
        jogos[2][1] = df_jogos[self.df_selecoes[nome_grupo][0]][self.df_selecoes[nome_grupo][2]] 
        
        # JOGO 4
        jogos[3][0] = df_jogos[self.df_selecoes[nome_grupo][1]][self.df_selecoes[nome_grupo][3]] 
        jogos[3][1] = df_jogos[self.df_selecoes[nome_grupo][3]][self.df_selecoes[nome_grupo][1]] 
        
        # JOGO 5
        jogos[4][0] = df_jogos[self.df_selecoes[nome_grupo][0]][self.df_selecoes[nome_grupo][3]] 
        jogos[4][1] = df_jogos[self.df_selecoes[nome_grupo][3]][self.df_selecoes[nome_grupo][0]] 
        
        # JOGO 6
        jogos[5][0] = df_jogos[self.df_selecoes[nome_grupo][2]][self.df_selecoes[nome_grupo][1]] 
        jogos[5][1] = df_jogos[self.df_selecoes[nome_grupo][1]][self.df_selecoes[nome_grupo][2]] 
    
        return jogos

#    Grupo A         Grupo B         Grupo C    Grupo D     Grupo E   Grupo F   Grupo G        Grupo H
# 1    Catar      Inglaterra       Argentina     França     Espanha   Bélgica    Brasil       Portugal
# 2  Equador             Irã  Arábia Saudita  Austrália  Costa Rica    Canadá    Sérvia           Gana
# 3  Senegal  Estados Unidos          México  Dinamarca    Alemanha  Marrocos     Suíça        Uruguai
# 4  Holanda   País de Gales         Polônia    Tunísia       Japão   Croácia  Camarões  Coreia do Sul

# JOGOS:
# 0 -> 1x2
# 1 -> 3x4
# 2 -> 1x3
# 3 -> 4x2
# 4 -> 4x1
# 5 -> 2x3

# JOGOS:                            PONTOS:
# 0 -> 1x2  Catar   0 x 1 Equador   Catar   -> 0 + 3 + 0 = 3
# 1 -> 3x4  Senegal 1 x 1 Holanda   Equador -> 3 + 0 + 0 = 3
# 2 -> 1x3  Catar   2 x 1 Senegal   Senegal -> 1 + 0 + 3 = 4
# 3 -> 4x2  Holanda 3 x 2 Equador   Holanda -> 1 + 3 + 3 = 7
# 4 -> 4x1  Holanda 5 x 4 Catar
# 5 -> 2x3  Equador 4 x 5 Senegal
    
    def recuperando_grupos(self, grupo: str):
        nome_grupo = grupo.replace(' ', '')
        
        jogos = self.recuperando_jogos(nome_grupo)
        
        grupo = Grupo(nome_grupo)
        
        # SELEÇÃO 1
        if -1 not in jogos[0]:
            grupo.selecao1.att_jogo(jogos[0][0], jogos[0][1])
            grupo.selecao2.att_jogo(jogos[0][1], jogos[0][0])
        
        if -1 not in jogos[1]:
            grupo.selecao3.att_jogo(jogos[1][0], jogos[1][1])
            grupo.selecao4.att_jogo(jogos[1][1], jogos[1][0])
        
        if -1 not in jogos[2]:
            grupo.selecao1.att_jogo(jogos[2][0], jogos[2][1])
            grupo.selecao3.att_jogo(jogos[2][1], jogos[2][0])  
        
        if -1 not in jogos[3]:
            grupo.selecao2.att_jogo(jogos[3][1], jogos[3][0])  
            grupo.selecao4.att_jogo(jogos[3][0], jogos[3][1])  
        
        if -1 not in jogos[4]:
            grupo.selecao1.att_jogo(jogos[4][1], jogos[4][0])
            grupo.selecao4.att_jogo(jogos[4][0], jogos[4][1])  
        
        if -1 not in jogos[5]:
            grupo.selecao2.att_jogo(jogos[5][0], jogos[5][1])
            grupo.selecao3.att_jogo(jogos[5][1], jogos[5][0])
        
        grupo.teste()
        
        grupo.organizando_grupos()
        
        grupo.teste()
        
        return grupo
        
    def criando_DataFrame(self, grupo: str):
        nome_grupo = grupo.replace(' ', '')
        
        inicio = [-1 for i in range(4)]
        
        data = {self.df_selecoes[nome_grupo][0]:inicio,
                self.df_selecoes[nome_grupo][1]:inicio,
                self.df_selecoes[nome_grupo][2]:inicio,
                self.df_selecoes[nome_grupo][3]:inicio,}
        
        df_padrao = pd.DataFrame(data, index=self.df_selecoes[nome_grupo])
        
        return df_padrao
    
if __name__ == '__main__':
    ds = DataSet()
    a_jogos = [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]
    ds.salvando_grupo('Grupo A', a_jogos)
    d_jogos = ds.recuperando_jogos('Grupo A')
    g = ds.recuperando_grupos('Grupo A')
    g.teste()
    print('Antes:  ', end='')
    print(a_jogos)
    print('Depois: ', end='')
    print(d_jogos)
    print()
    