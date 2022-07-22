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

from tkinter import StringVar
from Grupo import *


# Essa classe agrupa conjuntos de variaveis que serão usadas em
# atualizações do programa.
class Atualizacao:
    """
    Armazena os valores das strings variáveis das seleções de um grupo relacionadas
    inputs recebidos do usuário através da interface e armazena, tambeḿ, os aos
    valores calculados a partir desses inputs. Esses valores serão utilizados
    para atualizar os arquivos da base de dados.
    """

    def __init__(self, g):
        # Nome do Grupo
        self.grupo_nome = StringVar(value=g.nome_grupo)

        # Relativas à Seleção 1
        self.s1_nome = StringVar(value=g.selecao1.nome)
        self.s1_bandeira = StringVar(value=g.selecao1.bandeira)
        self.s1_pontos = StringVar(value=g.selecao1.pontos)
        self.s1_vitorias = StringVar(value=g.selecao1.vitorias)
        self.s1_empates = StringVar(value=g.selecao1.empates)
        self.s1_derrotas = StringVar(value=g.selecao1.derrotas)
        self.s1_gols_favoraveis = StringVar(value=g.selecao1.gols_marcados)
        self.s1_gols_contrarios = StringVar(value=g.selecao1.gols_sofridos)
        self.s1_saldo_gols = StringVar(value=g.selecao1.saldo_de_gols)
        self.s1_colocacao = StringVar(value=g.selecao1.colocacao)

        # Relativas à Seleção 2
        self.s2_nome = StringVar(value=g.selecao2.nome)
        self.s2_bandeira = StringVar(value=g.selecao2.bandeira)
        self.s2_pontos = StringVar(value=g.selecao2.pontos)
        self.s2_vitorias = StringVar(value=g.selecao2.vitorias)
        self.s2_empates = StringVar(value=g.selecao2.empates)
        self.s2_derrotas = StringVar(value=g.selecao2.derrotas)
        self.s2_gols_favoraveis = StringVar(value=g.selecao2.gols_marcados)
        self.s2_gols_contrarios = StringVar(value=g.selecao2.gols_sofridos)
        self.s2_saldo_gols = StringVar(value=g.selecao2.saldo_de_gols)
        self.s2_colocacao = StringVar(value=g.selecao2.colocacao)

        # Relativas à Seleção 3
        self.s3_nome = StringVar(value=g.selecao3.nome)
        self.s3_bandeira = StringVar(value=g.selecao3.bandeira)
        self.s3_pontos = StringVar(value=g.selecao3.pontos)
        self.s3_vitorias = StringVar(value=g.selecao3.vitorias)
        self.s3_empates = StringVar(value=g.selecao3.empates)
        self.s3_derrotas = StringVar(value=g.selecao3.derrotas)
        self.s3_gols_favoraveis = StringVar(value=g.selecao3.gols_marcados)
        self.s3_gols_contrarios = StringVar(value=g.selecao3.gols_sofridos)
        self.s3_saldo_gols = StringVar(value=g.selecao3.saldo_de_gols)
        self.s3_colocacao = StringVar(value=g.selecao3.colocacao)

        # Relativas à Seleção 4
        self.s4_nome = StringVar(value=g.selecao4.nome)
        self.s4_bandeira = StringVar(value=g.selecao4.bandeira)
        self.s4_pontos = StringVar(value=g.selecao4.pontos)
        self.s4_vitorias = StringVar(value=g.selecao4.vitorias)
        self.s4_empates = StringVar(value=g.selecao4.empates)
        self.s4_derrotas = StringVar(value=g.selecao4.derrotas)
        self.s4_gols_favoraveis = StringVar(value=g.selecao4.gols_marcados)
        self.s4_gols_contrarios = StringVar(value=g.selecao4.gols_sofridos)
        self.s4_saldo_gols = StringVar(value=g.selecao4.saldo_de_gols)
        self.s4_colocacao = StringVar(value=g.selecao4.colocacao)


