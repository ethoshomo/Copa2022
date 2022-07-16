from Atualizacao import Atualizacao
import pandas as pd
from Selecao import Selecao

class Grupo(Selecao):
    def __init__(self, grupo: str):
        nome_grupo = grupo.replace(' ', '')

        df_selecoes   = pd.read_pickle('dataset/Selecoes.plk')
        self.selecao1 = Selecao(df_selecoes[nome_grupo][0])
        self.selecao2 = Selecao(df_selecoes[nome_grupo][1])
        self.selecao3 = Selecao(df_selecoes[nome_grupo][2])
        self.selecao4 = Selecao(df_selecoes[nome_grupo][3])

        self.nome_grupo = grupo

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

        lista_grupos.sort(key=lambda x: x.vitorias     , reverse=True)
        lista_grupos.sort(key=lambda x: x.saldo_de_gols, reverse=True)
        lista_grupos.sort(key=lambda x: x.pontos       , reverse=True)

        self.selecao1.set_colocacao(lista_grupos.index(self.selecao1))
        self.selecao2.set_colocacao(lista_grupos.index(self.selecao2))
        self.selecao3.set_colocacao(lista_grupos.index(self.selecao3))
        self.selecao4.set_colocacao(lista_grupos.index(self.selecao4))

    def atualizar(self, atualizar: Atualizacao):
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


if __name__ == "__main__":
    gA = Grupo('Grupo A')
    gA.teste()
    gA.selecao1.att_jogo(2,1)
    gA.selecao2.att_jogo(1,2)
    gA.organizando_grupos()
    gA.teste()


    gB = Grupo('Grupo B')
    gB.teste()

    gB = Grupo('Grupo C')
    gB.teste()

    gC = Grupo('Grupo D')
    gC.teste()

    gC = Grupo('Grupo E')
    gC.teste()
