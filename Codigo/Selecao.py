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
class Selecao():

    def __init__(self, nome: str):
        self.nome = nome
        self.pontos = 0
        self.vitorias = 0
        self.derrotas = 0
        self.empates = 0
        self.gols_marcados = 0
        self.gols_sofridos = 0
        self.saldo_de_gols = 0
        self.colocacao = 0
        self.bandeira = "imagens/bandeiras/" + self.converte_palavra(nome) + ".png"

    def set_nome(self, nome: str):
        self.nome = nome

    def set_pontos(self, pontos: int):
        self.pontos = pontos

    def set_gols_marcados(self, gols_marcados: int):
        self.gols_marcados += gols_marcados

    def set_gols_sofridos(self, gols_sofridos: int):
        self.gols_sofridos = gols_sofridos

    def set_bandeira(self, bandeira: str):
        self.bandeira = bandeira

    def set_colocacao(self, colocacao: int):
        self.colocacao = colocacao

    def get_nome(self):
        return self.nome

    def get_pontos(self):
        return self.pontos

    def get_vitorias(self):
        return self.vitorias

    def get_empates(self):
        return self.empates

    def get_gols_marcados(self):
        return self.gols_marcados

    def get_gols_sofridos(self):
        return self.gols_sofridos

    def get_bandeira(self):
        return self.bandeira

    def att_gols_marcados(self, gols_marcados):
        self.gols_marcados += int(gols_marcados)

    def att_gols_sofridos(self, gols_sofridos):
        self.gols_sofridos += int(gols_sofridos)

    def att_jogo(self, gols_favoraveis, gols_contra):
        # Atualiza dados da Tabela

        # Gols a favor e contra
        self.att_gols_marcados(gols_favoraveis)
        self.att_gols_sofridos(gols_contra)

        # Vitorias, Empates e Derrotas
        if gols_favoraveis == gols_contra:
            self.empates += 1
        elif gols_favoraveis > gols_contra:
            self.vitorias += 1
        elif gols_contra > gols_favoraveis:
            self.derrotas += 1

        self.saldo_de_gols += int(gols_favoraveis) - int(gols_contra)

        # Pontos Ganhos
        self.att_pontos()

    def att_pontos(self):
        self.set_pontos(int(self.get_vitorias())*3+int(self.get_empates())*1)

    def __str__(self) -> str:
        s  = str(self.nome) + ' colocação: ' + str(self.colocacao)
        return s

    # Converte as letras não ASCII de um alfabeto e os espaços também
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