class AtualizarOitavas:
    """
    Armazena os valores das strings variáveis das oitavas de final
    relacionadas à quantidade de gols inserida pelo usuário através da
    interface e aos nomes e bandeiras das seleções vitoriosas da fase de
    grupos. Esses valores serão utilizados para atualizar os arquivos da
    base de dados.
    """
    def __init__(self, dados: list):

        self.s1_str = StringVar(value=dados[0][0])
        self.s1_band = StringVar(value=dados[0][1])
        self.s1_gol = StringVar(value=dados[0][2])

        self.s2_str = StringVar(value=dados[1][0])
        self.s2_band = StringVar(value=dados[1][1])
        self.s2_gol = StringVar(value=dados[1][2])

        self.s3_str = StringVar(value=dados[2][0])
        self.s3_band = StringVar(value=dados[2][1])
        self.s3_gol = StringVar(value=dados[2][2])

        self.s4_str = StringVar(value=dados[3][0])
        self.s4_band = StringVar(value=dados[3][1])
        self.s4_gol = StringVar(value=dados[3][2])

        self.s5_str = StringVar(value=dados[4][0])
        self.s5_band = StringVar(value=dados[4][1])
        self.s5_gol = StringVar(value=dados[4][2])

        self.s6_str = StringVar(value=dados[5][0])
        self.s6_band = StringVar(value=dados[5][1])
        self.s6_gol = StringVar(value=dados[5][2])

        self.s7_str = StringVar(value=dados[6][0])
        self.s7_band = StringVar(value=dados[6][1])
        self.s7_gol = StringVar(value=dados[6][2])

        self.s8_str = StringVar(value=dados[7][0])
        self.s8_band = StringVar(value=dados[7][1])
        self.s8_gol = StringVar(value=dados[7][2])

        self.s9_str = StringVar(value=dados[8][0])
        self.s9_band = StringVar(value=dados[8][1])
        self.s9_gol = StringVar(value=dados[8][2])

        self.s10_str = StringVar(value=dados[9][0])
        self.s10_band = StringVar(value=dados[9][1])
        self.s10_gol = StringVar(value=dados[9][2])

        self.s11_str = StringVar(value=dados[10][0])
        self.s11_band = StringVar(value=dados[10][1])
        self.s11_gol = StringVar(value=dados[10][2])

        self.s12_str = StringVar(value=dados[11][0])
        self.s12_band = StringVar(value=dados[11][1])
        self.s12_gol = StringVar(value=dados[11][2])

        self.s13_str = StringVar(value=dados[12][0])
        self.s13_band = StringVar(value=dados[12][1])
        self.s13_gol = StringVar(value=dados[12][2])

        self.s14_str = StringVar(value=dados[13][0])
        self.s14_band = StringVar(value=dados[13][1])
        self.s14_gol = StringVar(value=dados[13][2])

        self.s15_str = StringVar(value=dados[14][0])
        self.s15_band = StringVar(value=dados[14][1])
        self.s15_gol = StringVar(value=dados[14][2])

        self.s16_str = StringVar(value=dados[15][0])
        self.s16_band = StringVar(value=dados[15][1])
        self.s16_gol = StringVar(value=dados[15][2])

    def atualizar(self, dados: list):
        """
        Atualiza os valores da classe para que estejam coerentes
        com os novos valores inseridos pelo usuário.

        :param dados: Dados de debugação que serão impressos.
        """

        self.s1_str.set(value=dados[0][0])
        self.s1_band.set(value=dados[0][1])
        self.s1_gol.set(value=dados[0][2])

        self.s2_str.set(value=dados[1][0])
        self.s2_band.set(value=dados[1][1])
        self.s2_gol.set(value=dados[1][2])

        self.s3_str.set(value=dados[2][0])
        self.s3_band.set(value=dados[2][1])
        self.s3_gol.set(value=dados[2][2])

        self.s4_str.set(value=dados[3][0])
        self.s4_band.set(value=dados[3][1])
        self.s4_gol.set(value=dados[3][2])

        self.s5_str.set(value=dados[4][0])
        self.s5_band.set(value=dados[4][1])
        self.s5_gol.set(value=dados[4][2])

        self.s6_str.set(value=dados[5][0])
        self.s6_band.set(value=dados[5][1])
        self.s6_gol.set(value=dados[5][2])

        self.s7_str.set(value=dados[6][0])
        self.s7_band.set(value=dados[6][1])
        self.s7_gol.set(value=dados[6][2])

        self.s8_str.set(value=dados[7][0])
        self.s8_band.set(value=dados[7][1])
        self.s8_gol.set(value=dados[7][2])

        self.s9_str.set(value=dados[8][0])
        self.s9_band.set(value=dados[8][1])
        self.s9_gol.set(value=dados[8][2])

        self.s10_str.set(value=dados[9][0])
        self.s10_band.set(value=dados[9][1])
        self.s10_gol.set(value=dados[9][2])

        self.s11_str.set(value=dados[10][0])
        self.s11_band.set(value=dados[10][1])
        self.s11_gol.set(value=dados[10][2])

        self.s12_str.set(value=dados[11][0])
        self.s12_band.set(value=dados[11][1])
        self.s12_gol.set(value=dados[11][2])

        self.s13_str.set(value=dados[12][0])
        self.s13_band.set(value=dados[12][1])
        self.s13_gol.set(value=dados[12][2])

        self.s14_str.set(value=dados[13][0])
        self.s14_band.set(value=dados[13][1])
        self.s14_gol.set(value=dados[13][2])

        self.s15_str.set(value=dados[14][0])
        self.s15_band.set(value=dados[14][1])
        self.s15_gol.set(value=dados[14][2])

        self.s16_str.set(value=dados[15][0])
        self.s16_band.set(value=dados[15][1])
        self.s16_gol.set(value=dados[15][2])


