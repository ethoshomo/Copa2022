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
        self.bandeira = "../imagens/bandeiras/" + nome + ".png"

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

    def att_gols_marcados(self, gols_marcados: int):
        self.gols_marcados += gols_marcados

    def att_gols_sofridos(self, gols_sofridos: int):
        self.gols_sofridos += gols_sofridos

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

        self.saldo_de_gols += gols_favoraveis - gols_contra

        # Pontos Ganhos
        self.att_pontos()

    def att_pontos(self):
        self.set_pontos(self.get_vitorias()*3+self.get_empates()*1)

    def __str__(self) -> str:
        s  = str(self.nome) + ' ' + str(self.saldo_de_gols) + ' ' + str(self.pontos) + ' ' + str(self.colocacao)
        return s
