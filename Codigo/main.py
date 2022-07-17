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
from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk
import pygame
import random

from Codigo.Quiz import Quiz
from Grupo import Grupo
from DataSet import DataSet
from Atualizacao import *


# ----------------------------------------------------------------------------------------------------------------------
# FUNÇOES AUXILIARES COMUNS A TODAS AS JANELAS
def quit(uma):
    uma.destroy()


# ----------------------------------------------------------------------------------------------------------------------
# JANELAS
def janela_grupos():
    # Inicia o DataSet recuperando os jogos
    data = DataSet()
    lista = data.recuperando_jogos_str(a.grupo_nome.get())

    # ------------------------------------------------------------------------------------------------------------------
    # Funções auxiliares

    # Função que verifica se as informações dos placares são consistentes
    def tratamento_dados(valor):
        # Verifica valores de entrada
        if valor.isdigit() and valor != '' and int(valor) >= 0:
            return int(valor)
        elif valor == '':
            return -1
        else:
            messagebox.showerror("ERRO", "Por favor, digite somente valores inteiros maiores"
                                         " ou iguais a zero.", parent=janela2)
            return -1

    # Função que exibe uma caixa de informações de ajuda para orientar o usuário.
    def ajuda():
        messagebox.showinfo("AJUDA", "Para utilizar o programa, esteja atento aos seguintes tópicos:\na) os "
                                     "resultados somente serão salvos se a tabela for atualizada.\nb) os placares "
                                     "somente aceitam valores de números inteiros maiores ou iguais a zero.")

    # Função atualizar tabela realiza a gravação dos resultados inseridos pelo usuário e atualiza  a tabela do grupo.
    def atualizar_tabela():
        resultados = [[tratamento_dados(resultado11.get()), tratamento_dados(resultado12.get())],
                      [tratamento_dados(resultado21.get()), tratamento_dados(resultado22.get())],
                      [tratamento_dados(resultado31.get()), tratamento_dados(resultado32.get())],
                      [tratamento_dados(resultado41.get()), tratamento_dados(resultado42.get())],
                      [tratamento_dados(resultado51.get()), tratamento_dados(resultado52.get())],
                      [tratamento_dados(resultado61.get()), tratamento_dados(resultado62.get())]]

        data.salvando_grupo(a.grupo_nome.get(), resultados)
        grupo = data.recuperando_grupos(a.grupo_nome.get())
        grupo.atualizar(a)

    # Modifica o Grupo em exibição mostrando os dados do grupo clicado
    def alterar_grupo(novo):

        # Acessa um novo agrupo e recupera os placares para atualização
        novo_grupo = Grupo(novo)
        novo_grupo.atualizar(a)
        lista = data.recuperando_jogos_str(a.grupo_nome.get())

        # Recuperando valores para as caixas de entrada dos placares
        resultado11.delete(0)
        resultado11.insert(0, lista[0][0])

        resultado12.delete(0)
        resultado12.insert(0, lista[0][1])

        resultado21.delete(0)
        resultado21.insert(0, lista[1][0])

        resultado22.delete(0)
        resultado22.insert(0, lista[1][1])

        resultado31.delete(0)
        resultado31.insert(0, lista[2][0])

        resultado32.delete(0)
        resultado32.insert(0, lista[2][1])

        resultado41.delete(0)
        resultado41.insert(0, lista[3][0])

        resultado42.delete(0)
        resultado42.insert(0, lista[3][1])

        resultado51.delete(0)
        resultado51.insert(0, lista[4][0])

        resultado52.delete(0)
        resultado52.insert(0, lista[4][1])

        resultado61.delete(0)
        resultado61.insert(0, lista[5][1])

        resultado62.delete(0)
        resultado62.insert(0, lista[5][1])

        # Para recuperar imagens dinamicamente, é necessário o seguinte código
        img1 = ImageTk.PhotoImage(Image.open(a.s1_bandeira.get()).resize((50, 30)))
        lbl1.configure(image=img1)
        lbl1.image = img1

        img2 = ImageTk.PhotoImage(Image.open(a.s2_bandeira.get()).resize((50, 30)))
        lbl2.configure(image=img2)
        lbl2.image = img2

        img3 = ImageTk.PhotoImage(Image.open(a.s3_bandeira.get()).resize((50, 30)))
        lbl3.configure(image=img3)
        lbl3.image = img3

        img4 = ImageTk.PhotoImage(Image.open(a.s4_bandeira.get()).resize((50, 30)))
        lbl4.configure(image=img4)
        lbl4.image = img4

        img5 = ImageTk.PhotoImage(Image.open(a.s1_bandeira.get()).resize((50, 30)))
        lbl5.configure(image=img5)
        lbl5.image = img5

        img6 = ImageTk.PhotoImage(Image.open(a.s3_bandeira.get()).resize((50, 30)))
        lbl6.configure(image=img6)
        lbl6.image = img6

        img7 = ImageTk.PhotoImage(Image.open(a.s4_bandeira.get()).resize((50, 30)))
        lbl7.configure(image=img7)
        lbl7.image = img7

        img8 = ImageTk.PhotoImage(Image.open(a.s2_bandeira.get()).resize((50, 30)))
        lbl8.configure(image=img8)
        lbl8.image = img8

        img9 = ImageTk.PhotoImage(Image.open(a.s4_bandeira.get()).resize((50, 30)))
        lbl9.configure(image=img9)
        lbl9.image = img9

        img10 = ImageTk.PhotoImage(Image.open(a.s1_bandeira.get()).resize((50, 30)))
        lbl10.configure(image=img10)
        lbl10.image = img10

        img11 = ImageTk.PhotoImage(Image.open(a.s2_bandeira.get()).resize((50, 30)))
        lbl11.configure(image=img11)
        lbl11.image = img11

        img12 = ImageTk.PhotoImage(Image.open(a.s3_bandeira.get()).resize((50, 30)))
        lbl12.configure(image=img12)
        lbl12.image = img12

    # -------------------------------------------------------------------------------------------------------------------
    # Cria a janela de Fase de Grupos
    janela2 = Toplevel()
    janela2.title("SHOW DE BOLA - QUIZZ")
    janela2.configure(background='#405E38')
    janela2.geometry("800x500+200+200")
    janela2.transient(janela)
    janela2.focus_force()
    janela2.grab_set()
    janela2.resizable(False, False)

    # Personaliza o background
    bg = ImageTk.PhotoImage(Image.open('imagens/campo.png').resize((800, 500)))
    canvas = Canvas(janela2, width=800, height=600)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg, anchor="nw")

    # Serão três frames longos: frame superior, jogos e tabela
    # -------------------------------------------------------------------------------------------------------------------
    # Frame de Grupos (Recebe os botões para alterar os grupos exibidos no frame jogos)
    frame = Frame(janela2, bg="white")
    frame.grid_anchor(CENTER)
    frame.place(relx=0.05, rely=0.01, relwidth=0.9, relheight=0.07)

    # Códigos acerca dos Botões dos Grupos-----------------------------------

    # Criação dos objetos Botões que serão posicionados no frame
    btn_grupo_a = Button(frame, font="Verdana 10 bold", text="Grupo A", bd=0, padx=2, pady=2, bg="#405E38", fg="white",
                         command=lambda: alterar_grupo('Grupo A'))
    btn_grupo_b = Button(frame, font="Verdana 10 bold", text="Grupo B", bd=0, padx=2, pady=2, bg="#405E38", fg="white",
                         command=lambda: alterar_grupo('Grupo B'))
    btn_grupo_c = Button(frame, font="Verdana 10 bold", text="Grupo C", bd=0, padx=2, pady=2, bg="#405E38", fg="white",
                         command=lambda: alterar_grupo('Grupo C'))
    btn_grupo_d = Button(frame, font="Verdana 10 bold", text="Grupo D", bd=0, padx=2, pady=2, bg="#405E38", fg="white",
                         command=lambda: alterar_grupo('Grupo D'))
    btn_grupo_e = Button(frame, font="Verdana 10 bold", text="Grupo E", bd=0, padx=2, pady=2, bg="#405E38", fg="white",
                         command=lambda: alterar_grupo('Grupo E'))
    btn_grupo_f = Button(frame, font="Verdana 10 bold", text="Grupo F", bd=0, padx=2, pady=2, bg="#405E38", fg="white",
                         command=lambda: alterar_grupo('Grupo F'))
    btn_grupo_g = Button(frame, font="Verdana 10 bold", text="Grupo G", bd=0, padx=2, pady=2, bg="#405E38", fg="white",
                         command=lambda: alterar_grupo('Grupo G'))
    btn_grupo_h = Button(frame, font="Verdana 10 bold", text="Grupo H", bd=0, padx=2, pady=2, bg="#405E38", fg="white",
                         command=lambda: alterar_grupo('Grupo H'))
    btn_retornar = Button(frame, font="Verdana 10 bold", text="MENU PRINCIPAL", bd=0, padx=2, pady=2, bg="#405E38",
                          fg="white", command=lambda: quit(janela2))

    # Posicionamento dos objetos na tela utilizando a formatação grid
    btn_grupo_a.grid(row=0, column=0, padx=1)
    btn_grupo_b.grid(row=0, column=1, padx=1)
    btn_grupo_c.grid(row=0, column=2, padx=1)
    btn_grupo_d.grid(row=0, column=3, padx=1)
    btn_grupo_e.grid(row=0, column=4, padx=1)
    btn_grupo_f.grid(row=0, column=5, padx=1)
    btn_grupo_g.grid(row=0, column=6, padx=1)
    btn_grupo_h.grid(row=0, column=7, padx=1)
    btn_retornar.grid(row=0, column=8, padx=1)

    # ------------------------------------------------------------------------------------------------------------------
    # Frame de jogos (Exibe os dados dos jogos armazenados)

    # Criação do frame com características personalizadas
    jogos = Frame(janela2, bg="white")
    jogos.grid_anchor(CENTER)
    jogos.place(relx=0.05, rely=0.10, relwidth=0.9, relheight=0.55)

    # Label que exibe o nome do Grupo
    Label(jogos, padx=2, justify=CENTER, textvariable=a.grupo_nome, font="Verdana 12 bold", bg="white",
          fg="#405E38", ).grid(row=0, column=0, columnspan=7, padx=2)

    # Cada linha existente no frame representa um jogo e utiliza os seguintes widgets para exibir informações:
    #   Label: informar nome da seleção 1
    #   Label de Imagem: informar bandeira do time 1
    #   Entry: caixa de entrada para informar primeiro valor do placar
    #   Label: informa o valor 'X'
    #   Entry: caixa de entrada para informar segundo valor do placar
    #   Label de Imagem: informar bandeira do time 2
    #   Label: informar nome da seleção 2
    # Observações:
    #   -> As informações do frame são dinâmicas (imagens e strings que podem ser alteradas pelas ações do usuário).
    #     Por isso, não há forma elegante de escrever o código dessa parte.
    #   -> Somente o primeiro jogo será comentado. Os demais identicamente estruturados.

    # Primeiro jogo-----------------------------------------------------------------------------------------------------
    # Recupera valores das imagens
    img1 = ImageTk.PhotoImage(Image.open(a.s1_bandeira.get()).resize((50, 30)))
    img2 = ImageTk.PhotoImage(Image.open(a.s2_bandeira.get()).resize((50, 30)))

    # Label que exibe o nome da eeleção 1 (possui propriedades dinâmicas)
    Label(jogos, bg='white', textvariable=a.s1_nome, padx=2, justify=RIGHT, font="Verdana 10 bold").grid(row=1,
                                                                                                         column=0,
                                                                                                         padx=2)

    # Criação de um objeto label de imagem dinâmica para exibir a bandeira da seleção 1
    lbl1 = Label(jogos, bg='white', width=60, justify=LEFT)
    lbl1.configure(image=img1)
    lbl1.image = img1
    lbl1.grid(row=1, column=1)

    # Cria um objeto resultado11 e exibe uma caixa de entrada para a primeira informação do placar
    resultado11 = Entry(jogos, bg='white', width=3)
    resultado11.grid(row=1, column=2, ipadx=2)

    # Widget que exibe o 'X' entre os dois times
    Label(jogos, bg='white', width=2, text='X').grid(row=1, column=3)

    # Cria um objeto resultado12 e exibe uma caixa de entrada para a segunda informação do placar
    resultado12 = Entry(jogos, bg='white', width=3)
    resultado12.grid(row=1, column=4, ipadx=2)

    # Criação de um objeto label de imagem dinâmica para exibir a bandeira da seleção 2
    lbl2 = Label(jogos, bg='white', width=60, justify=RIGHT, image=img2)
    lbl2.configure(image=img2)
    lbl2.image = img2
    lbl2.grid(row=1, column=5)

    # Label que exibe o nome da seleção 2 (possui propriedades dinâmicas)
    Label(jogos, bg='white', textvariable=a.s2_nome, padx=5, justify=LEFT, font="Verdana 10 bold").grid(row=1, column=6,
                                                                                                        padx=2)

    # Segundo jogo------------------------------------------------------------------------------------------------------
    linha2 = 2
    img3 = ImageTk.PhotoImage(Image.open(a.s3_bandeira.get()).resize((50, 30)))
    img4 = ImageTk.PhotoImage(Image.open(a.s4_bandeira.get()).resize((50, 30)))
    Label(jogos, bg='white', textvariable=a.s3_nome, padx=2, justify=RIGHT, font="Verdana 10 bold").grid(row=linha2,
                                                                                                         column=0,
                                                                                                         padx=2)
    lbl3 = Label(jogos, bg='white', width=60, justify=LEFT)
    lbl3.configure(image=img3)
    lbl3.image = img3
    lbl3.grid(row=linha2, column=1)
    resultado21 = Entry(jogos, bg='white', width=3)
    resultado21.grid(row=linha2, column=2, ipadx=2)
    Label(jogos, bg='white', width=2, text='X').grid(row=linha2, column=3)
    resultado22 = Entry(jogos, bg='white', width=3)
    resultado22.grid(row=linha2, column=4, ipadx=2)
    lbl4 = Label(jogos, bg='white', width=60, justify=RIGHT, image=img4)
    lbl4.configure(image=img4)
    lbl4.image = img4
    lbl4.grid(row=linha2, column=5)
    Label(jogos, bg='white', textvariable=a.s4_nome, padx=5, justify=LEFT, font="Verdana 10 bold").grid(row=linha2,
                                                                                                        column=6,
                                                                                                        padx=2)

    # Terceiro jogo-----------------------------------------------------------------------------------------------------
    linha3 = 3
    img5 = ImageTk.PhotoImage(Image.open(a.s1_bandeira.get()).resize((50, 30)))
    img6 = ImageTk.PhotoImage(Image.open(a.s3_bandeira.get()).resize((50, 30)))
    Label(jogos, bg='white', textvariable=a.s1_nome, padx=2, justify=RIGHT, font="Verdana 10 bold").grid(row=linha3,
                                                                                                         column=0,
                                                                                                         padx=2)
    lbl5 = Label(jogos, bg='white', width=60, justify=LEFT)
    lbl5.configure(image=img5)
    lbl5.image = img5
    lbl5.grid(row=linha3, column=1)
    resultado31 = Entry(jogos, bg='white', width=3)
    resultado31.grid(row=linha3, column=2, ipadx=2)
    Label(jogos, bg='white', width=2, text='X').grid(row=linha3, column=3)
    resultado32 = Entry(jogos, bg='white', width=3)
    resultado32.grid(row=linha3, column=4, ipadx=2)
    lbl6 = Label(jogos, bg='white', width=60, justify=RIGHT)
    lbl6.configure(image=img6)
    lbl6.image = img6
    lbl6.grid(row=linha3, column=5)
    Label(jogos, bg='white', textvariable=a.s3_nome, padx=5, justify=LEFT, font="Verdana 10 bold").grid(row=linha3,
                                                                                                        column=6,
                                                                                                        padx=2)

    # Quarto jogo-------------------------------------------------------------------------------------------------------
    linha4 = 4
    img7 = ImageTk.PhotoImage(Image.open(a.s4_bandeira.get()).resize((50, 30)))
    img8 = ImageTk.PhotoImage(Image.open(a.s2_bandeira.get()).resize((50, 30)))
    Label(jogos, bg='white', textvariable=a.s4_nome, padx=2, justify=RIGHT, font="Verdana 10 bold").grid(row=linha4,
                                                                                                         column=0,
                                                                                                         padx=2)
    lbl7 = Label(jogos, bg='white', width=60, justify=LEFT)
    lbl7.configure(image=img7)
    lbl7.image = img7
    lbl7.grid(row=linha4, column=1)
    resultado41 = Entry(jogos, bg='white', width=3)
    resultado41.grid(row=linha4, column=2, ipadx=2)
    Label(jogos, bg='white', width=2, text='X').grid(row=linha4, column=3)
    resultado42 = Entry(jogos, bg='white', width=3)
    resultado42.grid(row=linha4, column=4, ipadx=2)
    lbl8 = Label(jogos, bg='white', width=60, justify=RIGHT)
    lbl8.configure(image=img8)
    lbl8.image = img8
    lbl8.grid(row=linha4, column=5)
    Label(jogos, bg='white', textvariable=a.s2_nome, padx=5, justify=LEFT, font="Verdana 10 bold").grid(row=linha4,
                                                                                                        column=6,
                                                                                                        padx=2)

    # Quinto jogo ------------------------------------------------------------------------------------------------------
    linha5 = 5
    img9 = ImageTk.PhotoImage(Image.open(a.s4_bandeira.get()).resize((50, 30)))
    img10 = ImageTk.PhotoImage(Image.open(a.s1_bandeira.get()).resize((50, 30)))
    Label(jogos, bg='white', textvariable=a.s4_nome, padx=2, justify=RIGHT, font="Verdana 10 bold").grid(row=linha5,
                                                                                                         column=0,
                                                                                                         padx=2)
    lbl9 = Label(jogos, bg='white', width=60, justify=LEFT)
    lbl9.configure(image=img9)
    lbl9.image = img9
    lbl9.grid(row=linha5, column=1)
    resultado51 = Entry(jogos, bg='white', width=3)
    resultado51.grid(row=linha5, column=2, ipadx=2)
    Label(jogos, bg='white', width=2, text='X').grid(row=linha5, column=3)
    resultado52 = Entry(jogos, bg='white', width=3)
    resultado52.grid(row=linha5, column=4, ipadx=2)
    lbl10 = Label(jogos, bg='white', width=60, justify=RIGHT)
    lbl10.configure(image=img10)
    lbl10.image = img10
    lbl10.grid(row=linha5, column=5)
    Label(jogos, bg='white', textvariable=a.s1_nome, padx=5, justify=LEFT, font="Verdana 10 bold").grid(row=linha5,
                                                                                                        column=6,
                                                                                                        padx=2)

    # Sexto jogo--------------------------------------------------------------------------------------------------------
    linha6 = 6
    img11 = ImageTk.PhotoImage(Image.open(a.s2_bandeira.get()).resize((50, 30)))
    img12 = ImageTk.PhotoImage(Image.open(a.s3_bandeira.get()).resize((50, 30)))
    Label(jogos, bg='white', textvariable=a.s2_nome, padx=2, justify=RIGHT, font="Verdana 10 bold").grid(row=linha6,
                                                                                                         column=0,
                                                                                                         padx=2)
    lbl11 = Label(jogos, bg='white', width=60, justify=LEFT)
    lbl11.configure(image=img11)
    lbl11.image = img11
    lbl11.grid(row=linha6, column=1)
    resultado61 = Entry(jogos, bg='white', width=3)
    resultado61.grid(row=linha6, column=2, ipadx=2)
    Label(jogos, bg='white', width=2, text='X').grid(row=linha6, column=3)
    resultado62 = Entry(jogos, bg='white', width=3)
    resultado62.grid(row=linha6, column=4, ipadx=2)
    lbl12 = Label(jogos, bg='white', width=60, justify=RIGHT)
    lbl12.configure(image=img12)
    lbl12.image = img12
    lbl12.grid(row=linha6, column=5)
    Label(jogos, bg='white', textvariable=a.s3_nome, padx=5, justify=LEFT, font="Verdana 10 bold").grid(row=linha6,
                                                                                                        column=6,
                                                                                                        padx=2)
    # LINHA EM BRANCO --------------------------------------------------------------------------------------------------
    Label(jogos, bg='white').grid(row=7, column=6, padx=2)

    # Salvar informações -----------------------------------------------------------------------------------------------
    btn_salvar = Button(jogos, font="Verdana 10 bold", text="ATUALIZAR TABELA", bd=0, padx=2, pady=2, bg="#405E38",
                        fg="white", command=atualizar_tabela)
    btn_salvar.grid(row=8, column=1, columnspan=3, padx=1)
    # Ajuda
    btn_ajuda = Button(jogos, font="Verdana 10 bold", text="AJUDA", bd=0, padx=2, pady=2, bg="#405E38", fg="white",
                       command=ajuda)
    btn_ajuda.grid(row=8, column=4, columnspan=2, padx=1)

    # Recupera valores para preenchimento dos placares
    resultado11.insert(0, lista[0][0])
    resultado12.insert(0, lista[0][1])
    resultado21.insert(0, lista[1][0])
    resultado22.insert(0, lista[1][1])
    resultado31.insert(0, lista[2][0])
    resultado32.insert(0, lista[2][1])
    resultado41.insert(0, lista[3][0])
    resultado42.insert(0, lista[3][1])
    resultado51.insert(0, lista[4][0])
    resultado52.insert(0, lista[4][1])
    resultado61.insert(0, lista[5][1])
    resultado62.insert(0, lista[5][1])

    # ------------------------------------------------------------------------------------------------------------------
    # Frame da Tabela dos Grupos (exibe estatísticas e posicionamento das seleções dentro do grupo)

    # Criação do frame com suas características
    frame_grupos = Frame(janela2, bg="white")
    frame_grupos.grid_anchor(CENTER)
    frame_grupos.place(relx=0.05, rely=0.67, relwidth=0.9, relheight=0.30)

    # Título do Frame
    Label(frame_grupos, text="TABELA DO GRUPO", font="Verdana 12 bold", bg="white", fg="#405E38", padx=5, pady=5,
          height=1, justify=LEFT).grid(row=0, column=0, columnspan=8)

    # Primeira Linha da Tabela de Jogos - Cabeçalho
    Label(frame_grupos, bg="#405E38", fg='white', text='Classificação', width=30, padx=2, justify=LEFT,
          font="Verdana 9 bold").grid(row=1, column=1)
    Label(frame_grupos, bg="#405E38", fg='white', text='P', width=6, padx=2, justify=LEFT, font="Verdana 9 bold").grid(
        row=1, column=2)
    Label(frame_grupos, bg="#405E38", fg='white', text='V', width=6, padx=2, justify=LEFT, font="Verdana 9 bold").grid(
        row=1, column=3)
    Label(frame_grupos, bg="#405E38", fg='white', text='E', width=6, padx=2, justify=LEFT, font="Verdana 9 bold").grid(
        row=1, column=4)
    Label(frame_grupos, bg="#405E38", fg='white', text='D', width=6, padx=2, justify=LEFT, font="Verdana 9 bold").grid(
        row=1, column=5)
    Label(frame_grupos, bg="#405E38", fg='white', text='GP', width=6, padx=2, justify=LEFT, font="Verdana 9 bold").grid(
        row=1, column=6)
    Label(frame_grupos, bg="#405E38", fg='white', text='GC', width=6, padx=2, justify=LEFT, font="Verdana 9 bold").grid(
        row=1, column=7)
    Label(frame_grupos, bg="#405E38", fg='white', text='SG', width=6, padx=2, justify=LEFT, font="Verdana 9 bold").grid(
        row=1, column=8)

    # Montando a Coluna 0 (informa a classificação)
    Label(frame_grupos, bg="#405E38", fg='white', textvariable=a.s1_colocacao, width=3, padx=2, justify=LEFT,
          font="Verdana 8 bold").grid(row=2, column=0, padx=2)
    Label(frame_grupos, bg="#405E38", fg='white', textvariable=a.s2_colocacao, width=3, padx=2, justify=LEFT,
          font="Verdana 8 bold").grid(row=3, column=0, padx=2)
    Label(frame_grupos, bg="#405E38", fg='white', textvariable=a.s3_colocacao, width=3, padx=2, justify=LEFT,
          font="Verdana 8 bold").grid(row=4, column=0, padx=2)
    Label(frame_grupos, bg="#405E38", fg='white', textvariable=a.s4_colocacao, width=3, padx=2, justify=LEFT,
          font="Verdana 8 bold").grid(row=5, column=0, padx=2)

    # Dados da Primeira Seleção
    Label(frame_grupos, bg='white', fg='black', textvariable=a.s1_nome, width=30, padx=2, justify=LEFT,
          font="Verdana 9 bold").grid(row=2, column=1)
    Label(frame_grupos, bg='white', fg='black', textvariable=a.s1_pontos, width=6, padx=2, justify=LEFT,
          font="Verdana 9 bold").grid(row=2, column=2)
    Label(frame_grupos, bg='white', fg='black', textvariable=a.s1_vitorias, width=6, padx=2, justify=LEFT,
          font="Verdana 9 bold").grid(row=2, column=3)
    Label(frame_grupos, bg='white', fg='black', textvariable=a.s1_empates, width=6, padx=2, justify=LEFT,
          font="Verdana 9 bold").grid(row=2, column=4)
    Label(frame_grupos, bg='white', fg='black', textvariable=a.s1_derrotas, width=6, padx=2, justify=LEFT,
          font="Verdana 9 bold").grid(row=2, column=5)
    Label(frame_grupos, bg='white', fg='black', textvariable=a.s1_gols_favoraveis, width=6, padx=2, justify=LEFT,
          font="Verdana 9 bold").grid(row=2, column=6)
    Label(frame_grupos, bg='white', fg='black', textvariable=a.s1_gols_contrarios, width=6, padx=2, justify=LEFT,
          font="Verdana 9 bold").grid(row=2, column=7)
    Label(frame_grupos, bg='white', fg='black', textvariable=a.s1_saldo_gols, width=6, padx=2, justify=LEFT,
          font="Verdana 9 bold").grid(row=2, column=8)

    # Dados da Segunda Seleção
    Label(frame_grupos, bg='white', fg='black', textvariable=a.s2_nome, width=30, padx=2, justify=LEFT,
          font="Verdana 9 bold").grid(row=3, column=1)
    Label(frame_grupos, bg='white', fg='black', textvariable=a.s2_pontos, width=6, padx=2, justify=LEFT,
          font="Verdana 9 bold").grid(row=3, column=2)
    Label(frame_grupos, bg='white', fg='black', textvariable=a.s2_vitorias, width=6, padx=2, justify=LEFT,
          font="Verdana 9 bold").grid(row=3, column=3)
    Label(frame_grupos, bg='white', fg='black', textvariable=a.s2_empates, width=6, padx=2, justify=LEFT,
          font="Verdana 9 bold").grid(row=3, column=4)
    Label(frame_grupos, bg='white', fg='black', textvariable=a.s2_derrotas, width=6, padx=2, justify=LEFT,
          font="Verdana 9 bold").grid(row=3, column=5)
    Label(frame_grupos, bg='white', fg='black', textvariable=a.s2_gols_favoraveis, width=6, padx=2, justify=LEFT,
          font="Verdana 9 bold").grid(row=3, column=6)
    Label(frame_grupos, bg='white', fg='black', textvariable=a.s2_gols_contrarios, width=6, padx=2, justify=LEFT,
          font="Verdana 9 bold").grid(row=3, column=7)
    Label(frame_grupos, bg='white', fg='black', textvariable=a.s2_saldo_gols, width=6, padx=2, justify=LEFT,
          font="Verdana 9 bold").grid(row=3, column=8)

    # Dados da Terceira Seleção
    Label(frame_grupos, bg='white', fg='black', textvariable=a.s3_nome, width=30, padx=2, justify=LEFT,
          font="Verdana 9 bold").grid(row=4, column=1)
    Label(frame_grupos, bg='white', fg='black', textvariable=a.s3_pontos, width=6, padx=2, justify=LEFT,
          font="Verdana 9 bold").grid(row=4, column=2)
    Label(frame_grupos, bg='white', fg='black', textvariable=a.s3_vitorias, width=6, padx=2, justify=LEFT,
          font="Verdana 9 bold").grid(row=4, column=3)
    Label(frame_grupos, bg='white', fg='black', textvariable=a.s3_empates, width=6, padx=2, justify=LEFT,
          font="Verdana 9 bold").grid(row=4, column=4)
    Label(frame_grupos, bg='white', fg='black', textvariable=a.s3_derrotas, width=6, padx=2, justify=LEFT,
          font="Verdana 9 bold").grid(row=4, column=5)
    Label(frame_grupos, bg='white', fg='black', textvariable=a.s3_gols_favoraveis, width=6, padx=2, justify=LEFT,
          font="Verdana 9 bold").grid(row=4, column=6)
    Label(frame_grupos, bg='white', fg='black', textvariable=a.s3_gols_contrarios, width=6, padx=2, justify=LEFT,
          font="Verdana 9 bold").grid(row=4, column=7)
    Label(frame_grupos, bg='white', fg='black', textvariable=a.s3_saldo_gols, width=6, padx=2, justify=LEFT,
          font="Verdana 9 bold").grid(row=4, column=8)

    # Dados da Quarta Seleção
    Label(frame_grupos, bg='white', fg='black', textvariable=a.s4_nome, width=30, padx=2, justify=LEFT,
          font="Verdana 9 bold").grid(row=5, column=1)
    Label(frame_grupos, bg='white', fg='black', textvariable=a.s4_pontos, width=6, padx=2, justify=LEFT,
          font="Verdana 9 bold").grid(row=5, column=2)
    Label(frame_grupos, bg='white', fg='black', textvariable=a.s4_vitorias, width=6, padx=2, justify=LEFT,
          font="Verdana 9 bold").grid(row=5, column=3)
    Label(frame_grupos, bg='white', fg='black', textvariable=a.s4_empates, width=6, padx=2, justify=LEFT,
          font="Verdana 9 bold").grid(row=5, column=4)
    Label(frame_grupos, bg='white', fg='black', textvariable=a.s4_derrotas, width=6, padx=2, justify=LEFT,
          font="Verdana 9 bold").grid(row=5, column=5)
    Label(frame_grupos, bg='white', fg='black', textvariable=a.s4_gols_favoraveis, width=6, padx=2, justify=LEFT,
          font="Verdana 9 bold").grid(row=5, column=6)
    Label(frame_grupos, bg='white', fg='black', textvariable=a.s4_gols_contrarios, width=6, padx=2, justify=LEFT,
          font="Verdana 9 bold").grid(row=5, column=7)
    Label(frame_grupos, bg='white', fg='black', textvariable=a.s4_saldo_gols, width=6, padx=2, justify=LEFT,
          font="Verdana 9 bold").grid(row=5, column=8)

    janela2.mainloop()


