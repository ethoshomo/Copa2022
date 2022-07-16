import pandas as pd
import os
from Grupo import Grupo

class DataSet():
    def __init__(self):
        self.df_selecoes = pd.read_pickle('dataset/Selecoes.plk')

    def salvando_grupo(self, grupo :str, jogos: list):
        # Caso o nome venha com ' '
        nome_grupo = grupo.replace(' ', '')

        df_jogos = self.criando_DataFrame(nome_grupo)

        # Quantos gols a seleção df_selecoes[grupo][1] fez em df_selecoes[grupo][0] e vice-versa
        # JOGO 1
        df_jogos.loc[self.df_selecoes[nome_grupo][1]][self.df_selecoes[nome_grupo][0]] = jogos[0][1]
        df_jogos.loc[self.df_selecoes[nome_grupo][0]][self.df_selecoes[nome_grupo][1]] = jogos[0][0]

        # JOGO 2
        df_jogos.loc[self.df_selecoes[nome_grupo][3]][self.df_selecoes[nome_grupo][2]] = jogos[1][1]
        df_jogos.loc[self.df_selecoes[nome_grupo][2]][self.df_selecoes[nome_grupo][3]] = jogos[1][0]

        # JOGO 3
        df_jogos.loc[self.df_selecoes[nome_grupo][2]][self.df_selecoes[nome_grupo][0]] = jogos[2][1]
        df_jogos.loc[self.df_selecoes[nome_grupo][0]][self.df_selecoes[nome_grupo][2]] = jogos[2][0]

        # JOGO 4
        df_jogos.loc[self.df_selecoes[nome_grupo][1]][self.df_selecoes[nome_grupo][3]] = jogos[3][1]
        df_jogos.loc[self.df_selecoes[nome_grupo][3]][self.df_selecoes[nome_grupo][1]] = jogos[3][0]

        # JOGO 5
        df_jogos.loc[self.df_selecoes[nome_grupo][0]][self.df_selecoes[nome_grupo][3]] = jogos[4][1]
        df_jogos.loc[self.df_selecoes[nome_grupo][3]][self.df_selecoes[nome_grupo][0]] = jogos[4][0]

        # JOGO 6
        df_jogos.loc[self.df_selecoes[nome_grupo][2]][self.df_selecoes[nome_grupo][1]] = jogos[5][1]
        df_jogos.loc[self.df_selecoes[nome_grupo][1]][self.df_selecoes[nome_grupo][2]] = jogos[5][0]

        nome = 'dataset/' + nome_grupo + '.pkl'

        df_jogos.to_pickle(nome)

    def recuperando_jogos(self, grupo: str):
        nome_grupo = grupo.replace(' ', '')

        # Se o arquivo do jogo ainda não existe, cria
        self.cria_arq(grupo)

        # Inicia os jogos e faz a leitura do arquivo
        jogos = [[-1, -1] for i in range(6)]
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
    
    def recuperando_jogos_str(self, grupo: str):
        # transforma os dados recebidos em int para str
        jogos_int = self.recuperando_jogos(grupo)

        # Caso o usuário não preencheu o placar
        jogos_str = [['',''] for i in range(6)]

        for i in range(len(jogos_int)):
            for j in range(2):
                if jogos_int[i][j] != -1:
                    jogos_str[i][j] = str(jogos_int[i][j])

        return jogos_str
    
    def recuperando_grupos(self, grupo: str):
        # Recupera o grupo do jeito que estava
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

        grupo.organizando_grupos()

        return grupo

    def criando_DataFrame(self, grupo: str):
        # Cria um dataframe standart
        nome_grupo = grupo.replace(' ', '')

        inicio = [-1 for i in range(4)]

        data = {self.df_selecoes[nome_grupo][0]:inicio,
                self.df_selecoes[nome_grupo][1]:inicio,
                self.df_selecoes[nome_grupo][2]:inicio,
                self.df_selecoes[nome_grupo][3]:inicio,}

        df_padrao = pd.DataFrame(data, index=self.df_selecoes[nome_grupo])

        return df_padrao
    
    def cria_arq(self, grupo: str):
        #cria um arquivo se ele não existir
        nome_grupo = grupo.replace(' ', '')
        nome_data  = 'dataset/' + nome_grupo + '.pkl'

        if not os.path.exists(nome_data):
            df = self.criando_DataFrame(grupo)
            df.to_pickle(nome_data)
            
if __name__ == '__main__':
    ds = DataSet()
    g  = ds.recuperando_jogos_str('Grupo F')

