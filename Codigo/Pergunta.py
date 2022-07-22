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

class Pergunta():
    """
    Controla as váriáveis da janela do Quiz da Copa.
    """

    # Incia o objeto pergunta com seus repectivas informações
    def __init__(self, campos: list):
        self.questao   = campos[0]
        self.resposta1 = campos[1]
        self.resposta2 = campos[2]
        self.resposta3 = campos[3]
        self.resposta4 = campos[4]
        self.gabarito  = campos[5]

    def get_questao(self):
        """
        Devolve a string da pergunta.

        :return self.questao: String da pergunta.
        """
        return self.questao

    def get_resposta1(self):
        """
        Devolve a string da primeira resposta.

        :return self.resposta1: String da primeira resposta.
        """
        return self.resposta1

    def get_resposta2(self):
        """
        Devolve a string da segunda resposta.

        :return self.resposta2: String da segunda resposta.
        """
        return self.resposta2

    def get_resposta3(self):
        """
        Devolve a string da terceira resposta.

        :return self.resposta3: String da terceita resposta.
        """
        return self.resposta3

    def get_resposta4(self):
        """
        Devolve a string da quarta resposta.

        :return self.resposta4: String da quarta resposta.
        """
        return self.resposta4

    def get_gabarito(self):
        """
        Devolve a string da resposta correta.

        :return self.gabarito: String da resposta correta.
        """
        return self.gabarito