class Pergunta():
    def __init__(self, campos: list):
        self.questao   = campos[0]
        self.resposta1 = campos[1]
        self.resposta2 = campos[2]
        self.resposta3 = campos[3]
        self.resposta4 = campos[4]
        self.gabarito  = campos[5]
    
    def get_questao(self):
        return self.questao
    
    def get_resposta1(self):
        return self.resposta1

    def get_resposta2(self):
        return self.resposta2

    def get_resposta3(self):
        return self.resposta3

    def get_resposta4(self):
        return self.resposta4
    
    def get_gabarito(self):
        return self.gabarito
    
    def __str__(self):
        s = self.get_questao() + ' ---> ' + self.get_gabarito()
        return s