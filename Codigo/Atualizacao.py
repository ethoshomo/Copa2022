from tkinter import StringVar
from Grupo import *


class Atualizacao:

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
        self.s1_colocacao = g.selecao1.colocacao

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
        self.s2_colocacao = g.selecao2.colocacao

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
        self.s3_colocacao = g.selecao3.colocacao

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
        self.s4_colocacao = g.selecao4.colocacao


class AtualizacaoResultados:

    def __init__(self):
        self.resultado11 = int()
        self.resultado12 = int()
        self.resultado21 = int()
        self.resultado22 = int()
        self.resultado31 = int()
        self.resultado32 = int()
        self.resultado41 = int()
        self.resultado42 = int()
        self.resultado51 = int()
        self.resultado52 = int()
        self.resultado61 = int()
        self.resultado62 = int()
