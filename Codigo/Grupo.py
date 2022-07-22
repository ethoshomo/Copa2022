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

from atualizacao import Atualizacao
import pandas as pd
from Selecao import Selecao

class Grupo(Selecao):
    """
    A partir do nome de um grupo, acessa as seleções que estão contidas nele
    e cria os objetos do tipo seleção com seus respectivos nomes. Após isso,
    inicia as colocações das seleções na tabela da UI
    """
    def __init__(self, grupo: str):
        nome_grupo = grupo.replace(' ', '') # Formatação

        # A partir do nome do grupo, acessa as seleções contida
        # nele e cria os objetos do tipo seleção com seus nomes
        df_selecoes   = pd.read_pickle('dataset/Selecoes.plk')
        self.selecao1 = Selecao(df_selecoes[nome_grupo][0])
        self.selecao2 = Selecao(df_selecoes[nome_grupo][1])
        self.selecao3 = Selecao(df_selecoes[nome_grupo][2])
        self.selecao4 = Selecao(df_selecoes[nome_grupo][3])

        self.nome_grupo = grupo # Nome do grupo com ' '

        # Inicia as colocações das seleções na tabela
        self.selecao1.set_colocacao(1)
        self.selecao2.set_colocacao(2)
        self.selecao3.set_colocacao(3)
        self.selecao4.set_colocacao(4)

    def organizando_grupos(self):
        """
        A partir dos dados das seleções, faz a ordenação das colocações no grupo
        segundo a ordem estabelecida pela classificação da FIFA, que segue a
        seguinte prioridade: pontos, saldo de gols e vitórias.

        :return lista_grupos: Lista com cada uma das seleções em ordem com as regras da FIFA.
        """

        # Cria lista para ser ordenada
        lista_grupos = [self.selecao1, self.selecao2, self.selecao3, self.selecao4]

        # Ordena os grupos com a ordem de prioridae
        lista_grupos.sort(key=lambda x: x.vitorias     , reverse=True)
        lista_grupos.sort(key=lambda x: x.saldo_de_gols, reverse=True)
        lista_grupos.sort(key=lambda x: x.pontos       , reverse=True)

        # Seta a colocação da seleção com a posição dela no vetor
        self.selecao1.set_colocacao(lista_grupos.index(self.selecao1)+1)
        self.selecao2.set_colocacao(lista_grupos.index(self.selecao2)+1)
        self.selecao3.set_colocacao(lista_grupos.index(self.selecao3)+1)
        self.selecao4.set_colocacao(lista_grupos.index(self.selecao4)+1)

        return lista_grupos

    def atualizar(self, atualizar: Atualizacao):
        """
        Quando o programa é inicializado, é criado um Objeto atualização que
        recebe as variáveis do grupo. Essas variáveis são dinâmicas e pertencem à
        interface. Com elas, a função atualiza os valores de um grupo.

        :param atualizar: Valores atuais do grupo que serão utilizados para atualizar o grupo.
        """
        # Atualiza posicoes
        self.organizando_grupos()

        # Atualizar nome do Grupo
        atualizar.grupo_nome.set(self.nome_grupo)

        # Atualizando Selecao 1
        atualizar.s1_nome.set(self.selecao1.nome)
        atualizar.s1_bandeira.set(self.selecao1.bandeira)
        atualizar.s1_pontos.set(self.selecao1.pontos)
        atualizar.s1_vitorias.set(self.selecao1.vitorias)
        atualizar.s1_empates.set(self.selecao1.empates)
        atualizar.s1_derrotas.set(self.selecao1.derrotas)
        atualizar.s1_gols_favoraveis.set(self.selecao1.gols_marcados)
        atualizar.s1_gols_contrarios.set(self.selecao1.gols_sofridos)
        atualizar.s1_saldo_gols.set(self.selecao1.saldo_de_gols)
        atualizar.s1_colocacao.set(self.selecao1.colocacao)

        # Atualizando Selecao 2
        atualizar.s2_nome.set(self.selecao2.nome)
        atualizar.s2_bandeira.set(self.selecao2.bandeira)
        atualizar.s2_pontos.set(self.selecao2.pontos)
        atualizar.s2_vitorias.set(self.selecao2.vitorias)
        atualizar.s2_empates.set(self.selecao2.empates)
        atualizar.s2_derrotas.set(self.selecao2.derrotas)
        atualizar.s2_gols_favoraveis.set(self.selecao2.gols_marcados)
        atualizar.s2_gols_contrarios.set(self.selecao2.gols_sofridos)
        atualizar.s2_saldo_gols.set(self.selecao2.saldo_de_gols)
        atualizar.s2_colocacao.set(self.selecao2.colocacao)

        # Atualizando Selecao 3
        atualizar.s3_nome.set(self.selecao3.nome)
        atualizar.s3_bandeira.set(self.selecao3.bandeira)
        atualizar.s3_pontos.set(self.selecao3.pontos)
        atualizar.s3_vitorias.set(self.selecao3.vitorias)
        atualizar.s3_empates.set(self.selecao3.empates)
        atualizar.s3_derrotas.set(self.selecao3.derrotas)
        atualizar.s3_gols_favoraveis.set(self.selecao3.gols_marcados)
        atualizar.s3_gols_contrarios.set(self.selecao3.gols_sofridos)
        atualizar.s3_saldo_gols.set(self.selecao3.saldo_de_gols)
        atualizar.s3_colocacao.set(self.selecao3.colocacao)

        # Atualizando Selecao 4
        atualizar.s4_nome.set(self.selecao4.nome)
        atualizar.s4_bandeira.set(self.selecao4.bandeira)
        atualizar.s4_pontos.set(self.selecao4.pontos)
        atualizar.s4_vitorias.set(self.selecao4.vitorias)
        atualizar.s4_empates.set(self.selecao4.empates)
        atualizar.s4_derrotas.set(self.selecao4.derrotas)
        atualizar.s4_gols_favoraveis.set(self.selecao4.gols_marcados)
        atualizar.s4_gols_contrarios.set(self.selecao4.gols_sofridos)
        atualizar.s4_saldo_gols.set(self.selecao4.saldo_de_gols)
        atualizar.s4_colocacao.set(self.selecao4.colocacao)