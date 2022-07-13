from cmath import pi
from itertools import repeat
from numpy import column_stack
from tkinter import *
from PIL import Image, ImageTk
import pygame
import random
from Selecao import Selecao
import pandas as pd


class Grupo():
    def __init__(self) -> None:
        self.grupos = [[] for i in range(8)]

    def formando_grupos(self):
        selecoes = pd.read_csv('selecoes.csv', header=None)

        linhas = selecoes.shape[0]
        colunas = selecoes.shape[1]

        for i in range(linhas):
            for j in range(colunas):
                self.grupos[i].append(Selecao(selecoes[j][i]))

    def janela_grupos(self):
        # Variaveis
        selecao1_nome = str("Brasil")
        selecao_bandeira = "imagens/brasil.png"
        selecao1_pontos = int(0)
        selecao1_jogos = int(0)
        selecao1_vitorias = int(0)
        selecao1_empates = int(0)
        selecao1_derrotas = int(0)
        selecao1_gols_favoraveis = int(0)
        selecao1_gols_contrarios = int(0)

        # Cria a janela de Fase de Grupos
        janela2 = Toplevel()
        janela2.title("SHOW DE BOLA - QUIZZ")
        janela2.configure(background='#405E38')
        janela2.geometry("800x600+200+200")
        janela2.transient(janela)
        janela2.focus_force()
        janela2.grab_set()
        janela2.resizable(True, True)

        # Personaliza o background
        bg = ImageTk.PhotoImage(Image.open('imagens/campo.png').resize((800, 600)))
        canvas = Canvas(janela2, width=800, height=600)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor="nw")

        # Frame de Grupos
        frame = Frame(janela2, bg="white")
        frame.grid_anchor(CENTER)
        frame.place(relx=0.05, rely=0.03, relwidth=0.9, relheight=0.05)

        # Botões dos Grupos
        btn_grupo_a = Button(frame,
                             font="Verdana 10 bold",
                             text="Grupo A",
                             bd=0,
                             padx=2,
                             pady=2,
                             bg="#405E38",
                             fg="white",
                             command=lambda: quit(janela2))
        btn_grupo_a.grid(row=0, column=0, padx=1)

        btn_grupo_b = Button(frame,
                             font="Verdana 10 bold",
                             text="Grupo B",
                             bd=0,
                             padx=2,
                             pady=2,
                             bg="#405E38",
                             fg="white",
                             command=lambda: quit(janela2))
        btn_grupo_b.grid(row=0, column=1, padx=1)

        btn_grupo_c = Button(frame,
                             font="Verdana 10 bold",
                             text="Grupo C",
                             bd=0,
                             padx=2,
                             pady=2,
                             bg="#405E38",
                             fg="white",
                             command=lambda: quit(janela2))
        btn_grupo_c.grid(row=0, column=2, padx=1)

        btn_grupo_d = Button(frame,
                             font="Verdana 10 bold",
                             text="Grupo D",
                             bd=0,
                             padx=2,
                             pady=2,
                             bg="#405E38",
                             fg="white",
                             command=lambda: quit(janela2))
        btn_grupo_d.grid(row=0, column=3, padx=1)

        btn_grupo_e = Button(frame,
                             font="Verdana 10 bold",
                             text="Grupo E",
                             bd=0,
                             padx=2,
                             pady=2,
                             bg="#405E38",
                             fg="white",
                             command=lambda: quit(janela2))
        btn_grupo_e.grid(row=0, column=4, padx=1)

        btn_grupo_f = Button(frame,
                             font="Verdana 10 bold",
                             text="Grupo F",
                             bd=0,
                             padx=2,
                             pady=2,
                             bg="#405E38",
                             fg="white",
                             command=lambda: quit(janela2))
        btn_grupo_f.grid(row=0, column=5, padx=1)

        btn_grupo_g = Button(frame,
                             font="Verdana 10 bold",
                             text="Grupo G",
                             bd=0,
                             padx=2,
                             pady=2,
                             bg="#405E38",
                             fg="white",
                             command=lambda: quit(janela2))
        btn_grupo_g.grid(row=0, column=6, padx=1)

        btn_grupo_h = Button(frame,
                             font="Verdana 10 bold",
                             text="Grupo H",
                             bd=0,
                             padx=2,
                             pady=2,
                             bg="#405E38",
                             fg="white",
                             command=lambda: quit(janela2))
        btn_grupo_h.grid(row=0, column=7, padx=1)

        btn_grupo_h = Button(frame,
                             font="Verdana 10 bold",
                             text="MENU PRINCIPAL",
                             bd=0,
                             padx=2,
                             pady=2,
                             bg="#405E38",
                             fg="white",
                             command=lambda: quit(janela2))
        btn_grupo_h.grid(row=0, column=8, padx=1)

        # Frame de Dados dos Grupos
        frame = Frame(janela2, bg="white")
        frame.grid_anchor(CENTER)
        frame.place(relx=0.05, rely=0.10, relwidth=0.9, relheight=0.42)

        # Frame da Tabela dos Grupos
        frame_grupos = Frame(janela2, bg="white")
        frame_grupos.grid_anchor(CENTER)
        frame_grupos.place(relx=0.05, rely=0.55, relwidth=0.9, relheight=0.42)

        label_pergunta = Label(frame_grupos,
                               text="TABELA DO GRUPO",
                               font="Verdana 12 bold",
                               bg="white",
                               fg="#405E38",
                               padx=5,
                               pady=5,
                               height=1,
                               justify=LEFT)
        label_pergunta.place(relx=0.35, rely=0.03, relwidth=0.3)

        frame_grupos.grid_configure(relx=0.05, rely=0.15)

        janela2.mainloop()

if __name__ == "__main__":
    a = Grupo()
    a.formando_grupos()