def janela_quizz():
    # Essa função verifica se a resposta corresponde ao gabarito
    def verificar_resposta(resposta):

        # Verifica igualdade
        if str(resposta.get()) == str(gabarito.get()):
            pontuacao.set(str(int(pontuacao.get()) + 10))

        # Desabilita botão de verificar
        btn_verificar_resposta.configure(state=DISABLED)

    # Função que atualiza informações para próxima pergunta
    def proxima_pergunta():

        # Coleta a próxima pergunta
        prox = quizz.proxima_pergunta()

        # Caso as perguntas se esgotem, desabilita o botão de próxima pergunta
        if len(quizz.perguntas) == 0:
            btn_avancar.configure(state=DISABLED)

        # Ativa o botão de verificar o gabarito
        btn_verificar_resposta.configure(state=ACTIVE)

        # Atualiza novos valores
        questao.set(prox.get_questao())
        resposta1.set(prox.get_resposta1())
        resposta2.set(prox.get_resposta2())
        resposta3.set(prox.get_resposta3())
        resposta4.set(prox.get_resposta4())
        gabarito.set(prox.get_gabarito())

        # Atualiza radiobuttons
        radiobtn1.configure(value=resposta1.get())
        radiobtn1.value = resposta1.get()
        radiobtn2.configure(value=resposta2.get())
        radiobtn2.value = resposta2.get()
        radiobtn3.configure(value=resposta3.get())
        radiobtn3.value = resposta3.get()
        radiobtn4.configure(value=resposta4.get())
        radiobtn4.value = resposta4.get()

        # Desmarca todos os botões
        radiobtn1.deselect()
        radiobtn2.deselect()
        radiobtn3.deselect()
        radiobtn4.deselect()

        janela2.mainloop()

    # Cria um objeto quizz
    quizz = Quiz()

    # Seleciona uma pergunta para ser usada no contexto do aplicativo
    pergunta = quizz.proxima_pergunta()

    # Cria a janela de exibição do Quizz.
    janela2 = Toplevel()
    janela2.title("SHOW DE BOLA - QUIZZ")
    janela2.configure(background='#4A2A2D')
    janela2.geometry("800x400+200+200")
    janela2.transient(janela)
    janela2.focus_force()
    janela2.grab_set()
    janela2.resizable(False, False)

    # Declarando variáveis dinâmicas
    var = StringVar()
    questao = StringVar()
    resposta1 = StringVar()
    resposta2 = StringVar()
    resposta3 = StringVar()
    resposta4 = StringVar()
    gabarito = StringVar()
    pontuacao = StringVar(value="0")

    # Preenchendo variáveis dinâmicas
    questao.set(pergunta.get_questao())
    resposta1.set(pergunta.get_resposta1())
    resposta2.set(pergunta.get_resposta2())
    resposta3.set(pergunta.get_resposta3())
    resposta4.set(pergunta.get_resposta4())
    gabarito.set(pergunta.get_gabarito())

    # Personaliza o background
    bg = ImageTk.PhotoImage(Image.open('imagens/estadio.png').resize((800, 400)))
    canvas = Canvas(janela2, width=800, height=400)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg, anchor="nw")

    # Cria o objeto e exibe o título do corpo da janela
    label_titulo = Label(janela2, text="QUIZZ", font="Verdana 20 bold", bg="#0E0405", fg="#911724")
    label_titulo.place(anchor=N, rely=0.05, relx=0.5, relwidth=0.9)

    # ------------------------------------------------------------------------------------------------------------------
    # FRAME DO QUIZZ (ONDE SERÃO POSICIONADAS AS PERGUNTAS E RESPOSTAS)
    frame_quiz = Frame(janela2, bg="#0E0405")
    frame_quiz.grid_anchor(CENTER)
    frame_quiz.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.6)

    # PORÇÃO QUE INDICA A QUESTÃO --------------------------------------------------------------------------------------

    # Criação dos objetos Label (um que exibe a palavra "PERGUNTA" e outro que exibe a questão)
    label_pergunta = Label(frame_quiz, text="PERGUNTA:", font="Verdana 14 bold", bg="#0E0405", fg="#911724", padx=5,
                           pady=5, height=2, justify=LEFT)
    label_questao = Label(frame_quiz, textvariable=questao, font="Verdana 10 bold", bg="#0E0405", fg="white", height=4,
                          justify=LEFT, wraplength=500)

    # Posiciona os dois labels na linha 0 do Grid.
    label_pergunta.grid(row=0, column=0, sticky=E)
    label_questao.grid(row=0, column=1, sticky=W)

    # OPCAO 1 ----------------------------------------------------------------------------------------------------------

    # Criação dos objetos do radiobutton e do label de respostas
    radiobtn1 = Radiobutton(frame_quiz, variable=var, bd=0, padx=0, pady=0, bg="#0E0405", value=resposta1.get())
    label_resposta1 = Label(frame_quiz, textvariable=resposta1, font="Verdana 10 bold", bg="#0E0405", fg="white",
                            wraplength=400)

    # Posicionamento dos objetos no grid
    radiobtn1.grid(row=1, column=0, sticky=E)
    label_resposta1.grid(row=1, column=1, sticky=W)

    # OPCAO 2 ----------------------------------------------------------------------------------------------------------

    # Criação dos objetos do radiobutton e do label de respostas
    radiobtn2 = Radiobutton(frame_quiz, variable=var, bd=0, padx=0, pady=0, bg="#0E0405", value=resposta2.get())
    label_resposta2 = Label(frame_quiz, textvariable=resposta2, font="Verdana 10 bold", bg="#0E0405", fg="white",
                            wraplength=400)

    # Posicionamento dos objetos no grid
    radiobtn2.grid(row=2, column=0, sticky=E)
    label_resposta2.grid(row=2, column=1, sticky=W)

    # OPCAO 3 ----------------------------------------------------------------------------------------------------------

    # Criação dos objetos do radiobutton e do label de respostas
    radiobtn3 = Radiobutton(frame_quiz, variable=var, bd=0, padx=0, pady=0, bg="#0E0405", value=resposta3.get())
    label_resposta4 = Label(frame_quiz, textvariable=resposta3, font="Verdana 10 bold", bg="#0E0405", fg="white",
                            wraplength=400)

    # Posicionamento dos objetos no grid
    radiobtn3.grid(row=3, column=0, sticky=E)
    label_resposta4.grid(row=3, column=1, sticky=W)

    # OPCAO 4 ----------------------------------------------------------------------------------------------------------

    # Criação dos objetos do radiobutton e do label de respostas
    radiobtn4 = Radiobutton(frame_quiz, variable=var, bd=0, padx=0, pady=0, bg="#0E0405", value=resposta4.get())
    label_resposta4 = Label(frame_quiz, textvariable=resposta4, font="Verdana 10 bold", bg="#0E0405", fg="white",
                            wraplength=400)

    # Posicionamento dos objetos no grid
    radiobtn4.grid(row=4, column=0, sticky=E)
    label_resposta4.grid(row=4, column=1, sticky=W)

    # BOTÃO DE VERIFICAÇÃO DE RESPOSTAS --------------------------------------------------------------------------------

    btn_verificar_resposta = Button(frame_quiz, font="Verdana 10 bold", text="VERIFICAR RESPOSTA", bd=0, padx=2, pady=2,
                                    bg="#911724", fg="white", command=lambda: verificar_resposta(var))
    btn_verificar_resposta.grid(row=6, columnspan=2, padx=2, pady=10)

    # ------------------------------------------------------------------------------------------------------------------
    # FRAME DO BOTTOM (ONDE SERÃO INDICADAS A PONTUAÇÃO TOTAL, BOTÃO PROXIMA PERGUNTA E BOTÃO RETORNAR AO MENU)
    frame = Frame(janela2, bg="#0E0405")
    frame.grid_anchor(CENTER)
    frame.place(relx=0.05, rely=0.9, relwidth=0.9)

    # Criação dos widgets para formação do frame de rodapé.
    label_pontuacao_str = Label(frame, font="Verdana 8 bold", text="Pontuação total: ", bd=0, padx=1, pady=1, width=20,
                                bg="#0E0405", fg="white", anchor=CENTER)
    label_pontuacao = Label(frame, font="Verdana 8 bold", textvariable=pontuacao, bd=0, padx=1, pady=1, width=10,
                            bg="#0E0405", fg="white", anchor=CENTER)
    btn_avancar = Button(frame, font="Verdana 10 bold", text="PROXIMA PERGUNTA", bd=0, padx=2, pady=2, bg="#911724",
                         fg="white", command=lambda: proxima_pergunta())
    btn_sair = Button(frame, font="Verdana 10 bold", text="RETORNAR MENU", bd=0, padx=2, pady=2, bg="#911724",
                      fg="white", command=lambda: quit(janela2))

    # Posicionamento dos objetos no grid
    label_pontuacao_str.grid(row=0, column=0, padx=5)
    label_pontuacao.grid(row=0, column=1, padx=5)
    btn_avancar.grid(row=0, column=2, padx=2)
    btn_sair.grid(row=0, column=3, padx=2)

    janela2.mainloop()


