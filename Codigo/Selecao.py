
import re


class Selecao():
    def __init__(self, nome: str):
        self.nome = nome
        self.pontos = 0
        self.gols_marcados = 0
        self.gols_sofridos = 0
        self.bandeira = None

    def set_nome(self, nome: str):
        self.nome = nome

    def set_pontos(self, pontos: int):
        self.pontos = pontos

    def set_gols_marcados(self, gols_marcados: int):
        self.gols_marcados = gols_marcados

    def set_gols_sofridos(self, gols_sofridos: int):
        self.gols_sofridos = gols_sofridos

    def set_bandeira(self, bandeira: str): # Arrumar depois
        self.bandeira = bandeira

    def get_nome(self):
        return self.nome

    def get_pontos(self):
        return self.pontos

    def get_gols_marcados(self):
        return self.gols_marcados

    def get_gols_sofridos(self):
        return self.gols_sofridos

    def get_bandeira(self):
        return self.bandeira

    def att_gols_marcados(self, gols_marcados: int):
        self.gols_marcados += gols_marcados

    def attt_gols_sofridos(self, gols_sofridos: int):
        self.gols_sofridos += gols_sofridos

    def __str__(self) -> str:
        return self.nome
