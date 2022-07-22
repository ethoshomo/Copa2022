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

OBSERVAÇÃO: todos os alunos participaram de forma equivalente.
"""

from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk
import pygame
import random

#from Codigo.Quiz import Quiz
#from Codigo.FaseFinal import FaseFinal
from FaseFinal import FaseFinal
from Quiz import Quiz
from Grupo import Grupo
from DataSet import DataSet
from atualizacao import *


# ----------------------------------------------------------------------------------------------------------------------
# FUNÇOES AUXILIARES COMUNS A TODAS AS JANELAS
def quit(uma):
    """
    Função que fecha janelas.

    :param uma: Uma janela.
    """
    uma.destroy()


def tratamento_dados(valor):
    """
    Função que verifica se as informações dos placares são consistentes

    :param valor: Valor que será checado.
    """
    # Verifica valores de entrada
    if valor.isdigit() and valor != '' and int(valor) >= 0:
        return int(valor)
    elif valor == '':
        return -1
    else:
        messagebox.showerror("ERRO", "Por favor, digite somente valores inteiros maiores"
                                     " ou iguais a zero.") # parent=janela2
        return -1


# ----------------------------------------------------------------------------------------------------------------------
# JANELAS
def janela_grupos():
    """
    Manipula a janela de grupos, seus dados, estilos, botões e
    funcionamento geral. Nessa janela o usuário pode inserir os
    resultados dos jogos entre as seleções de cada um dos grupos.
    A tabela de colocação e pontuações de cada grupo pode ser
    atualizada de acordo com os dados inseridos ao apertar o botão
    de atualizar, mostrando as vitórias, derrotas, saldo de gol, etc,
    de cada seleção do grupo.
    """
    # Inicia o DataSet recuperando os jogos
    data = DataSet()
    lista = data.recuperando_jogos_str(a.grupo_nome.get())

    # ------------------------------------------------------------------------------------------------------------------
    # Funções auxiliares

    def ajuda():
        """
        Função que exibe uma caixa de informações de ajuda para orientar o usuário.
        """
        messagebox.showinfo("AJUDA", "Para utilizar o programa, esteja atento aos seguintes tópicos:\na) os "
                                     "resultados somente serão salvos se a tabela for atualizada.\nb) os placares "
                                     "somente aceitam valores de números inteiros maiores ou iguais a zero.")

    def atualizar_tabela():
        """
        Função atualizar tabela realiza a gravação dos resultados inseridos pelo
        usuário e atualiza a tabela do grupo.
        """
        resultados = [[tratamento_dados(resultado11.get()), tratamento_dados(resultado12.get())],
                      [tratamento_dados(resultado21.get()), tratamento_dados(resultado22.get())],
                      [tratamento_dados(resultado31.get()), tratamento_dados(resultado32.get())],
                      [tratamento_dados(resultado41.get()), tratamento_dados(resultado42.get())],
                      [tratamento_dados(resultado51.get()), tratamento_dados(resultado52.get())],
                      [tratamento_dados(resultado61.get()), tratamento_dados(resultado62.get())]]

        data.salvando_grupo(a.grupo_nome.get(), resultados)
        grupo = data.recuperando_grupos(a.grupo_nome.get())
        grupo.atualizar(a)

    def alterar_grupo(novo):
        """
        # Modifica o Grupo em exibição mostrando os dados do grupo clicado.

        :param novo:
        """
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
    janela2.title("SHOW DE BOLA - GRUPOS")
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
          fg="#405E38").grid(row=0, column=0, columnspan=7, padx=2)

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

    # Label que exibe o nome da Seleção 1 (possui propriedades dinâmicas)
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


def janela_fase_final():
    """
    Manipula a janela da fase final, seus dados, botões, estilo e
    funcionamento geral. Nessa janela, os vencedores da fase de grupos,
    escolhidos de acordo com o input do usuário na janela de fase de grupos,
    seram escalados em jogos seguindo a lógica oficial da FIFA. O usuário pode
    decidir os gols marcados e os resultados de eventuais desempates por penaltis.
    Essa fase começa nas oitavas de final, mas os vencedores dela progredirão
    para as quartas de final e os vencedores dessa para as semifinais. Por fim,
    as duas seleções vitoriosas prosseguirão para as finais e o usuário poderá decidir
    quem será o vencedor da Copa do Mundo de 2022 e o vencedor da disputa pelo terceiro
    lugar.
    """

    # Função destinada a mostrar informações ao usuário
    def informacoes():
        # Exibe uma janela de mensagens na tela com as informações.
        messagebox.showinfo("INFORMAÇÕES", "Na Fase Final, é importante saber que os dados são atualizados"
                                           " de forma automática, objetivando modificar as próximas fases. Por isso, esteja"
                                           " atento nas alterações dos resultados anteriores (por exemplo, modificar dados"
                                           " das oitavas quando já se tem dados da quartas e das semifinais), pois sua "
                                           " atualização implicará no apagamento das informações posteriores (quartas de"
                                           " finais e semifinais). Além disso, caso haja erros de informações, é "
                                           "possível corrigir os equívocos, ressaltando-se as observações acima.")


    # Salva o resultado das oitavas (lembrando que pode acontecer empate que é resolvido por penaltis).
    def salvar_oitavas():
        """

        :return:
        """

        #criação de uma lista com dados devidamente tratados que serão salvos no banco de dados.
        resul_oitavas = [[tratamento_dados(oitavas11.get()), tratamento_dados(oitavas12.get()), -1, -1],
                         [tratamento_dados(oitavas21.get()), tratamento_dados(oitavas22.get()), -1, -1],
                         [tratamento_dados(oitavas31.get()), tratamento_dados(oitavas32.get()), -1, -1],
                         [tratamento_dados(oitavas41.get()), tratamento_dados(oitavas42.get()), -1, -1],
                         [tratamento_dados(oitavas51.get()), tratamento_dados(oitavas52.get()), -1, -1],
                         [tratamento_dados(oitavas61.get()), tratamento_dados(oitavas62.get()), -1, -1],
                         [tratamento_dados(oitavas71.get()), tratamento_dados(oitavas72.get()), -1, -1],
                         [tratamento_dados(oitavas81.get()), tratamento_dados(oitavas82.get()), -1, -1]]


        # Bloco que analisa os resultados das partidas e verifica se houve penaltis.
        # Infelizmente não foi possível essa verificação em uma função devido a espeficidades das variáveis dinâmicas.
        if resul_oitavas[0][0] == resul_oitavas[0][1] and resul_oitavas[0][0] != -1:
            msg = messagebox.askyesno("PENALTIS!!!", "A seleção da(o) " + dados_oitavas.s1_str.get() +
                                      " empatou com a seleção da(o) " + dados_oitavas.s2_str.get() + ". O(A) " +
                                      dados_oitavas.s1_str.get() + " venceu nos penaltis?")
            if msg:
                resul_oitavas[0][2] = 1
                resul_oitavas[0][3] = 0
            else:
                resul_oitavas[0][2] = 0
                resul_oitavas[0][3] = 1


        if resul_oitavas[1][0] == resul_oitavas[1][1] and resul_oitavas[1][0] != -1:
            msg = messagebox.askyesno("PENALTIS!!!", "A seleção da(o) " + dados_oitavas.s3_str.get() +
                                      " empatou com a seleção da(o) " + dados_oitavas.s4_str.get() + ". O(A) " +
                                      dados_oitavas.s3_str.get() + " venceu nos penaltis?")
            if msg:
                resul_oitavas[1][2] = 1
                resul_oitavas[1][3] = 0
            else:
                resul_oitavas[1][2] = 0
                resul_oitavas[1][3] = 1

        if resul_oitavas[2][0] == resul_oitavas[2][1] and resul_oitavas[2][0] != -1:
            msg = messagebox.askyesno("PENALTIS!!!", "A seleção da(o) " + dados_oitavas.s5_str.get() +
                                      " empatou com a seleção da(o) " + dados_oitavas.s6_str.get() + ". O(A) " +
                                      dados_oitavas.s5_str.get() + " venceu nos penaltis?")
            if msg:
                resul_oitavas[2][2] = 1
                resul_oitavas[2][3] = 0
            else:
                resul_oitavas[2][2] = 0
                resul_oitavas[2][3] = 1


        if resul_oitavas[3][0] == resul_oitavas[3][1] and resul_oitavas[3][0] != -1:
            msg = messagebox.askyesno("PENALTIS!!!", "A seleção da(o) " + dados_oitavas.s7_str.get() +
                                      " empatou com a seleção da(o) " + dados_oitavas.s8_str.get() + ". O(A) " +
                                      dados_oitavas.s7_str.get() + " venceu nos penaltis?")
            if msg:
                resul_oitavas[3][2] = 1
                resul_oitavas[3][3] = 0
            else:
                resul_oitavas[3][2] = 0
                resul_oitavas[3][3] = 1

        if resul_oitavas[4][0] == resul_oitavas[4][1] and resul_oitavas[4][0] != -1:
            msg = messagebox.askyesno("PENALTIS!!!", "A seleção da(o) " + dados_oitavas.s9_str.get() +
                                      " empatou com a seleção da(o) " + dados_oitavas.s10_str.get() + ". O(A) " +
                                      dados_oitavas.s9_str.get() + " venceu nos penaltis?")
            if msg:
                resul_oitavas[4][2] = 1
                resul_oitavas[4][3] = 0
            else:
                resul_oitavas[4][2] = 0
                resul_oitavas[4][3] = 1


        if resul_oitavas[5][0] == resul_oitavas[5][1] and resul_oitavas[5][0] != -1:
            msg = messagebox.askyesno("PENALTIS!!!", "A seleção da(o) " + dados_oitavas.s11_str.get() +
                                      " empatou com a seleção da(o) " + dados_oitavas.s12_str.get() + ". O(A) " +
                                      dados_oitavas.s11_str.get() + " venceu nos penaltis?")
            if msg:
                resul_oitavas[5][2] = 1
                resul_oitavas[5][3] = 0
            else:
                resul_oitavas[5][2] = 0
                resul_oitavas[5][3] = 1


        if resul_oitavas[6][0] == resul_oitavas[6][1] and resul_oitavas[6][0] != -1:
            msg = messagebox.askyesno("PENALTIS!!!", "A seleção da(o) " + dados_oitavas.s13_str.get() +
                                      " empatou com a seleção da(o) " + dados_oitavas.s14_str.get() + ". O(A) " +
                                      dados_oitavas.s13_str.get() + " venceu nos penaltis?")
            if msg:
                resul_oitavas[6][2] = 1
                resul_oitavas[6][3] = 0
            else:
                resul_oitavas[6][2] = 0
                resul_oitavas[6][3] = 1


        if resul_oitavas[7][0] == resul_oitavas[7][1] and resul_oitavas[7][0] != -1:
            msg = messagebox.askyesno("PENALTIS!!!", "A seleção da(o) " + dados_oitavas.s15_str.get() +
                                      " empatou com a seleção da(o) " + dados_oitavas.s16_str.get() + ". O(A) " +
                                      dados_oitavas.s15_str.get() + " venceu nos penaltis?")
            if msg:
                resul_oitavas[7][2] = 1
                resul_oitavas[7][3] = 0
            else:
                resul_oitavas[7][2] = 0
                resul_oitavas[7][3] = 1

        # Salva os resultados dos jogos e forma os grupos das quartas, seminfinais e finais
        data.salvando_oitavas(resul_oitavas)
        fase_final.formando_quartas()
        fase_final.formando_semifinais()
        fase_final.formando_finais()


    # Salvamento das quartas de finais. Isso acontece quando há o clique no botão "Salvar" na interface gráfica.
    def salvar_quartas():

        # Os valores são passados ao banco de dados por meio de uma lista de listas.
        # Os primeiros dois valores são relacionados com o placar dos jogos, enquanto os segundos são preenchidos
        # em caso de penalties.
        resul_quartas = [[tratamento_dados(quartas11.get()), tratamento_dados(quartas12.get()), -1, -1],
                         [tratamento_dados(quartas21.get()), tratamento_dados(quartas22.get()), -1, -1],
                         [tratamento_dados(quartas31.get()), tratamento_dados(quartas32.get()), -1, -1],
                         [tratamento_dados(quartas41.get()), tratamento_dados(quartas42.get()), -1, -1]]


        # Verifica se os resultados são empates. Caso sejam, pergunta sobre os vencedores nos penalties.
        if resul_quartas[0][0] == resul_quartas[0][1] and resul_quartas[0][0] != -1:
            msg = messagebox.askyesno("PENALTIS!!!", "A seleção da(o) " + dados_quartas.s1_str.get() +
                                      " empatou com a seleção da(o) " + dados_quartas.s2_str.get() + ". O(A) " +
                                      dados_quartas.s1_str.get() + " venceu nos penaltis?")
            if msg:
                resul_quartas[0][2] = 1
                resul_quartas[0][3] = 0
            else:
                resul_quartas[0][2] = 0
                resul_quartas[0][3] = 1

        if resul_quartas[1][0] == resul_quartas[1][1] and resul_quartas[1][0] != -1:
            msg = messagebox.askyesno("PENALTIS!!!", "A seleção da(o) " + dados_quartas.s3_str.get() +
                                      " empatou com a seleção da(o) " + dados_quartas.s4_str.get() + ". O(A) " +
                                      dados_quartas.s3_str.get() + " venceu nos penaltis?")
            if msg:
                resul_quartas[1][2] = 1
                resul_quartas[1][3] = 0
            else:
                resul_quartas[1][2] = 0
                resul_quartas[1][3] = 1

        if resul_quartas[2][0] == resul_quartas[2][1] and resul_quartas[2][0] != -1:
            msg = messagebox.askyesno("PENALTIS!!!", "A seleção da(o) " + dados_quartas.s5_str.get() +
                                      " empatou com a seleção da(o) " + dados_quartas.s6_str.get() + ". O(A) " +
                                      dados_quartas.s5_str.get() + " venceu nos penaltis?")
            if msg:
                resul_quartas[2][2] = 1
                resul_quartas[2][3] = 0
            else:
                resul_quartas[2][2] = 0
                resul_quartas[2][3] = 1

        if resul_quartas[3][0] == resul_quartas[3][1] and resul_quartas[3][0] != -1:
            msg = messagebox.askyesno("PENALTIS!!!", "A seleção da(o) " + dados_quartas.s7_str.get() +
                                      " empatou com a seleção " + dados_quartas.s8_str.get() + ". O(A) " +
                                      dados_quartas.s7_str.get() + " venceu nos penaltis?")
            if msg:
                resul_quartas[3][2] = 1
                resul_quartas[3][3] = 0
            else:
                resul_quartas[3][2] = 0
                resul_quartas[3][3] = 1

        # Realiza o salvamento dos resultados das quartas de finais, atualiza variáveis e forma semifinais
        # Logo, em seguida, faz o seu salvamento.
        data.salvando_quartas(resul_quartas)
        dados_quartas.atualizar(data.recuperando_quartas_str())
        fase_final.formando_semifinais()
        atualizar_semifinais()

    # Realiza o salvamento dos resultados quando o botão "Salvar" é clicado na interface.
    def salvar_semifinais():

        # Os resultados são armazenados na forma de lista de listas, representando o placar do jogo e o resultado
        # dos penalties, quando ocorrer empates.
        resul_semifinais = [[tratamento_dados(semifinais11.get()), tratamento_dados(semifinais12.get()), -1, -1],
                            [tratamento_dados(semifinais21.get()), tratamento_dados(semifinais22.get()), -1, -1]]


        # Verifica a ocorrência de penalties e providencia respostas.
        if resul_semifinais[0][0] == resul_semifinais[0][1] and resul_semifinais[0][0] != -1:
            msg = messagebox.askyesno("PENALTIS!!!", "A seleção da(o) " + dados_semifinal.s1_str.get() +
                                      " empatou com a seleção da(o) " + dados_semifinal.s2_str.get() + ". O(A) " +
                                      dados_semifinal.s1_str.get() + " venceu nos penaltis?")
            if msg:
                resul_semifinais[0][2] = 1
                resul_semifinais[0][3] = 0
            else:
                resul_semifinais[0][2] = 0
                resul_semifinais[0][3] = 1

        if resul_semifinais[1][0] == resul_semifinais[1][1] and resul_semifinais[1][0] != -1:
            msg = messagebox.askyesno("PENALTIS!!!", "A seleção da(o) " + dados_semifinal.s3_str.get() +
                                      " empatou com a seleção da(o) " + dados_semifinal.s4_str.get() + ". O(A) " +
                                      dados_semifinal.s3_str.get() + " venceu nos penaltis?")
            if msg:
                resul_semifinais[1][2] = 1
                resul_semifinais[1][3] = 0
            else:
                resul_semifinais[1][2] = 0
                resul_semifinais[1][3] = 1

        # Salva os valores todos atualizados e forma as finais.
        data.salvando_semifinais(resul_semifinais)
        dados_semifinal.atualizar(data.recuperando_semifinais_str())
        fase_final.formando_finais()

    # Realiza o salvamento da final e apresenta o campeão, quando o o botão for clicado.
    def salvar_final():


        resul_finais = [[tratamento_dados(final11.get()), tratamento_dados(final12.get()), -1, -1],
                        [tratamento_dados(final21.get()), tratamento_dados(final22.get()), -1, -1]]


        # Verifica a ocorrência de penalties na disputa por terceiro e quarto lugar.
        if resul_finais[1][0] == resul_finais[1][1] and resul_finais[1][0] != -1:
            msg = messagebox.askyesno("PENALTIS!!!", "A seleção da(o) " + dados_finais.s3_str.get() +
                                      " empatou com a seleção da(o) " + dados_finais.s4_str.get() + ". O(A) " +
                                      dados_finais.s3_str.get() + " venceu nos penaltis?")
            if msg:
                resul_finais[1][2] = 1
                resul_finais[1][3] = 0
            else:
                resul_finais[1][2] = 0
                resul_finais[1][3] = 1

        # Verifica resultado da disputa de primeiro e segundo lugar na final. Caso seja empate, o vencedor
        # será decidido nos penalties.
        if resul_finais[0][0] != -1 and resul_finais[0][1] != -1:
            if resul_finais[0][0] > resul_finais[0][1]:
                messagebox.showinfo("CAMPEÃ!!!", "A seleção da(o) " + dados_finais.s1_str.get() + " é a campeã!!!")
            elif resul_finais[0][0] < resul_finais[0][1]:
                messagebox.showinfo("CAMPEÃ!!!", "A seleção da(o) " + dados_finais.s2_str.get() + " é a campeã!!!")
            else:
                msg = messagebox.askyesno("PENALTIS!!!", "A seleção da(o) " + dados_finais.s1_str.get() +
                                            " empatou com a seleção da(o) " + dados_finais.s2_str.get() + ". O(A) " +
                                            dados_finais.s1_str.get() + " venceu nos penaltis?")
                if msg:
                    messagebox.showinfo("CAMPEÃ!!!", "A seleção da(o) " + dados_finais.s1_str.get() + " é a campeã!!!")
                    resul_finais[0][2] = 1
                    resul_finais[0][3] = 0
                else:
                    messagebox.showinfo("CAMPEÃ!!!", "A seleção da(o) " + dados_finais.s2_str.get() + " é a campeã!!!")
                    resul_finais[0][2] = 0
                    resul_finais[0][3] = 1

        # Salva os dados das finais.
        data.salvando_finais(resul_finais)

    # Essa função tem a finalidade de atualizar todas as variáveis dinâmicas da interface gráfica.
    def oitavas_final():

        frame_oitavas.place(x=50, y=50, width=700, height=430)  # posição de exibição
        frame_quartas_semifinais.place(x=50, y=600, width=700, height=430)  # posição de exibição
        frame_final.place(x=600, y=600, width=700, height=430)  # posição de exibição

        # Recupera os dados salvos na memória e atualiza valores das variáveis.
        dados_oitavas.atualizar(data.recuperando_oitavas_str())

        # Apaga os valores do placar existente nos placares e recupera valores para preenchimento dos placares
        oitavas11.delete(0)
        oitavas12.delete(0)
        oitavas21.delete(0)
        oitavas22.delete(0)
        oitavas31.delete(0)
        oitavas32.delete(0)
        oitavas41.delete(0)
        oitavas42.delete(0)
        oitavas51.delete(0)
        oitavas52.delete(0)
        oitavas61.delete(0)
        oitavas62.delete(0)
        oitavas71.delete(0)
        oitavas72.delete(0)
        oitavas81.delete(0)
        oitavas82.delete(0)
        oitavas11.insert(0, dados_oitavas.s1_gol.get())
        oitavas12.insert(0, dados_oitavas.s2_gol.get())
        oitavas21.insert(0, dados_oitavas.s3_gol.get())
        oitavas22.insert(0, dados_oitavas.s4_gol.get())
        oitavas31.insert(0, dados_oitavas.s5_gol.get())
        oitavas32.insert(0, dados_oitavas.s6_gol.get())
        oitavas41.insert(0, dados_oitavas.s7_gol.get())
        oitavas42.insert(0, dados_oitavas.s8_gol.get())
        oitavas51.insert(0, dados_oitavas.s9_gol.get())
        oitavas52.insert(0, dados_oitavas.s10_gol.get())
        oitavas61.insert(0, dados_oitavas.s11_gol.get())
        oitavas62.insert(0, dados_oitavas.s12_gol.get())
        oitavas71.insert(0, dados_oitavas.s13_gol.get())
        oitavas72.insert(0, dados_oitavas.s14_gol.get())
        oitavas81.insert(0, dados_oitavas.s15_gol.get())
        oitavas82.insert(0, dados_oitavas.s16_gol.get())

        # Para recuperar imagens dinamicamente, é necessário mostrar ao programa a alteração dos valores
        # das variáveis dinâmicas. Por isso, exige o código abaixo.
        img1 = ImageTk.PhotoImage(Image.open(dados_oitavas.s1_band.get()).resize((50, 30)))
        img2 = ImageTk.PhotoImage(Image.open(dados_oitavas.s2_band.get()).resize((50, 30)))
        img3 = ImageTk.PhotoImage(Image.open(dados_oitavas.s3_band.get()).resize((50, 30)))
        img4 = ImageTk.PhotoImage(Image.open(dados_oitavas.s4_band.get()).resize((50, 30)))
        img5 = ImageTk.PhotoImage(Image.open(dados_oitavas.s5_band.get()).resize((50, 30)))
        img6 = ImageTk.PhotoImage(Image.open(dados_oitavas.s6_band.get()).resize((50, 30)))
        img7 = ImageTk.PhotoImage(Image.open(dados_oitavas.s7_band.get()).resize((50, 30)))
        img8 = ImageTk.PhotoImage(Image.open(dados_oitavas.s8_band.get()).resize((50, 30)))
        img9 = ImageTk.PhotoImage(Image.open(dados_oitavas.s9_band.get()).resize((50, 30)))
        img10 = ImageTk.PhotoImage(Image.open(dados_oitavas.s10_band.get()).resize((50, 30)))
        img11 = ImageTk.PhotoImage(Image.open(dados_oitavas.s11_band.get()).resize((50, 30)))
        img12 = ImageTk.PhotoImage(Image.open(dados_oitavas.s12_band.get()).resize((50, 30)))
        img13 = ImageTk.PhotoImage(Image.open(dados_oitavas.s13_band.get()).resize((50, 30)))
        img14 = ImageTk.PhotoImage(Image.open(dados_oitavas.s14_band.get()).resize((50, 30)))
        img15 = ImageTk.PhotoImage(Image.open(dados_oitavas.s15_band.get()).resize((50, 30)))
        img16 = ImageTk.PhotoImage(Image.open(dados_oitavas.s16_band.get()).resize((50, 30)))
        lbl1.configure(image=img1)
        lbl2.configure(image=img2)
        lbl3.configure(image=img3)
        lbl4.configure(image=img4)
        lbl5.configure(image=img5)
        lbl6.configure(image=img6)
        lbl7.configure(image=img7)
        lbl8.configure(image=img8)
        lbl9.configure(image=img9)
        lbl10.configure(image=img10)
        lbl11.configure(image=img11)
        lbl12.configure(image=img12)
        lbl13.configure(image=img13)
        lbl14.configure(image=img14)
        lbl15.configure(image=img15)
        lbl16.configure(image=img16)
        lbl1.image = img1
        lbl2.image = img2
        lbl3.image = img3
        lbl4.image = img4
        lbl5.image = img5
        lbl6.image = img6
        lbl7.image = img7
        lbl8.image = img8
        lbl9.image = img9
        lbl10.image = img10
        lbl11.image = img11
        lbl12.image = img12
        lbl13.image = img13
        lbl14.image = img14
        lbl15.image = img15
        lbl16.image = img16


    # Função interna que serve para colocar o frame das quartas e das semifinais em foco e realizar a atualização
    # das variáveis das quartas e das semifinais.
    def quartas_semifinais():
        # Coloca o frame das quartas_semifinais em foco na tela.
        frame_quartas_semifinais.place(x=50, y=50, width=700, height=430)  # posição de exibição
        frame_oitavas.place(x=50, y=600, width=700, height=430)  # posição de exibição
        frame_final.place(x=600, y=600, width=700, height=430)  # posição de exibição

        # Atualiza as variáveis dinâmicas relacionadas com as quartas de finais e com as semifinais.
        atualizar_quartas()
        atualizar_semifinais()

    # Função que atualiza os valores das variáveis
    def atualizar_quartas():
        # Recupera valores das quartas de finais.
        dados_quartas.atualizar(data.recuperando_quartas_str())

        # Provoca a alteração dos valores das imagens e atualiza as variáveis dinâmicas.
        img17 = ImageTk.PhotoImage(Image.open(dados_quartas.s1_band.get()).resize((50, 30)))
        img18 = ImageTk.PhotoImage(Image.open(dados_quartas.s2_band.get()).resize((50, 30)))
        img19 = ImageTk.PhotoImage(Image.open(dados_quartas.s3_band.get()).resize((50, 30)))
        img20 = ImageTk.PhotoImage(Image.open(dados_quartas.s4_band.get()).resize((50, 30)))
        img21 = ImageTk.PhotoImage(Image.open(dados_quartas.s5_band.get()).resize((50, 30)))
        img22 = ImageTk.PhotoImage(Image.open(dados_quartas.s6_band.get()).resize((50, 30)))
        img23 = ImageTk.PhotoImage(Image.open(dados_quartas.s7_band.get()).resize((50, 30)))
        img24 = ImageTk.PhotoImage(Image.open(dados_quartas.s8_band.get()).resize((50, 30)))
        lbl17.configure(image=img17)
        lbl18.configure(image=img18)
        lbl19.configure(image=img19)
        lbl20.configure(image=img20)
        lbl21.configure(image=img21)
        lbl22.configure(image=img22)
        lbl23.configure(image=img23)
        lbl24.configure(image=img24)
        lbl17.image = img17
        lbl18.image = img18
        lbl19.image = img19
        lbl20.image = img20
        lbl21.image = img21
        lbl22.image = img22
        lbl23.image = img23
        lbl24.image = img24

        # Apaga os valores das caixas de entrada e recupera valores para preenchimento dos placares
        quartas11.delete(0)
        quartas12.delete(0)
        quartas21.delete(0)
        quartas22.delete(0)
        quartas31.delete(0)
        quartas32.delete(0)
        quartas41.delete(0)
        quartas42.delete(0)
        quartas11.insert(0, dados_quartas.s1_gol.get())
        quartas12.insert(0, dados_quartas.s2_gol.get())
        quartas21.insert(0, dados_quartas.s3_gol.get())
        quartas22.insert(0, dados_quartas.s4_gol.get())
        quartas31.insert(0, dados_quartas.s5_gol.get())
        quartas32.insert(0, dados_quartas.s6_gol.get())
        quartas41.insert(0, dados_quartas.s7_gol.get())
        quartas42.insert(0, dados_quartas.s8_gol.get())


    # Função interna que serve para atualizar os dados das semifinais.
    def atualizar_semifinais():

        # Recupera os dados existentes no banco de dados.
        dados_semifinal.atualizar(data.recuperando_semifinais_str())

        # Provoca a alteração dos conteúdos das variáveis dinâmicas.
        img25 = ImageTk.PhotoImage(Image.open(dados_semifinal.s1_band.get()).resize((50, 30)))
        img26 = ImageTk.PhotoImage(Image.open(dados_semifinal.s2_band.get()).resize((50, 30)))
        img27 = ImageTk.PhotoImage(Image.open(dados_semifinal.s3_band.get()).resize((50, 30)))
        img28 = ImageTk.PhotoImage(Image.open(dados_semifinal.s4_band.get()).resize((50, 30)))
        lbl25.configure(image=img25)
        lbl26.configure(image=img26)
        lbl27.configure(image=img27)
        lbl28.configure(image=img28)
        lbl25.image = img25
        lbl26.image = img26
        lbl27.image = img27
        lbl28.image = img28

        # Apaga os valores das caixas de texto e reescreve os valores recuperados do banco de dados.
        semifinais11.delete(0)
        semifinais12.delete(0)
        semifinais21.delete(0)
        semifinais22.delete(0)
        semifinais11.insert(0, dados_semifinal.s1_gol.get())
        semifinais12.insert(0, dados_semifinal.s2_gol.get())
        semifinais21.insert(0, dados_semifinal.s3_gol.get())
        semifinais22.insert(0, dados_semifinal.s4_gol.get())


    # Função interna que serva para posicionar o frame da final em foco, bem como recuperar os dados
    # do banco de dados.
    def final():

        # Coloca em foco o frame da final.
        frame_final.place(x=50, y=50, width=700, height=430)  # posição de exibição
        frame_quartas_semifinais.place(x=50, y=600, width=700, height=430)  # posição de exibição
        frame_oitavas.place(x=600, y=600, width=700, height=430)  # posição de exibição

        # Recupera os dados das finais do banco de daos.
        dados_finais.atualizar(data.recuperando_finais_str())

        # Apaga os valores das caixas de texto e recupera os valores e entrada dos placares do banco de dados.
        final11.delete(0)
        final12.delete(0)
        final21.delete(0)
        final22.delete(0)
        final11.insert(0, dados_finais.s1_gol.get())
        final12.insert(0, dados_finais.s2_gol.get())
        final21.insert(0, dados_finais.s3_gol.get())
        final22.insert(0, dados_finais.s4_gol.get())

        # Para recuperar imagens dinamicamente, é necessário o seguinte código
        img29 = ImageTk.PhotoImage(Image.open(dados_finais.s1_band.get()).resize((50, 30)))
        img30 = ImageTk.PhotoImage(Image.open(dados_finais.s2_band.get()).resize((50, 30)))
        img31 = ImageTk.PhotoImage(Image.open(dados_finais.s3_band.get()).resize((50, 30)))
        img32 = ImageTk.PhotoImage(Image.open(dados_finais.s4_band.get()).resize((50, 30)))
        lbl29.configure(image=img29)
        lbl30.configure(image=img30)
        lbl31.configure(image=img31)
        lbl32.configure(image=img32)
        lbl29.image = img29
        lbl30.image = img30
        lbl31.image = img31
        lbl32.image = img32



    # -------------------------------------------------------------------------------------------------------------------
    # Cria a janela de Fase Final
    janela2 = Toplevel()
    janela2.title("SHOW DE BOLA - FASE FINAL")
    janela2.configure(background='#405E38')
    janela2.geometry("800x500+200+200") #800x500 no começo
    janela2.transient(janela)
    janela2.focus_force()
    janela2.grab_set()
    janela2.resizable(False, False)

    # Personaliza o background
    bg = ImageTk.PhotoImage(Image.open('imagens/campo.png').resize((800, 500)))
    canvas = Canvas(janela2, width=800, height=600)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg, anchor="nw")

    # Inicializa objetos para manipular o banco de dados e informações do back-end da Fase Final.
    # Por exemplo, a formação das oitavas de final com os dados dos grupos é realizada nesse momento.
    data = DataSet()
    fase_final = FaseFinal()
    fase_final.formando_oitavas()

    # Criar objetos para atualização das variáveis dinâmicas com valores padrões.
    padrao = [['-', 'imagens/bandeira.png', ''] for i in range(17)]
    dados_oitavas = AtualizarOitavas(data.recuperando_oitavas())
    dados_quartas = AutalizarQuartas(padrao)
    dados_semifinal = AtualizarFinalSemi(padrao)
    dados_finais = AtualizarFinalSemi(padrao)


    # -------------------------------------------------------------------------------------------------------------------
    # Frame das Etapas da Fase Final (Recebe os botões para alterar as fases)
    frame = Frame(janela2, bg="white")
    frame.grid_anchor(CENTER)
    frame.place(x=50, y=10, width=700, height=30)

    # Códigos acerca dos Botões dos Grupos-----------------------------------

    # Criação dos objetos Botões que serão posicionados no frame
    btn_informacoes = Button(frame, font="Verdana 10 bold", text="INFORMACOES", bd=0, padx=2, pady=2, bg="#405E38", fg="white",
                         command=informacoes)
    btn_oitavas = Button(frame, font="Verdana 10 bold", text="OITAVAS DE FINAL", bd=0, padx=2, pady=2, bg="#405E38", fg="white",
                         command=oitavas_final)
    btn_quartas_semifinais= Button(frame, font="Verdana 10 bold", text="QUARTAS E SEMIFINAIS", bd=0, padx=2, pady=2, bg="#405E38", fg="white",
                         command=quartas_semifinais)
    btn_final = Button(frame, font="Verdana 10 bold", text="FINAL", bd=0, padx=2, pady=2, bg="#405E38", fg="white",
                         command=final)
    btn_retornar = Button(frame, font="Verdana 10 bold", text="MENU PRINCIPAL", bd=0, padx=2, pady=2, bg="#405E38",
                          fg="white", command=lambda: quit(janela2))

    # Posicionamento dos objetos na tela utilizando a formatação grid
    btn_oitavas.grid(row=0, column=0, padx=1)
    btn_quartas_semifinais.grid(row=0, column=1, padx=1)
    btn_final.grid(row=0, column=2, padx=1)
    btn_informacoes.grid(row=0, column=3, padx=1)
    btn_retornar.grid(row=0, column=4, padx=1)


    # Exibindo por padrão as Oitavas de Final
    # -------------------------------------------------------------------------------------------------------------------
    # Frames das Eliminatórias (Recebe os botões para alterar os grupos exibidos no frame jogos)
    frame_oitavas = Frame(janela2, bg="white")
    frame_quartas_semifinais = Frame(janela2, bg="white")
    frame_final = Frame(janela2, bg="white")

    # Configurações de posicionamento nos Frames
    frame_oitavas.grid_anchor(CENTER)
    frame_quartas_semifinais.grid_anchor(CENTER)
    frame_final.grid_anchor(CENTER)


    # ------------------------------------------------------------------------------------------------------------------
    # Montagem do Frame de Oitavas de Final

    # Título do Frame
    Label(frame_oitavas, fg="#405E38", bg="white", font="Verdana 12 bold", text="OITAVAS DE FINAL").grid(row=0, column=0, columnspan=7)
    Label(frame_oitavas, bg='white').grid(row=1, column=0)

    # Primeiro jogo------------------------------------------------------------------------------------------------------
    oitava1 = 2
    img1 = ImageTk.PhotoImage(Image.open(dados_oitavas.s1_band.get()).resize((50, 30)))
    img2 = ImageTk.PhotoImage(Image.open(dados_oitavas.s2_band.get()).resize((50, 30)))
    Label(frame_oitavas, bg='white', textvariable=dados_oitavas.s1_str, padx=2, justify=RIGHT, font="Verdana 10 bold").grid(row=oitava1, column=0, padx=2)
    lbl1 = Label(frame_oitavas, bg='white', width=60, justify=LEFT)
    lbl1.configure(image=img1)
    lbl1.image = img1
    lbl1.grid(row=oitava1, column=1)
    oitavas11 = Entry(frame_oitavas, bg='white', width=3)
    oitavas11.grid(row=oitava1, column=2, ipadx=2)
    Label(frame_oitavas, bg='white', width=2, text='X').grid(row=oitava1, column=3)
    oitavas12 = Entry(frame_oitavas, bg='white', width=3)
    oitavas12.grid(row=oitava1, column=4, ipadx=2)
    lbl2 = Label(frame_oitavas, bg='white', width=60, justify=RIGHT)
    lbl2.configure(image=img2)
    lbl2.image = img2
    lbl2.grid(row=oitava1, column=5)
    Label(frame_oitavas, bg='white', textvariable=dados_oitavas.s2_str, padx=5, justify=LEFT, font="Verdana 10 bold").grid(row=oitava1, column=6, padx=2)

    # Segundo jogo------------------------------------------------------------------------------------------------------
    oitava2 = 3
    img3 = ImageTk.PhotoImage(Image.open(dados_oitavas.s3_band.get()).resize((50, 30)))
    img4 = ImageTk.PhotoImage(Image.open(dados_oitavas.s4_band.get()).resize((50, 30)))
    Label(frame_oitavas, bg='white', textvariable=dados_oitavas.s3_str, padx=2, justify=RIGHT, font="Verdana 10 bold").grid(row=oitava2, column=0, padx=2)
    lbl3 = Label(frame_oitavas, bg='white', width=60, justify=LEFT)
    lbl3.configure(image=img3)
    lbl3.image = img3
    lbl3.grid(row=oitava2, column=1)
    oitavas21 = Entry(frame_oitavas, bg='white', width=3)
    oitavas21.grid(row=oitava2, column=2, ipadx=2)
    Label(frame_oitavas, bg='white', width=2, text='X').grid(row=oitava2, column=3)
    oitavas22 = Entry(frame_oitavas, bg='white', width=3)
    oitavas22.grid(row=oitava2, column=4, ipadx=2)
    lbl4 = Label(frame_oitavas, bg='white', width=60, justify=RIGHT)
    lbl4.configure(image=img4)
    lbl4.image = img4
    lbl4.grid(row=oitava2, column=5)
    Label(frame_oitavas, bg='white', textvariable=dados_oitavas.s4_str, padx=5, justify=LEFT, font="Verdana 10 bold").grid(row=oitava2, column=6, padx=2)


    # Terceiro jogo ----------------------------------------------------------------------------------------------------
    oitava3 = 4
    img5 = ImageTk.PhotoImage(Image.open(dados_oitavas.s5_band.get()).resize((50, 30)))
    img6 = ImageTk.PhotoImage(Image.open(dados_oitavas.s6_band.get()).resize((50, 30)))
    Label(frame_oitavas, bg='white', textvariable=dados_oitavas.s5_str, padx=2, justify=RIGHT, font="Verdana 10 bold").grid(row=oitava3, column=0, padx=2)
    lbl5 = Label(frame_oitavas, bg='white', width=60, justify=LEFT)
    lbl5.configure(image=img5)
    lbl5.image = img5
    lbl5.grid(row=oitava3, column=1)
    oitavas31 = Entry(frame_oitavas, bg='white', width=3)
    oitavas31.grid(row=oitava3, column=2, ipadx=2)
    Label(frame_oitavas, bg='white', width=2, text='X').grid(row=oitava3, column=3)
    oitavas32 = Entry(frame_oitavas, bg='white', width=3)
    oitavas32.grid(row=oitava3, column=4, ipadx=2)
    lbl6 = Label(frame_oitavas, bg='white', width=60, justify=RIGHT)
    lbl6.configure(image=img6)
    lbl6.image = img6
    lbl6.grid(row=oitava3, column=5)
    Label(frame_oitavas, bg='white', textvariable=dados_oitavas.s6_str, padx=5, justify=LEFT, font="Verdana 10 bold").grid(row=oitava3, column=6, padx=2)

    # Quarto jogo------------------------------------------------------------------------------------------------------
    oitava4 = 5
    img7 = ImageTk.PhotoImage(Image.open(dados_oitavas.s7_band.get()).resize((50, 30)))
    img8 = ImageTk.PhotoImage(Image.open(dados_oitavas.s8_band.get()).resize((50, 30)))
    Label(frame_oitavas, bg='white', textvariable=dados_oitavas.s7_str, padx=2, justify=RIGHT, font="Verdana 10 bold").grid(row=oitava4, column=0, padx=2)
    lbl7 = Label(frame_oitavas, bg='white', width=60, justify=LEFT)
    lbl7.configure(image=img7)
    lbl7.image = img7
    lbl7.grid(row=oitava4, column=1)
    oitavas41 = Entry(frame_oitavas, bg='white', width=3)
    oitavas41.grid(row=oitava4, column=2, ipadx=2)
    Label(frame_oitavas, bg='white', width=2, text='X').grid(row=oitava4, column=3)
    oitavas42 = Entry(frame_oitavas, bg='white', width=3)
    oitavas42.grid(row=oitava4, column=4, ipadx=2)
    lbl8 = Label(frame_oitavas, bg='white', width=60, justify=RIGHT)
    lbl8.configure(image=img8)
    lbl8.image = img8
    lbl8.grid(row=oitava4, column=5)
    Label(frame_oitavas, bg='white', textvariable=dados_oitavas.s8_str, padx=5, justify=LEFT, font="Verdana 10 bold").grid(row=oitava4, column=6, padx=2)


    # Quinto jogo ------------------------------------------------------------------------------------------------------
    oitava5 = 6
    img9 = ImageTk.PhotoImage(Image.open(dados_oitavas.s9_band.get()).resize((50, 30)))
    img10 = ImageTk.PhotoImage(Image.open(dados_oitavas.s10_band.get()).resize((50, 30)))
    Label(frame_oitavas, bg='white', textvariable=dados_oitavas.s9_str, padx=2, justify=RIGHT, font="Verdana 10 bold").grid(row=oitava5, column=0, padx=2)
    lbl9 = Label(frame_oitavas, bg='white', width=60, justify=LEFT)
    lbl9.configure(image=img9)
    lbl9.image = img9
    lbl9.grid(row=oitava5, column=1)
    oitavas51 = Entry(frame_oitavas, bg='white', width=3)
    oitavas51.grid(row=oitava5, column=2, ipadx=2)
    Label(frame_oitavas, bg='white', width=2, text='X').grid(row=oitava5, column=3)
    oitavas52 = Entry(frame_oitavas, bg='white', width=3)
    oitavas52.grid(row=oitava5, column=4, ipadx=2)
    lbl10 = Label(frame_oitavas, bg='white', width=60, justify=RIGHT)
    lbl10.configure(image=img10)
    lbl10.image = img10
    lbl10.grid(row=oitava5, column=5)
    Label(frame_oitavas, bg='white', textvariable=dados_oitavas.s10_str, padx=5, justify=LEFT, font="Verdana 10 bold").grid(row=oitava5, column=6, padx=2)

    # Sexto jogo------------------------------------------------------------------------------------------------------
    oitava6 = 7
    img11 = ImageTk.PhotoImage(Image.open(dados_oitavas.s11_band.get()).resize((50, 30)))
    img12 = ImageTk.PhotoImage(Image.open(dados_oitavas.s12_band.get()).resize((50, 30)))
    Label(frame_oitavas, bg='white', textvariable=dados_oitavas.s11_str, padx=2, justify=RIGHT, font="Verdana 10 bold").grid(row=oitava6, column=0, padx=2)
    lbl11 = Label(frame_oitavas, bg='white', width=60, justify=LEFT)
    lbl11.configure(image=img11)
    lbl11.image = img11
    lbl11.grid(row=oitava6, column=1)
    oitavas61 = Entry(frame_oitavas, bg='white', width=3)
    oitavas61.grid(row=oitava6, column=2, ipadx=2)
    Label(frame_oitavas, bg='white', width=2, text='X').grid(row=oitava6, column=3)
    oitavas62 = Entry(frame_oitavas, bg='white', width=3)
    oitavas62.grid(row=oitava6, column=4, ipadx=2)
    lbl12 = Label(frame_oitavas, bg='white', width=60, justify=RIGHT)
    lbl12.configure(image=img12)
    lbl12.image = img12
    lbl12.grid(row=oitava6, column=5)
    Label(frame_oitavas, bg='white', textvariable=dados_oitavas.s12_str, padx=5, justify=LEFT, font="Verdana 10 bold").grid(row=oitava6, column=6, padx=2)


    # Sétimo jogo ------------------------------------------------------------------------------------------------------
    oitava7 = 8
    img13 = ImageTk.PhotoImage(Image.open(dados_oitavas.s13_band.get()).resize((50, 30)))
    img14 = ImageTk.PhotoImage(Image.open(dados_oitavas.s14_band.get()).resize((50, 30)))
    Label(frame_oitavas, bg='white', textvariable=dados_oitavas.s13_str, padx=2, justify=RIGHT, font="Verdana 10 bold").grid(row=oitava7, column=0, padx=2)
    lbl13 = Label(frame_oitavas, bg='white', width=60, justify=LEFT)
    lbl13.configure(image=img13)
    lbl13.image = img13
    lbl13.grid(row=oitava7, column=1)
    oitavas71 = Entry(frame_oitavas, bg='white', width=3)
    oitavas71.grid(row=oitava7, column=2, ipadx=2)
    Label(frame_oitavas, bg='white', width=2, text='X').grid(row=oitava7, column=3)
    oitavas72 = Entry(frame_oitavas, bg='white', width=3)
    oitavas72.grid(row=oitava7, column=4, ipadx=2)
    lbl14 = Label(frame_oitavas, bg='white', width=60, justify=RIGHT)
    lbl14.configure(image=img14)
    lbl14.image = img14
    lbl14.grid(row=oitava7, column=5)
    Label(frame_oitavas, bg='white', textvariable=dados_oitavas.s14_str, padx=5, justify=LEFT, font="Verdana 10 bold").grid(row=oitava7, column=6, padx=2)

    # Oitavo jogo------------------------------------------------------------------------------------------------------
    oitava8 = 9
    img15 = ImageTk.PhotoImage(Image.open(dados_oitavas.s15_band.get()).resize((50, 30)))
    img16 = ImageTk.PhotoImage(Image.open(dados_oitavas.s16_band.get()).resize((50, 30)))
    Label(frame_oitavas, bg='white', textvariable=dados_oitavas.s15_str, padx=2, justify=RIGHT, font="Verdana 10 bold").grid(row=oitava8, column=0, padx=2)
    lbl15 = Label(frame_oitavas, bg='white', width=60, justify=LEFT)
    lbl15.configure(image=img15)
    lbl15.image = img15
    lbl15.grid(row=oitava8, column=1)
    oitavas81 = Entry(frame_oitavas, bg='white', width=3)
    oitavas81.grid(row=oitava8, column=2, ipadx=2)
    Label(frame_oitavas, bg='white', width=2, text='X').grid(row=oitava8, column=3)
    oitavas82 = Entry(frame_oitavas, bg='white', width=3)
    oitavas82.grid(row=oitava8, column=4, ipadx=2)
    lbl16 = Label(frame_oitavas, bg='white', width=60, justify=RIGHT)
    lbl16.configure(image=img16)
    lbl16.image = img16
    lbl16.grid(row=oitava8, column=5)
    Label(frame_oitavas, bg='white', textvariable=dados_oitavas.s16_str, padx=5, justify=LEFT, font="Verdana 10 bold").grid(row=oitava8, column=6, padx=2)

    # Botão de salvar resultados
    Label(frame_oitavas, bg='white').grid(row=14, column=0)
    Button(frame_oitavas, font="Verdana 10 bold", text="SALVAR", bd=0, padx=2, pady=2, bg="#405E38", fg="white", command=salvar_oitavas).grid(row=15, column=0, columnspan=7)

    # ------------------------------------------------------------------------------------------------------------------
    # Montagem do Frame de Quartas e Semifinal (PRINCIPAL)

    frame_quartas_semifinais_interno = Frame(frame_quartas_semifinais, bg="white")
    frame_quartas_semifinais_interno.grid_anchor(CENTER)
    frame_quartas_semifinais_interno.grid(row=2, column=0)


    # ------------------------------------------------------------------------------------------------------------------
    # Montagem do Frame de Quartas
    frame_quartas = Frame(frame_quartas_semifinais_interno, bg="white")
    frame_quartas.grid_anchor(CENTER)
    frame_quartas.grid(row=0, column=0)

    Label(frame_quartas, fg="#405E38", bg="white", font="Verdana 12 bold", text="QUARTAS DE FINAIS").grid(row=0, column=0, columnspan=7)
    Label(frame_quartas, bg='white').grid(row=1, column=0)

    # Primeiro jogo------------------------------------------------------------------------------------------------------
    quartas1 = 2
    img17 = ImageTk.PhotoImage(Image.open(dados_quartas.s1_band.get()).resize((50, 30)))
    img18 = ImageTk.PhotoImage(Image.open(dados_quartas.s2_band.get()).resize((50, 30)))
    Label(frame_quartas, bg='white', textvariable=dados_quartas.s1_str, padx=2, justify=RIGHT, font="Verdana 10 bold").grid(row=quartas1, column=0, padx=2)
    lbl17 = Label(frame_quartas, bg='white', width=60, justify=LEFT)
    lbl17.configure(image=img17)
    lbl17.image = img17
    lbl17.grid(row=quartas1, column=1)
    quartas11 = Entry(frame_quartas, bg='white', width=3)
    quartas11.grid(row=quartas1, column=2, ipadx=2)
    Label(frame_quartas, bg='white', width=2, text='X').grid(row=quartas1, column=3)
    quartas12 = Entry(frame_quartas, bg='white', width=3)
    quartas12.grid(row=quartas1, column=4, ipadx=2)
    lbl18 = Label(frame_quartas, bg='white', width=60, justify=RIGHT)
    lbl18.configure(image=img18)
    lbl18.image = img18
    lbl18.grid(row=quartas1, column=5)
    Label(frame_quartas, bg='white', textvariable=dados_quartas.s2_str, padx=5, justify=LEFT, font="Verdana 10 bold").grid(row=quartas1, column=6, padx=2)

    # Segundo jogo------------------------------------------------------------------------------------------------------
    quartas2 = 3
    img19 = ImageTk.PhotoImage(Image.open(dados_quartas.s3_band.get()).resize((50, 30)))
    img20 = ImageTk.PhotoImage(Image.open(dados_quartas.s4_band.get()).resize((50, 30)))
    Label(frame_quartas, bg='white', textvariable=dados_quartas.s3_str, padx=2, justify=RIGHT, font="Verdana 10 bold").grid(row=quartas2, column=0, padx=2)
    lbl19 = Label(frame_quartas, bg='white', width=60, justify=LEFT)
    lbl19.configure(image=img19)
    lbl19.image = img19
    lbl19.grid(row=quartas2, column=1)
    quartas21 = Entry(frame_quartas, bg='white', width=3)
    quartas21.grid(row=quartas2, column=2, ipadx=2)
    Label(frame_quartas, bg='white', width=2, text='X').grid(row=quartas2, column=3)
    quartas22 = Entry(frame_quartas, bg='white', width=3)
    quartas22.grid(row=quartas2, column=4, ipadx=2)
    lbl20 = Label(frame_quartas, bg='white', width=60, justify=RIGHT)
    lbl20.configure(image=img20)
    lbl20.image = img20
    lbl20.grid(row=quartas2, column=5)
    Label(frame_quartas, bg='white', textvariable=dados_quartas.s4_str, padx=5, justify=LEFT, font="Verdana 10 bold").grid(row=quartas2, column=6, padx=2)

    # Terceiro jogo ----------------------------------------------------------------------------------------------------
    quartas3 = 4
    img21 = ImageTk.PhotoImage(Image.open(dados_quartas.s5_band.get()).resize((50, 30)))
    img22 = ImageTk.PhotoImage(Image.open(dados_quartas.s6_band.get()).resize((50, 30)))
    Label(frame_quartas, bg='white', textvariable=dados_quartas.s5_str, padx=2, justify=RIGHT, font="Verdana 10 bold").grid(row=quartas3, column=0, padx=2)
    lbl21 = Label(frame_quartas, bg='white', width=60, justify=LEFT)
    lbl21.configure(image=img21)
    lbl21.image = img21
    lbl21.grid(row=quartas3, column=1)
    quartas31 = Entry(frame_quartas, bg='white', width=3)
    quartas31.grid(row=quartas3, column=2, ipadx=2)
    Label(frame_quartas, bg='white', width=2, text='X').grid(row=quartas3, column=3)
    quartas32 = Entry(frame_quartas, bg='white', width=3)
    quartas32.grid(row=quartas3, column=4, ipadx=2)
    lbl22 = Label(frame_quartas, bg='white', width=60, justify=RIGHT)
    lbl22.configure(image=img22)
    lbl22.image = img22
    lbl22.grid(row=quartas3, column=5)
    Label(frame_quartas, bg='white', textvariable=dados_quartas.s6_str, padx=5, justify=LEFT, font="Verdana 10 bold").grid(row=quartas3, column=6, padx=2)

    # Quarto jogo------------------------------------------------------------------------------------------------------
    quartas4 = 5
    img23 = ImageTk.PhotoImage(Image.open(dados_quartas.s7_band.get()).resize((50, 30)))
    img24 = ImageTk.PhotoImage(Image.open(dados_quartas.s8_band.get()).resize((50, 30)))
    Label(frame_quartas, bg='white', textvariable=dados_quartas.s7_str, padx=2, justify=RIGHT, font="Verdana 10 bold").grid(row=quartas4, column=0, padx=2)
    lbl23 = Label(frame_quartas, bg='white', width=60, justify=LEFT)
    lbl23.configure(image=img23)
    lbl23.image = img23
    lbl23.grid(row=quartas4, column=1)
    quartas41 = Entry(frame_quartas, bg='white', width=3)
    quartas41.grid(row=quartas4, column=2, ipadx=2)
    Label(frame_quartas, bg='white', width=2, text='X').grid(row=quartas4, column=3)
    quartas42 = Entry(frame_quartas, bg='white', width=3)
    quartas42.grid(row=quartas4, column=4, ipadx=2)
    lbl24 = Label(frame_quartas, bg='white', width=60, justify=RIGHT)
    lbl24.configure(image=img24)
    lbl24.image = img24
    lbl24.grid(row=quartas4, column=5)
    Label(frame_quartas, bg='white', textvariable=dados_quartas.s8_str, padx=5, justify=LEFT, font="Verdana 10 bold").grid(row=quartas4, column=6, padx=2)

    # Botão de salvar resultados
    Label(frame_quartas, bg='white').grid(row=6, column=0)
    Button(frame_quartas, font="Verdana 10 bold", text="SALVAR", bd=0, padx=2, pady=2, bg="#405E38", fg="white",
           command=salvar_quartas).grid(row=7, column=0, columnspan=7)

    # Preenche as caixas de texto com os valores dos placares recuperadas do banco de dados ou valores padrão.
    quartas11.insert(0, dados_quartas.s1_gol.get())
    quartas12.insert(0, dados_quartas.s2_gol.get())
    quartas21.insert(0, dados_quartas.s3_gol.get())
    quartas22.insert(0, dados_quartas.s4_gol.get())
    quartas31.insert(0, dados_quartas.s5_gol.get())
    quartas32.insert(0, dados_quartas.s6_gol.get())
    quartas41.insert(0, dados_quartas.s7_gol.get())
    quartas42.insert(0, dados_quartas.s8_gol.get())


    # ------------------------------------------------------------------------------------------------------------------
    # Divide os dois frames (frame_quartas e frame_semifinais)
    Label(frame_quartas_semifinais_interno, bg='white').grid(row=1, column=0)

    # ------------------------------------------------------------------------------------------------------------------
    # Montagem do Frame de Semifinal
    frame_semifinais = Frame(frame_quartas_semifinais_interno, bg="white")
    frame_semifinais.grid_anchor(CENTER)
    frame_semifinais.grid(row=2, column=0)

    Label(frame_semifinais, fg="#405E38", bg="white", font="Verdana 12 bold", text="SEMIFINAIS").grid(row=0, column=0, columnspan=7)
    Label(frame_semifinais, bg='white').grid(row=1, column=0)


    # Primeiro jogo ----------------------------------------------------------------------------------------------------
    semifinal1 = 2
    img25 = ImageTk.PhotoImage(Image.open(dados_semifinal.s1_band.get()).resize((50, 30)))
    img26 = ImageTk.PhotoImage(Image.open(dados_semifinal.s2_band.get()).resize((50, 30)))
    Label(frame_semifinais, bg='white', textvariable=dados_semifinal.s1_str, padx=2, justify=RIGHT, font="Verdana 10 bold").grid(row=semifinal1, column=0, padx=2)
    lbl25 = Label(frame_semifinais, bg='white', width=60, justify=LEFT)
    lbl25.configure(image=img25)
    lbl25.image = img25
    lbl25.grid(row=semifinal1, column=1)
    semifinais11 = Entry(frame_semifinais, bg='white', width=3)
    semifinais11.grid(row=semifinal1, column=2, ipadx=2)
    Label(frame_semifinais, bg='white', width=2, text='X').grid(row=semifinal1, column=3)
    semifinais12 = Entry(frame_semifinais, bg='white', width=3)
    semifinais12.grid(row=semifinal1, column=4, ipadx=2)
    lbl26 = Label(frame_semifinais, bg='white', width=60, justify=RIGHT)
    lbl26.configure(image=img26)
    lbl26.image = img26
    lbl26.grid(row=semifinal1, column=5)
    Label(frame_semifinais, bg='white', textvariable=dados_semifinal.s2_str, padx=5, justify=LEFT, font="Verdana 10 bold").grid(row=semifinal1, column=6, padx=2)

    # Segundo jogo------------------------------------------------------------------------------------------------------
    semifinal2 = 3
    img27 = ImageTk.PhotoImage(Image.open(dados_semifinal.s3_band.get()).resize((50, 30)))
    img28 = ImageTk.PhotoImage(Image.open(dados_semifinal.s4_band.get()).resize((50, 30)))
    Label(frame_semifinais, bg='white', textvariable=dados_semifinal.s3_str, padx=2, justify=RIGHT, font="Verdana 10 bold").grid(row=semifinal2, column=0, padx=2)
    lbl27 = Label(frame_semifinais, bg='white', width=60, justify=LEFT)
    lbl27.configure(image=img27)
    lbl27.image = img27
    lbl27.grid(row=semifinal2, column=1)
    semifinais21 = Entry(frame_semifinais, bg='white', width=3)
    semifinais21.grid(row=semifinal2, column=2, ipadx=2)
    Label(frame_semifinais, bg='white', width=2, text='X').grid(row=semifinal2, column=3)
    semifinais22 = Entry(frame_semifinais, bg='white', width=3)
    semifinais22.grid(row=semifinal2, column=4, ipadx=2)
    lbl28 = Label(frame_semifinais, bg='white', width=60, justify=RIGHT)
    lbl28.configure(image=img28)
    lbl28.image = img28
    lbl28.grid(row=semifinal2, column=5)
    Label(frame_semifinais, bg='white', textvariable=dados_semifinal.s4_str, padx=5, justify=LEFT, font="Verdana 10 bold").grid(row=semifinal2, column=6, padx=2)

    Label(frame_quartas_semifinais, bg='white').grid(row=7, column=0)
    Button(frame_quartas_semifinais, font="Verdana 10 bold", text="SALVAR", bd=0, padx=2, pady=2, bg="#405E38",
           fg="white", command=salvar_semifinais).grid(row=8, column=0, columnspan=7)

    # Preenche as caixas de texto com os valores dos placares recuperadas do banco de dados ou com valores padrão.
    semifinais11.insert(0, dados_semifinal.s1_gol.get())
    semifinais12.insert(0, dados_semifinal.s2_gol.get())
    semifinais21.insert(0, dados_semifinal.s3_gol.get())
    semifinais22.insert(0, dados_semifinal.s4_gol.get())


    # ------------------------------------------------------------------------------------------------------------------
    # Montagem do Frame da FINAL!
    # A final possui dois frames: 1) disputa terceiro e quarto Lugar; 2) disputa primeiro e segundo.

    # Título do Frame
    Label(frame_final, fg="#405E38", bg="white", font="Verdana 18 bold", text="FINAL").grid(row=0, column=0)
    Label(frame_final, bg='white').grid(row=1, column=0)

    #Os frames de disputa de primeiro (linha 2) e terceiro lugar (linha 3) foram ampliados abaixo.

    frame_podio = Frame(frame_final, bg="white", width=400, height=100)
    frame_podio.grid_anchor(CENTER)
    frame_podio.grid(row=4, column=0)


    # Botão de salvar resultados
    Label(frame_final, bg='white').grid(row=5, column=0)
    Button(frame_final, font="Verdana 10 bold", text="SALVAR", bd=0, padx=2, pady=2, bg="#405E38", fg="white", command=salvar_final).grid(row=6, column=0)

    # ------------------------------------------------------------------------------------------------------------------
    # Montagem do frame de disputa de primeiro

    frame_disputa_primeiro = Frame(frame_final, bg="white", width=400, height=100)
    frame_disputa_primeiro.grid_anchor(CENTER)
    frame_disputa_primeiro.grid(row=2, column=0)

    Label(frame_disputa_primeiro, fg="#405E38", bg="white", font="Verdana 12 bold", text="DISPUTA DE PRIMEIRO LUGAR").grid(row=0, column=0, columnspan=7)
    Label(frame_disputa_primeiro, bg='white').grid(row=1, column=0)

    # Jogo
    final1 = 2
    img29 = ImageTk.PhotoImage(Image.open(dados_finais.s1_band.get()).resize((50, 30)))
    img30 = ImageTk.PhotoImage(Image.open(dados_finais.s2_band.get()).resize((50, 30)))
    Label(frame_disputa_primeiro, bg='white', textvariable=dados_finais.s1_str, padx=2, justify=RIGHT, font="Verdana 10 bold").grid(row=final1, column=0, padx=2)
    lbl29 = Label(frame_disputa_primeiro, bg='white', width=60, justify=LEFT)
    lbl29.configure(image=img29)
    lbl29.image = img29
    lbl29.grid(row=final1, column=1)
    final11 = Entry(frame_disputa_primeiro, bg='white', width=3)
    final11.grid(row=final1, column=2, ipadx=2)
    Label(frame_disputa_primeiro, bg='white', width=2, text='X').grid(row=final1, column=3)
    final12 = Entry(frame_disputa_primeiro, bg='white', width=3)
    final12.grid(row=final1, column=4, ipadx=2)
    lbl30 = Label(frame_disputa_primeiro, bg='white', width=60, justify=RIGHT)
    lbl30.configure(image=img30)
    lbl30.image = img30
    lbl30.grid(row=final1, column=5)
    Label(frame_disputa_primeiro, bg='white', textvariable=dados_finais.s2_str, padx=5, justify=LEFT, font="Verdana 10 bold").grid(row=final1, column=6, padx=2)


    # ------------------------------------------------------------------------------------------------------------------
    # Montagem do frame de disputa de terceiro

    frame_disputa_terceiro = Frame(frame_final, bg="white", width=400, height=100)
    frame_disputa_terceiro.grid_anchor(CENTER)
    frame_disputa_terceiro.grid(row=3, column=0)

    Label(frame_disputa_terceiro, bg='white').grid(row=0, column=0)
    Label(frame_disputa_terceiro, bg='white').grid(row=1, column=0)
    Label(frame_disputa_terceiro, fg="#405E38", bg="white", font="Verdana 12 bold", text="DISPUTA DE TERCEIRO LUGAR").grid(row=2, column=0, columnspan=7)
    Label(frame_disputa_terceiro, bg='white').grid(row=3, column=0)

    # Jogo
    final2 = 4
    img31 = ImageTk.PhotoImage(Image.open(dados_finais.s3_band.get()).resize((50, 30)))
    img32 = ImageTk.PhotoImage(Image.open(dados_finais.s4_band.get()).resize((50, 30)))
    Label(frame_disputa_terceiro, bg='white', textvariable=dados_finais.s3_str, padx=2, justify=RIGHT, font="Verdana 10 bold").grid(row=final2, column=0, padx=2)
    lbl31 = Label(frame_disputa_terceiro, bg='white', width=60, justify=LEFT)
    lbl31.configure(image=img31)
    lbl31.image = img31
    lbl31.grid(row=final2, column=1)
    final21 = Entry(frame_disputa_terceiro, bg='white', width=3)
    final21.grid(row=final2, column=2, ipadx=2)
    Label(frame_disputa_terceiro, bg='white', width=2, text='X').grid(row=final2, column=3)
    final22 = Entry(frame_disputa_terceiro, bg='white', width=3)
    final22.grid(row=final2, column=4, ipadx=2)
    lbl32 = Label(frame_disputa_terceiro, bg='white', width=60, justify=RIGHT)
    lbl32.configure(image=img32)
    lbl32.image = img32
    lbl32.grid(row=final2, column=5)
    Label(frame_disputa_terceiro, bg='white', textvariable=dados_finais.s4_str, padx=5, justify=LEFT, font="Verdana 10 bold").grid(row=final2, column=6, padx=2)

    # Preenche as caixas de texto com os valores dos placares recuperadas do banco de dados ou com valores padrão.
    final11.insert(0, dados_finais.s1_gol.get())
    final12.insert(0, dados_finais.s2_gol.get())
    final21.insert(0, dados_finais.s3_gol.get())
    final22.insert(0, dados_finais.s4_gol.get())


    # ------------------------------------------------------------------------------------------------------------------

    # Retornando à janela principal:
    # Por padrão, inicia com oitavas de final
    oitavas_final()

    # Montagem dos elementos estáticos
    janela2.mainloop()


def janela_quizz():
    """
    Manipula a janela do Quiz da Copa, seus dados, estilo e funcionamento
    geral. Nessa janela o usuário pode tentar responder a um quiz de 10
    questões, valendo 10 pontos cada resposta correta. A ordem das questões
    é aleatória e o usuário tem 4 opções de resposta.
    """
    # Essa função verifica se a resposta corresponde ao gabarito
    def verificar_resposta(resposta):

        # Verifica igualdade
        if str(resposta.get()) == str(gabarito.get()):
            messagebox.showinfo("CERTA RESPOSTA!!", "Você acertou!")
            pontuacao.set(str(int(pontuacao.get()) + 10))
        else:
            messagebox.showerror("RESPOSTA ERRADA!!", "Tente novamente!")


        # Desabilita botão de verificar
        btn_verificar_resposta.configure(state=DISABLED)

    # Função que atualiza informações para próxima pergunta
    def proxima_pergunta():
        """

        :return:
        """

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
    """
    Manipula a janela da funcionalidade Vidente, seus dados, estilo,
    botões e funcionamento. Nessa janela o usuário pode inserir o nome
    de duas seleções e o programa irá prever qual deles vencerá a disputa.
    """
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
    """
    Manipula a janela que expõe informações sobre o programa
    e os seus desenvolvedores, e controla o funcionamento dos
    seus botões e dados.
    """
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
g_inicial = Grupo('Grupo A')

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
button2 = Button(janela, text="FASE FINAL", bg='white', fg='black', width=9, height=1, bd=3, relief=SOLID, anchor=CENTER,
                 font="bold", command=janela_fase_final)
button3 = Button(janela, text="QUIZZ", bg='white', fg='black', width=7, height=1, bd=3, relief=SOLID, anchor=CENTER,
                 font="bold", command=janela_quizz)
button4 = Button(janela, text="VIDENTE", bg='white', fg='black', width=7, height=1, bd=3, relief=SOLID, anchor=CENTER,
                 font="bold", command=janela_vidente)
button5 = Button(janela, text="SOBRE", bg='white', fg='black', width=7, height=1, bd=3, relief=SOLID, anchor=CENTER,
                 font="bold", command=janela_sobre)

# Exibição dos botões na tela
button1_canvas = canvas.create_window(15, 150, anchor="nw", window=button1)
button2_canvas = canvas.create_window(120, 150, anchor="nw", window=button2)
button3_canvas = canvas.create_window(245, 150, anchor="nw", window=button3)
button4_canvas = canvas.create_window(350, 150, anchor="nw", window=button4)
button5_canvas = canvas.create_window(455, 150, anchor="nw", window=button5)

# Mensagem no rodapé do programa
label = Label(janela, font="Verdana 8 bold", text="Copyright ® - Todos os direitos reservados", anchor=S,
              justify=CENTER)
label.place(relx=0.24, rely=0.9, relwidth=0.5)

janela.mainloop()