def janela_vidente():
    # Função para sair da tela desligando a música
    def quit_musica(tela):
        pygame.mixer.music.stop()
        tela.destroy()

    # Caso a pessoa clique no botão de fechar janela, cria um protocolo de
    # encerra a música e fecha a janela.
    def quit_protocol(quitprot):
        pygame.mixer.music.stop()
        quitprot.destroy()

    # Realiza a previsão do vencedor.
    def prever(btn, cx1, cx2, res):
        btn['state'] = DISABLED
        resultado = random.randint(0, 101)
        if resultado > 50:
            res['text'] = cx1.get()
        else:
            res['text'] = cx2.get()
        pygame.mixer.music.stop()

    # Inicializa Música
    pygame.mixer.init()
    pygame.mixer.music.load("musica/misterio.mp3")
    pygame.mixer.music.play(loops=0)

    # Cria a janela do vidente e ajusta padrões
    janela2 = Toplevel()
    janela2.title("SHOW DE BOLA - VIDENTE")
    janela2.configure(background='#ccbca4')
    janela2.geometry("450x400+300+300")
    janela2.transient(janela)
    janela2.focus_force()
    janela2.grab_set()
    janela2.resizable(False, False)

    # Personaliza o background
    bg = ImageTk.PhotoImage(Image.open('imagens/vidente.png').resize((450, 400)))
    canvas = Canvas(janela2, width=450, height=400)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg, anchor="nw")

    # Exibe o título do corpo da janela
    label_titulo = Label(janela2, text="VIDENTE", font="Verdana 20 bold", bg="#9f7c59", fg="#5e3414")
    label_titulo.place(anchor=N, rely=0.05, relx=0.5, relwidth=0.6)

    # Coletando dados do primeiro time
    label_time1 = Label(janela2, text="Digite o primeiro time:", font="Verdana 8 bold", bg="#9f7c59", fg="#5e3414")
    label_time1.place(anchor=N, rely=0.3, relx=0.75, relwidth=0.4)
    caixa1 = Entry(janela2)
    caixa1.place(rely=0.35, relx=0.55, relwidth=0.4)

    # Coletando dados do segundo time
    label_time2 = Label(janela2, text="Digite o segundo time:", font="Verdana 8 bold", bg="#9f7c59", fg="#5e3414")
    label_time2.place(anchor=N, rely=0.42, relx=0.75, relwidth=0.4)
    caixa2 = Entry(janela2)
    caixa2.place(rely=0.47, relx=0.55, relwidth=0.4)

    # Botão de Previsão
    btn_prever = Button(janela2, text="PREVER O FUTURO", bd=0, padx=0, pady=0, bg="#9f7c59", fg="#5e3414",
                        command=lambda: prever(btn_prever, caixa1, caixa2, label_resultado_valor))
    btn_prever.place(relx=0.55, rely=0.56, relwidth=0.4)

    # Porção que indica o resultado (label resultado fica embaixo do label resultado valor: serve para efeito visual)
    label_resultado = Label(janela2, text="RESULTADO: ", font="Verdana 8 bold", bg="#9f7c59", fg="#5e3414")
    label_resultado.place(anchor=N, rely=0.65, relx=0.75, relwidth=0.4)
    label_resultado_valor = Label(janela2, justify=CENTER, anchor=CENTER)
    label_resultado_valor.place(relx=0.55, rely=0.63, relwidth=0.4)

    # Botão retornar
    btn_sair = Button(janela2, text="RETORNAR MENU", bd=0, padx=0, pady=0, bg="#9f7c59", fg="#5e3414",
                      command=lambda: quit_musica(janela2))
    btn_sair.place(relx=0.35, rely=0.85, relwidth=0.3)

    # Ao fechar a janela, utiliza protocolo de saida.
    janela2.protocol("WM_DELETE_WINDOW", lambda: quit_protocol(janela2))
    janela2.mainloop()


