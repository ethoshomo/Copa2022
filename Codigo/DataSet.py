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
import os
from select import select
import pandas as pd
from Grupo import Grupo

class DataSet():
    # Inicia a classe com um draframe contendo todos os nomes das seleções
    def __init__(self):
        self.df_selecoes = pd.read_pickle('dataset/Selecoes.plk')
        self.oitavas = []
        
    # A partir dos jogos realizados pelas seleções de um grupo, salva eles 
    # em arquivos do tipo pkl
    def salvando_grupo(self, grupo :str, jogos: list):
        nome_grupo = grupo.replace(' ', '') # Caso o nome venha com espaço

        df_jogos = self.criando_DataFrame(nome_grupo) # Dataframe standart

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

        nome = 'dataset/' + nome_grupo + '.pkl' # path para criação do arquivo

        df_jogos.to_pickle(nome) # Salvamento

    # A partir do dataset recupera o estado que os jogos se encontravam
    def recuperando_jogos(self, grupo: str):
        nome_grupo = grupo.replace(' ', '') # Remove o espaço 

        self.cria_arq(grupo) # Se o arquivo do jogo ainda não existe, cria

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

    # A partir da listas do jogos em int transformas os resultados para str
    # e caso não haja preencimenoto no placar, assume vazio
    def recuperando_jogos_str(self, grupo: str):
        jogos_int = self.recuperando_jogos(grupo)

        jogos_str = [['',''] for i in range(6)]
        
        # Faz a leitura de toda a lista dos jogos em int e faz as alterações 
        # necessárias
        for i in range(len(jogos_int)):
            for j in range(2):
                if jogos_int[i][j] != -1: # Caso gols seja inicializado
                    jogos_str[i][j] = str(jogos_int[i][j])

        return jogos_str

    # A partir dos jogos recuperados, retorna o grupo no estado que ele se
    # encontrava
    def recuperando_grupos(self, grupo: str):
        nome_grupo = grupo.replace(' ', '')

        jogos = self.recuperando_jogos(nome_grupo)

        grupo = Grupo(grupo)

        # Se os jogos estão com um ou dois valores não inicializados, eles
        # não devem ser computados nos resultados dos jogos, para isso faze-
        # uma checagem prévia
        # JOGO 1
        if -1 not in jogos[0]:
            grupo.selecao1.att_jogo(jogos[0][0], jogos[0][1])
            grupo.selecao2.att_jogo(jogos[0][1], jogos[0][0])

        # JOGO 2
        if -1 not in jogos[1]:
            grupo.selecao3.att_jogo(jogos[1][0], jogos[1][1])
            grupo.selecao4.att_jogo(jogos[1][1], jogos[1][0])

        # JOGO 3
        if -1 not in jogos[2]:
            grupo.selecao1.att_jogo(jogos[2][0], jogos[2][1])
            grupo.selecao3.att_jogo(jogos[2][1], jogos[2][0])
        
        # JOGO 4
        if -1 not in jogos[3]:
            grupo.selecao2.att_jogo(jogos[3][1], jogos[3][0])
            grupo.selecao4.att_jogo(jogos[3][0], jogos[3][1])

        # JOGO 5
        if -1 not in jogos[4]:
            grupo.selecao1.att_jogo(jogos[4][1], jogos[4][0])
            grupo.selecao4.att_jogo(jogos[4][0], jogos[4][1])

        # JOGO 6
        if -1 not in jogos[5]:
            grupo.selecao2.att_jogo(jogos[5][0], jogos[5][1])
            grupo.selecao3.att_jogo(jogos[5][1], jogos[5][0])

        grupo.organizando_grupos()

        return grupo

    # Cria um dataframe standart com os valores não inicializados
    def criando_DataFrame(self, grupo: str):
        nome_grupo = grupo.replace(' ', '')

        inicio = [-1 for i in range(4)] # Auxilia a ciação

        # Informações que serão armazenadas
        data = {self.df_selecoes[nome_grupo][0]:inicio,
                self.df_selecoes[nome_grupo][1]:inicio,
                self.df_selecoes[nome_grupo][2]:inicio,
                self.df_selecoes[nome_grupo][3]:inicio,}
        
        # Cria o dataframe
        df_padrao = pd.DataFrame(data, index=self.df_selecoes[nome_grupo])

        return df_padrao

    # Checa se o arquivo exite. Se sim abre normalmente, mas caso contrário
    # cria um arquivos com todos os dados não inicializados
    def cria_arq(self, grupo: str):
        #cria um arquivo se ele não existir
        nome_grupo = grupo.replace(' ', '')
        nome_data  = 'dataset/' + nome_grupo + '.pkl'

        # Checa se existe, em caso false cria
        if not os.path.exists(nome_data):
            df = self.criando_DataFrame(grupo)
            df.to_pickle(nome_data)
            
    def recuperando_grupos_lista(self, grupo: str):
        aux = self.recuperando_grupos(grupo)
        
        return aux.organizando_grupos()
    
    def salvando_oitavas(self, oitavas: list, jogos: list):
        # ------------------------ SELEÇÕES
        times = []
        
        for i in range(8):
            for j in range(2):
                times.append(oitavas[i][j])
        
        
        data_oitavas = {0:times[0],
                        1:times[1],
                        2:times[2],
                        3:times[3],
                        4:times[4],
                        5:times[5],
                        6:times[6],
                        7:times[7],
                        8:times[8],
                        9:times[9],
                        10:times[10],
                        11:times[11],
                        12:times[12],
                        13:times[13],
                        14:times[14],
                        15:times[15]}

        df_oitavas = pd.DataFrame(data_oitavas, index=[0])

        df_oitavas.to_pickle('dataset/Oitavas.pkl')
    
        #------------------------ JOGOS
        inicio = [-1 for i in range(16)]
                
        data_ff = {times[0]:inicio,
                   times[1]:inicio,
                   times[2]:inicio,
                   times[3]:inicio,
                   times[4]:inicio,
                   times[5]:inicio,
                   times[6]:inicio,
                   times[7]:inicio,
                   times[8]:inicio,
                   times[9]:inicio,
                   times[10]:inicio,
                   times[11]:inicio,
                   times[12]:inicio,
                   times[13]:inicio,
                   times[14]:inicio,
                   times[15]:inicio}
        
        df_ff = pd.DataFrame(data_ff, index=times)

        # JOGO 1
        if times[0] != '-' and times[1] != '-':
            df_ff.loc[times[0]][times[1]] = jogos[0][1]
            df_ff.loc[times[1]][times[0]] = jogos[0][0]
        
        # JOGO 2
        if times[2] != '-' and times[3] != '-':
            df_ff.loc[times[2]][times[3]] = jogos[1][1]
            df_ff.loc[times[3]][times[2]] = jogos[1][0]
        
        # JOGO 3
        if times[4] != '-' and times[5] != '-':
            df_ff.loc[times[4]][times[5]] = jogos[2][1]
            df_ff.loc[times[5]][times[4]] = jogos[2][0]
        
        # JOGO 4
        if times[6] != '-' and times[7] != '-':
            df_ff.loc[times[6]][times[7]] = jogos[3][1]
            df_ff.loc[times[7]][times[6]] = jogos[3][0]
        
        # JOGO 5
        if times[8] != '-' and times[9] != '-':
            df_ff.loc[times[8]][times[9]] = jogos[4][1]
            df_ff.loc[times[9]][times[8]] = jogos[4][0]
        
        # JOGO 6
        if times[10] != '-' and times[11] != '-':
            df_ff.loc[times[10]][times[11]] = jogos[5][1]
            df_ff.loc[times[11]][times[10]] = jogos[5][0]
        
        # JOGO 7
        if times[12] != '-' and times[13] != '-':
            df_ff.loc[times[12]][times[13]] = jogos[6][1]
            df_ff.loc[times[13]][times[12]] = jogos[6][0]
        
        # JOGO 8
        if times[14] != '-' and times[15] != '-':
            df_ff.loc[times[14]][times[15]] = jogos[7][1]
            df_ff.loc[times[15]][times[14]] = jogos[7][0]       
        
        df_ff.to_pickle('dataset/FaseFinal.pkl')
        
    def recuperando_oitavas(self):
        aux = [['-', 'imagens/bandeira.png', ''] for i in range(17)]
        
        df_oitavas = pd.read_pickle('dataset/Oitavas.pkl')
        df_ff      = pd.read_pickle('dataset/FaseFinal.pkl')
        
        for i in range(0, 16, 2):
            if df_oitavas[i][0] != '-':
                aux[i+1][0] = df_oitavas[i][0]
                aux[i+1][1] = 'imagens/' + self.converte_palavra(df_oitavas[i][0]) + '.png'
            
            if df_oitavas[i+1][0] != '-':
                aux[i+2][0] = df_oitavas[i+1][0]
                aux[i+2][1] = 'imagens/' + self.converte_palavra(df_oitavas[i+1][0]) + '.png'
                
            if df_oitavas[i][0]  != '-' and df_oitavas[i+1][0] != '-':
                aux[i+1][2] = df_ff[df_oitavas[i][0]][df_oitavas[i+1][0]]
                aux[i+2][2] = df_ff[df_oitavas[i+1][0]][df_oitavas[i][0]]
                
        return aux
    
        
    def converte_palavra(self, palavra):
        palavra = palavra.lower()
        palavra = palavra.replace(" ", "_")
        palavra = palavra.replace("á", "a")
        palavra = palavra.replace("ã", "a")
        palavra = palavra.replace("â", "a")
        palavra = palavra.replace("é", "e")
        palavra = palavra.replace("ê", "e")
        palavra = palavra.replace("ó", "o")
        palavra = palavra.replace("õ", "o")
        palavra = palavra.replace("ô", "o")
        palavra = palavra.replace("í", "i")
        palavra = palavra.replace("ú", "u")
        palavra = palavra.replace("ç", "c")
        return palavra