class AutalizarQuartas:
    """
    Armazena os valores das strings variáveis das quartas de final
    relacionadas à quantidade de gols inserida pelo usuário através da
    interface e aos nomes e bandeiras das seleções vitoriosas das oitavas
    de final. Esses valores serão utilizados para atualizar os arquivos
    da base de dados.
    """

    def __init__(self, dados: list):

        self.s1_str = StringVar(value=dados[0][0])
        self.s1_band = StringVar(value=dados[0][1])
        self.s1_gol = StringVar(value=dados[0][2])

        self.s2_str = StringVar(value=dados[1][0])
        self.s2_band = StringVar(value=dados[1][1])
        self.s2_gol = StringVar(value=dados[1][2])

        self.s3_str = StringVar(value=dados[2][0])
        self.s3_band = StringVar(value=dados[2][1])
        self.s3_gol = StringVar(value=dados[2][2])

        self.s4_str = StringVar(value=dados[3][0])
        self.s4_band = StringVar(value=dados[3][1])
        self.s4_gol = StringVar(value=dados[3][2])

        self.s5_str = StringVar(value=dados[4][0])
        self.s5_band = StringVar(value=dados[4][1])
        self.s5_gol = StringVar(value=dados[4][2])

        self.s6_str = StringVar(value=dados[5][0])
        self.s6_band = StringVar(value=dados[5][1])
        self.s6_gol = StringVar(value=dados[5][2])

        self.s7_str = StringVar(value=dados[6][0])
        self.s7_band = StringVar(value=dados[6][1])
        self.s7_gol = StringVar(value=dados[6][2])

        self.s8_str = StringVar(value=dados[7][0])
        self.s8_band = StringVar(value=dados[7][1])
        self.s8_gol = StringVar(value=dados[7][2])


    def atualizar(self, dados: list):
        """
        Atualiza os valores da classe para que estejam coerentes
        com os novos valores inseridos pelo usuário.

        :param dados: Dados de debugação que serão impressos.
        """

        self.s1_str.set(value=dados[0][0])
        self.s1_band.set(value=dados[0][1])
        self.s1_gol.set(value=dados[0][2])

        self.s2_str.set(value=dados[1][0])
        self.s2_band.set(value=dados[1][1])
        self.s2_gol.set(value=dados[1][2])

        self.s3_str.set(value=dados[2][0])
        self.s3_band.set(value=dados[2][1])
        self.s3_gol.set(value=dados[2][2])

        self.s4_str.set(value=dados[3][0])
        self.s4_band.set(value=dados[3][1])
        self.s4_gol.set(value=dados[3][2])

        self.s5_str.set(value=dados[4][0])
        self.s5_band.set(value=dados[4][1])
        self.s5_gol.set(value=dados[4][2])

        self.s6_str.set(value=dados[5][0])
        self.s6_band.set(value=dados[5][1])
        self.s6_gol.set(value=dados[5][2])

        self.s7_str.set(value=dados[6][0])
        self.s7_band.set(value=dados[6][1])
        self.s7_gol.set(value=dados[6][2])

        self.s8_str.set(value=dados[7][0])
        self.s8_band.set(value=dados[7][1])
        self.s8_gol.set(value=dados[7][2])



class AtualizarFinalSemi:
    """
    Armazena os valores das strings variáveis das semfinais e da final
    relacionadas à quantidade de gols inserida pelo usuário através da
    interface e aos nomes e bandeiras das seleções vitoriosas das quartas
    de final. Esses valores serão utilizados para atualizar os arquivos
    da base de dados.
    """

    def __init__(self, dados : list):

        self.s1_str = StringVar(value=dados[0][0])
        self.s1_band = StringVar(value=dados[0][1])
        self.s1_gol = StringVar(value=dados[0][2])

        self.s2_str = StringVar(value=dados[1][0])
        self.s2_band = StringVar(value=dados[1][1])
        self.s2_gol = StringVar(value=dados[1][2])

        self.s3_str = StringVar(value=dados[2][0])
        self.s3_band = StringVar(value=dados[2][1])
        self.s3_gol = StringVar(value=dados[2][2])

        self.s4_str = StringVar(value=dados[3][0])
        self.s4_band = StringVar(value=dados[3][1])
        self.s4_gol = StringVar(value=dados[3][2])


    def atualizar(self, dados: list):
        """
        Atualiza os valores da classe para que estejam coerentes
        com os novos valores inseridos pelo usuário.

        :param dados: Dados de debugação que serão impressos.
        """

        self.s1_str.set(value=dados[0][0])
        self.s1_band.set(value=dados[0][1])
        self.s1_gol.set(value=dados[0][2])

        self.s2_str.set(value=dados[1][0])
        self.s2_band.set(value=dados[1][1])
        self.s2_gol.set(value=dados[1][2])

        self.s3_str.set(value=dados[2][0])
        self.s3_band.set(value=dados[2][1])
        self.s3_gol.set(value=dados[2][2])

        self.s4_str.set(value=dados[3][0])
        self.s4_band.set(value=dados[3][1])
        self.s4_gol.set(value=dados[3][2])