def janela_sobre():
    # Cria a janela que expõe informações sobre o programa
    janela2 = Toplevel()
    janela2.title("SHOW DE BOLA - SOBRE")
    janela2.configure(background='#5B7019')
    janela2.geometry("600x300+200+200")
    janela2.transient(janela)
    janela2.focus_force()
    janela2.grab_set()
    janela2.resizable(False, False)

    # Personaliza o background
    bg = ImageTk.PhotoImage(Image.open('imagens/background.png').resize((700, 300)))
    canvas = Canvas(janela2, width=600, height=300)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg, anchor="nw")

    # Texto de informaçoes
    info = """                   UNIVERSIDADE DE SÃO PAULO (USP)

        Programa:
        Programa desenvolvido para cumprimento do Projeto Final
        da disciplina de Programação Orientada a Objetos (POO)
        do professor Márcio Delamaro.

        Alunos:
        Carlos Filipe de Castro Lemos (12542630)
        João Gabriel Sasseron Roberto Amorin (12542564)
        Pedro Henrique Vilela do Nascimento (12803492)
        Pedro Guilherme dos Reis Teixeira (12542477)"""

    # Criação do label para exibir as informações
    informacoes = Label(janela2, anchor=CENTER, justify=LEFT, width=200, bd=1, relief=SOLID, bg="white", fg='black',
                        font="Verdana 8 bold", text=info, padx=10, pady=10)
    informacoes.place(relx=0.05, rely=0.10, relwidth=0.9)

    # Botao de retorno
    btn_sair = Button(janela2, text="RETORNAR MENU", bg='white', fg='black', width=7, height=1, bd=3, relief=SOLID,
                      anchor=CENTER, font="bold", command=lambda: quit(janela2))
    btn_sair.place(relx=0.35, rely=0.85, relwidth=0.3)

    # Montagem dos elementos estáticos
    janela2.mainloop()


