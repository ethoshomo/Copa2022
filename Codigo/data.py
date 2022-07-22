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

from click import password_option
from Grupo import Grupo
import pandas as pd



"""
                            OBSERVAÇÕES RELEVANTES

Este arquivo teve a utilidade de criar um banco de dados relacionado às seleções e às perguntas do
Quizz. Desse modo, os arquivos Perguntas.pkl e Selecoes.plk não devem ser deletados, sob pena de
ocorrência de erros na execução do programa. Caso tenham sido removidos por qualquer motivo,
basta executar esse arquivo para que sejam criados novos arquivos.

"""

def criando_pkl_jogos(nomes):
    """
    Cria um arquivo da base de dados com os nomes das seleções
    dos jogos de um grupo, mas com a quantidade de gols marcados
    vazia.

    :param nomes: Nomes das seleções de cada jogo.
    """
    lista_zeros = ['---' for i in range(4)]

    data = {nomes[0][0]:lista_zeros,
            nomes[0][1]:lista_zeros,
            nomes[0][2]:lista_zeros,
            nomes[0][3]:lista_zeros}

    df = pd.DataFrame(data, index=nomes[0])

    print(df)
    print()

def criando_pkl_selecoes(nomes):
    """
    Cria um arquivada da base de dados com os nomes das seleções
    de cada de cada grupo.

    :param nomes: Lista de listas com os nomes das seleções de cada grupo.
    """
    data_selecoes = {'GrupoA':nomes[0],
                     'GrupoB':nomes[1],
                     'GrupoC':nomes[2],
                     'GrupoD':nomes[3],
                     'GrupoE':nomes[4],
                     'GrupoF':nomes[5],
                     'GrupoG':nomes[6],
                     'GrupoH':nomes[7],}

    dataFrame_selecoes = pd.DataFrame(data_selecoes)

    dataFrame_selecoes.to_pickle('dataset/Selecoes.plk')

    dados_selecoes = pd.read_pickle('dataset/Selecoes.plk')

    print(dados_selecoes)
    print()

def nomes_por_grupo():
    """
    Retorna uma lista de listas com cada um dos nomes das seleções dos grupos das
    seleções que participarão da Copa do Mundo de 2022.

    :return nomes: Lista de listas com os nomes das seleções dos grupos. Cada sublista é um grupo.
    """
    nomes = [['Catar', 'Equador', 'Senegal', 'Holanda'],
             ['Inglaterra', 'Irã', 'Estados Unidos', 'País de Gales'],
             ['Argentina', 'Arábia Saudita', 'México', 'Polônia'],
             ['França', 'Austrália', 'Dinamarca', 'Tunísia'],
             ['Espanha', 'Costa Rica', 'Alemanha', 'Japão'],
             ['Bélgica', 'Canadá', 'Marrocos', 'Croácia'],
             ['Brasil', 'Sérvia', 'Suíça', 'Camarões'],
             ['Portugal', 'Gana', 'Uruguai', 'Coreia do Sul']]

    return nomes

def perguntas_quiz():
    """
    Encapsula as peguntas do Quiz da Copa em um arquivo da base dados.
    """
    perguntas = [[] for i in range(11)]

    perguntas[0] = ['Em que ano o Brasil conquistou sua primeira Copa da mundo?',
                    '1994',
                    '1958',
                    '1962',
                    '1950',
                    '1958']
    perguntas[1] = ['Quem é o maior goleador de todas as copas?',
                    'Ronaldo Fenômeno',
                    'Pelé',
                    'Miroslav Klose',
                    'Cristiano Ronaldo',
                    'Miroslav Klose']
    perguntas[2] = ['"A mão de deus" é um gol histórico da Copa do Mundo marcado por Maradona. O argentino marcou esse gol contra qual seleção?',
                    'Inglaterra',
                    'Brasil',
                    'Itália',
                    'Alemanha',
                    'Inglaterra']
    perguntas[3] = ['A Copa do mundo de 2010 foi sediada em qual país?',
                    'Brasil',
                    'África do Sul',
                    'Espanhã',
                    'Senegal',
                    'África do Sul']
    perguntas[4] = ['Em 1950, a seleção brasileira buscava seu primiero campeonato, porém sofreu uma derrota por 2x1 para a seleção do Uruguai. Como ficou conhecido esse episódio?',
                    'A derrota',
                    'A derrocada',
                    'Mineiraço',
                    'Maracanaço',
                    'Maracanaço']
    perguntas[5] = ['O Brasil é penta campeão mundial. Em que anos foram seus títulos?',
                    '1958 1962 1970 1994 2002',
                    '1950 1966 1978 1998 2002',
                    '1950 1966 1974 1990 2014',
                    '1947 1960 1973 2012 2017',
                    '1958 1962 1970 1994 2002']
    perguntas[6] = ['Na derrota humilhante por 7x1 para Alemanha na Copa de 2014, qual jogador marcou o gol brasileiro?',
                    'Neymar Jr.',
                    'Oscar',
                    'Klose',
                    'Kroos',
                    'Oscar']
    perguntas[7] = ['Qual jogador brasileiro homenageou seu filho que estava para nascer na Copa de 1994?',
                    'Romario',
                    'Bebeto',
                    'Taffarel',
                    'Rai',
                    'Bebeto']
    perguntas[8] = ['Qual a seleção que possuí mais vices de Copa do Mundo?',
                    'Brasil',
                    'Vasco',
                    'Alemanha',
                    'Itáia',
                    'Alemanha']
    perguntas[9] = ['Nas quartas de finais, da Copa de 1994, o Brasil enfrentou a seleção da Holanda e saiu vitorioso por causa de um gol de falta. Quem marcou o gol?',
                    'Romârio',
                    'Bebeto',
                    'Branco',
                    'Dunga',
                    'Branco']
    perguntas[10] = ['Quantas seleções já venceram a Copa do Mundo?',
                     '7',
                     '8',
                     '9',
                     '10',
                     '8']

    data_perguntas = {0:perguntas[0],
                      1:perguntas[1],
                      2:perguntas[2],
                      3:perguntas[3],
                      4:perguntas[4],
                      5:perguntas[5],
                      6:perguntas[6],
                      7:perguntas[7],
                      8:perguntas[8],
                      9:perguntas[9],
                      10:perguntas[10]}

    df_pergutas = pd.DataFrame(data_perguntas)

    df_pergutas.to_pickle('dataset/Perguntas.pkl')

    print(df_pergutas[7])

if __name__ == '__main__':
    perguntas_quiz()
