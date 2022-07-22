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
    """
    Contém os dados de uma seleção relevantes para os cálculos
    requisitados pela lógica do programa.
    Armazena desde o nome, a pontuação, a quantidade de vitórias,
    derrotas e empates, a quantidade de gols marcados e sofridos,
    o saldo de gols, a colocação na tabela do grupo a que pertence
    e o nome da sua bandeira.
    """

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
        """
        Define o nome da seleção.

        :param nome: Nome da seleção.
        """
        self.nome = nome

    def set_pontos(self, pontos: int):
        """
        Define a quantidade de pontos.

        :param pontos: Quantidade de pontos.
        """
        self.pontos = pontos

    def set_gols_marcados(self, gols_marcados: int):
        """
        Define a quantidade de gols marcados.

        :param gols_marcados: Quantidade de gols marcados.
        """
        self.gols_marcados += gols_marcados

    def set_gols_sofridos(self, gols_sofridos: int):
        """
        Define a quantidade de gols sofridos.

        :param gols_sofridos: Quantidade de gols sofridos.
        """
        self.gols_sofridos = gols_sofridos

    def set_bandeira(self, bandeira: str):
        """
        Define a bandeira da seleção.

        :param bandeira: Nova bandeira da seleção.
        """
        self.bandeira = bandeira

    def set_colocacao(self, colocacao: int):
        """
        Define a colocação da seleção.

        :param colocacao: Colocação da seleção.
        """
        self.colocacao = colocacao

    def get_nome(self):
        """
        Retorna o nome da seleção.

        :return self.nome: Nome da seleção.
        """
        return self.nome

    def get_pontos(self):
        """
        Retorna a quantidade de pontos da seleção.

        :return self.pontos: Quantidade de pontos da seleção.
        """
        return self.pontos

    def get_vitorias(self):
        """
        Retorna a quantidade de vitórias da seleção.

        :return self.vitorias: Quantidade de vitórias da seleção.
        """
        return self.vitorias

    def get_empates(self):
        """
        Retorna a quantidade de empates da seleção.

        :return self.empates: Quantidade de empates da seleção
        """

        return self.empates

    def get_gols_marcados(self):
        """
        Retorna a quantidade de gols marcados.

        :return self.gols_marcados: Quantidade de gols marcados.
        """

        return self.gols_marcados

    def get_gols_sofridos(self):
        """
        Retorna a quantidade de gols sofridos.

        :return self.gols_sofridos: Quantidade de gols sofridos.
        """
        return self.gols_sofridos

    def get_bandeira(self):
        """
        Retorna o nome da bandeira da seleção.

        :return self.bandeira: Nome da bandeira da seleção.
        """
        return self.bandeira

    def att_gols_marcados(self, gols_marcados):
        """
        Atualiza a quantidade de gols marcados somando os novos gols marcados.

        :param gols_marcados: Quantidade de novos gols marcados.
        """
        self.gols_marcados += int(gols_marcados)

    def att_gols_sofridos(self, gols_sofridos):
        """
        Atualiza a quantidade de gols sofridos somando os novos gols sofridos.

        :param gols_sofridos: Quantidade de novos gols sofridos.
        """
        self.gols_sofridos += int(gols_sofridos)

    def att_jogo(self, gols_favoraveis, gols_contra):
        """
        Atualiza a quantidade de vitórias, empates, derrotas, o saldo de
        gols e a pontuação da seleção conforme a quantidade de gols
        marcados e sofridos.

        :param gols_favoraveis: Quantidade de gols marcados.
        :param gols_contra: Quantidade de gols sofridos.
        """

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
        """
        Atualiza a quantidade de pontos de acordo com a quantidade de
        vitórias e empates da seleção.
        """
        self.set_pontos(int(self.get_vitorias())*3+int(self.get_empates())*1)

    def __str__(self) -> str:
        s  = str(self.nome) + ' colocação: ' + str(self.colocacao)
        return s

    # Converte as letras não ASCII de um alfabeto e os espaços também
    def converte_palavra(self, palavra):
        """
        Elimina os caractéres especiais e substitui os espaços vazios
        por underlines para aumentar a compatibilidadecom quaisquer sistemas.

        :param palavra: String qualquer.
        :return palavra: Palavra após as modificações.
        """
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