# Criação do Grupo Inicial que será usado na opção Grupos
g_inicial = Grupo('GrupoA')

# Criação da Janela do Menu e suas Configurações
janela = Tk()
p1 = PhotoImage(file="imagens/icone.png")
janela.iconphoto(False, p1)
janela.geometry("600x300+300+300")
janela.title("Show de Bola!!")
janela.resizable(False, False)

# Criação de variável de atualização que será usada na opção de grupos
a = Atualizacao(g_inicial)

# Imagem de fundo
bg = ImageTk.PhotoImage(Image.open('imagens/menu.png').resize((800, 300)))
canvas = Canvas(janela, width=700, height=300)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg, anchor="nw")

# Botões do menu (criação de seus objetos)
button1 = Button(janela, text="GRUPOS", bg='white', fg='black', width=7, height=1, bd=3, relief=SOLID, anchor=CENTER,
                 font="bold", command=janela_grupos)
button2 = Button(janela, text="QUIZZ", bg='white', fg='black', width=7, height=1, bd=3, relief=SOLID, anchor=CENTER,
                 font="bold", command=janela_quizz)
button3 = Button(janela, text="VIDENTE", bg='white', fg='black', width=7, height=1, bd=3, relief=SOLID, anchor=CENTER,
                 font="bold", command=janela_vidente)
button4 = Button(janela, text="SOBRE", bg='white', fg='black', width=7, height=1, bd=3, relief=SOLID, anchor=CENTER,
                 font="bold", command=janela_sobre)

# Exibição dos botões na tela
button1_canvas = canvas.create_window(72, 150, anchor="nw", window=button1)
button2_canvas = canvas.create_window(177, 150, anchor="nw", window=button2)
button3_canvas = canvas.create_window(282, 150, anchor="nw", window=button3)
button4_canvas = canvas.create_window(387, 150, anchor="nw", window=button4)

# Mensagem no rodapé do programa
label = Label(janela, font="Verdana 8 bold", text="Copyright ® - Todos os direitos reservados", anchor=S,
              justify=CENTER)
label.place(relx=0.24, rely=0.9, relwidth=0.5)

janela.mainloop()
