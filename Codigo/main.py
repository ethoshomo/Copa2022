from tkinter import *
from PIL import Image, ImageTk
import pygame
import random


#-----------------------------------------------------------------------------
# FUNÇOES AUXILIARES

def quit(uma):
    uma.destroy()
def quit_musica(tela):
    pygame.mixer.music.stop()
    tela.destroy()
def quit_protocol(quitprot):
    pygame.mixer.music.stop()
    quitprot.destroy()
def prever(btn, cx1, cx2, res):
    btn['state'] = DISABLED
    resultado = random.randint(0, 101)
    if resultado > 50:
        res['text'] = cx1.get()
    else:
        res['text'] = cx2.get()
    pygame.mixer.music.stop()
def salvar():
    pass

# Converte as letras não ASCII de um alfabeto e os espaços também
def converte_palavra(palavra) :
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

#-----------------------------------------------------------------------------
# JANELAS
def janela_grupos():

    grupo_str = str("GRUPO A")

    # Interface de Banco de Dados com Variáveis

    # Selecao 1
    selecao1_nome = str("Brasil")
    selecao1_bandeira = "imagens/brasil.png"
    selecao1_pontos = str(0)
    selecao1_jogos = str(0)
    selecao1_vitorias = str(0)
    selecao1_empates = str(0)
    selecao1_derrotas = str(0)
    selecao1_gols_favoraveis = str(0)
    selecao1_gols_contrarios = str(0)

    # Selecao 2
    selecao2_nome = str("Alemanha")
    selecao2_bandeira = "imagens/campo.png"
    selecao2_pontos = str(1)
    selecao2_jogos = str(1)
    selecao2_vitorias = str(1)
    selecao2_empates = str(1)
    selecao2_derrotas = str(1)
    selecao2_gols_favoraveis = str(1)
    selecao2_gols_contrarios = str(1)

    # Selecao 3
    selecao3_nome = str("Portugal")
    selecao3_bandeira = "imagens/estadio.png"
    selecao3_pontos = str(2)
    selecao3_jogos = str(2)
    selecao3_vitorias = str(2)
    selecao3_empates = str(2)
    selecao3_derrotas = str(2)
    selecao3_gols_favoraveis = str(2)
    selecao3_gols_contrarios = str(2)

    # Selecao 4
    selecao4_nome = str("Espanha")
    selecao4_bandeira = "imagens/vidente.png"
    selecao4_pontos = str(3)
    selecao4_jogos = str(3)
    selecao4_vitorias = str(3)
    selecao4_empates = str(3)
    selecao4_derrotas = str(3)
    selecao4_gols_favoraveis = str(3)
    selecao4_gols_contrarios = str(3)

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
    #-----------------------------------------------------------------------------
    # Frame de Grupos
    frame = Frame(janela2, bg="white")
    frame.grid_anchor(CENTER)
    frame.place(relx=0.05, rely=0.03, relwidth=0.9, relheight=0.05)

    # Botões dos Grupos
    btn_grupo_a = Button(frame, font="Verdana 10 bold",
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


    # -----------------------------------------------------------------------------
    # Frame de jogos
    jogos = Frame(janela2, bg="white")
    jogos.grid_anchor(CENTER)
    jogos.place(relx=0.05, rely=0.10, relwidth=0.9, relheight=0.50)

    Label(jogos, padx=2, justify=CENTER, text=grupo_str, font="Verdana 12 bold", bg="white", fg="#405E38",).grid(row=0, column=0, columnspan=7, padx=2)

    # Primeiro jogo
    linha1 = 1
    img1 = ImageTk.PhotoImage(Image.open(selecao1_bandeira).resize((50, 30)))
    img2 = ImageTk.PhotoImage(Image.open(selecao2_bandeira).resize((50, 30)))
    Label(jogos, bg='white', text=selecao1_nome, padx=2, justify=RIGHT, font="Verdana 10 bold").grid(row=linha1, column=0, padx=2)
    Label(jogos, bg='white', width=60, justify=LEFT, image=img1).grid(row=linha1, column=1)
    resultado11 = Entry(jogos, bg='white', width=3)
    resultado11.grid(row=linha1, column=2, ipadx=2)
    Label(jogos, bg='white', width=2, text='X').grid(row=linha1, column=3)
    resultado12 = Entry(jogos, bg='white', width=3)
    resultado12.grid(row=linha1, column=4, ipadx=2)
    Label(jogos, bg='white', width=60, justify=RIGHT, image=img2).grid(row=linha1, column=5)
    Label(jogos, bg='white', text=selecao2_nome, padx=5, justify=LEFT, font="Verdana 10 bold").grid(row=linha1, column=6, padx=2)

    # Segundo jogo
    linha2 = 2
    img3 = ImageTk.PhotoImage(Image.open(selecao3_bandeira).resize((50, 30)))
    img4 = ImageTk.PhotoImage(Image.open(selecao4_bandeira).resize((50, 30)))
    Label(jogos, bg='white', text=selecao3_nome, padx=2, justify=RIGHT, font="Verdana 10 bold").grid(row=linha2, column=0, padx=2)
    Label(jogos, bg='white', width=60, justify=LEFT, image=img3).grid(row=linha2, column=1)
    resultado21 = Entry(jogos, bg='white', width=3)
    resultado21.grid(row=linha2, column=2, ipadx=2)
    Label(jogos, bg='white', width=2, text='X').grid(row=linha2, column=3)
    resultado22 = Entry(jogos, bg='white', width=3)
    resultado22.grid(row=linha2, column=4, ipadx=2)
    Label(jogos, bg='white', width=60, justify=RIGHT, image=img4).grid(row=linha2, column=5)
    Label(jogos, bg='white', text=selecao4_nome, padx=5, justify=LEFT, font="Verdana 10 bold").grid(row=linha2, column=6, padx=2)

    # Terceiro jogo
    linha3 = 3
    img5 = ImageTk.PhotoImage(Image.open(selecao1_bandeira).resize((50, 30)))
    img6 = ImageTk.PhotoImage(Image.open(selecao3_bandeira).resize((50, 30)))
    Label(jogos, bg='white', text=selecao1_nome, padx=2, justify=RIGHT, font="Verdana 10 bold").grid(row=linha3, column=0, padx=2)
    Label(jogos, bg='white', width=60, justify=LEFT, image=img5).grid(row=linha3, column=1)
    resultado31 = Entry(jogos, bg='white', width=3)
    resultado31.grid(row=linha3, column=2, ipadx=2)
    Label(jogos, bg='white', width=2, text='X').grid(row=linha3, column=3)
    resultado32 = Entry(jogos, bg='white', width=3)
    resultado32.grid(row=linha3, column=4, ipadx=2)
    Label(jogos, bg='white', width=60, justify=RIGHT, image=img6).grid(row=linha3, column=5)
    Label(jogos, bg='white', text=selecao3_nome, padx=5, justify=LEFT, font="Verdana 10 bold").grid(row=linha3, column=6, padx=2)

    # Quarto jogo
    linha4 = 4
    img7 = ImageTk.PhotoImage(Image.open(selecao4_bandeira).resize((50, 30)))
    img8 = ImageTk.PhotoImage(Image.open(selecao2_bandeira).resize((50, 30)))
    Label(jogos, bg='white', text=selecao4_nome, padx=2, justify=RIGHT, font="Verdana 10 bold").grid(row=linha4, column=0, padx=2)
    Label(jogos, bg='white', width=60, justify=LEFT, image=img7).grid(row=linha4, column=1)
    resultado41 = Entry(jogos, bg='white', width=3)
    resultado41.grid(row=linha4, column=2, ipadx=2)
    Label(jogos, bg='white', width=2, text='X').grid(row=linha4, column=3)
    resultado42 = Entry(jogos, bg='white', width=3)
    resultado42.grid(row=linha4, column=4, ipadx=2)
    Label(jogos, bg='white', width=60, justify=RIGHT, image=img8).grid(row=linha4, column=5)
    Label(jogos, bg='white', text=selecao2_nome, padx=5, justify=LEFT, font="Verdana 10 bold").grid(row=linha4, column=6, padx=2)

    # Quinto jogo
    linha5 = 5
    img9 = ImageTk.PhotoImage(Image.open(selecao4_bandeira).resize((50, 30)))
    img10 = ImageTk.PhotoImage(Image.open(selecao1_bandeira).resize((50, 30)))
    Label(jogos, bg='white', text=selecao4_nome, padx=2, justify=RIGHT, font="Verdana 10 bold").grid(row=linha5, column=0, padx=2)
    Label(jogos, bg='white', width=60, justify=LEFT, image=img9).grid(row=linha5, column=1)
    resultado51 = Entry(jogos, bg='white', width=3)
    resultado51.grid(row=linha5, column=2, ipadx=2)
    Label(jogos, bg='white', width=2, text='X').grid(row=linha5, column=3)
    resultado52 = Entry(jogos, bg='white', width=3)
    resultado52.grid(row=linha5, column=4, ipadx=2)
    Label(jogos, bg='white', width=60, justify=RIGHT, image=img10).grid(row=linha5, column=5)
    Label(jogos, bg='white', text=selecao1_nome, padx=5, justify=LEFT, font="Verdana 10 bold").grid(row=linha5, column=6, padx=2)

    # Sexto jogo
    linha6 = 6
    img11 = ImageTk.PhotoImage(Image.open(selecao2_bandeira).resize((50, 30)))
    img12 = ImageTk.PhotoImage(Image.open(selecao3_bandeira).resize((50, 30)))
    Label(jogos, bg='white', text=selecao2_nome, padx=2, justify=RIGHT, font="Verdana 10 bold").grid(row=linha6, column=0, padx=2)
    Label(jogos, bg='white', width=60, justify=LEFT, image=img11).grid(row=linha6, column=1)
    resultado61 = Entry(jogos, bg='white', width=3)
    resultado61.grid(row=linha6, column=2, ipadx=2)
    Label(jogos, bg='white', width=2, text='X').grid(row=linha6, column=3)
    resultado62 = Entry(jogos, bg='white', width=3)
    resultado62.grid(row=linha6, column=4, ipadx=2)
    Label(jogos, bg='white', width=60, justify=RIGHT, image=img12).grid(row=linha6, column=5)
    Label(jogos, bg='white', text=selecao3_nome, padx=5, justify=LEFT, font="Verdana 10 bold").grid(row=linha6, column=6, padx=2)

    # Salvar informações
    btn_salvar = Button(jogos, font="Verdana 10 bold", text="SALVAR", bd=0, padx=2, pady=2, bg="#405E38", fg="white", command=salvar)
    btn_salvar.grid(row=7, column=2, columnspan=3, padx=1)


    # -----------------------------------------------------------------------------
    # Frame da Tabela dos Grupos
    frame_grupos = Frame(janela2, bg="white")
    frame_grupos.grid_anchor(CENTER)
    frame_grupos.place(relx=0.05, rely=0.62, relwidth=0.9, relheight=0.35)

    # Título do Frame
    Label(frame_grupos, text="TABELA DO GRUPO", font="Verdana 12 bold", bg="white", fg="#405E38", padx=5, pady=5, height=1, justify=LEFT).grid(row=0, column=0, columnspan=8)

    # AQUI FAZEMOS A DEFINIÇÃO DAS CLASSIFICAÇÕES NA TABELA
    # ATENÇÃO QUE EXISTE UMA DIFERENÇA DE LINHAS, AFINAL A TABELA DO GRID COMEÇA NA LINHA "TABELA DO GRUPO"
    # DESSE MODO, O PRIMEIRO COLOCADO FICA NA LINHA 2; SEGUNDO, NA 3; TERCEIRO, NA 4; QUARTO, NA 5.
    colocacaoA = int(4); # Colocação da Seleção 1
    colocacaoB = int(3) # Colocação da Seleção 2
    colocacaoC = int(5) # Colocação da Seleção 3
    colocacaoD = int(2)  # Colocação da Seleção 4


    # Primeira Linha da Tabela de Jogos - Cabeçalho
    posicaoA = int(1)
    Label(frame_grupos, bg="#405E38", fg='white', text='Classificação', width=30, padx=2, justify=LEFT, font="Verdana 9 bold").grid(row=posicaoA, column=1)
    Label(frame_grupos, bg="#405E38", fg='white', text='P', width=6, padx=2, justify=LEFT, font="Verdana 9 bold").grid(row=posicaoA, column=2)
    Label(frame_grupos, bg="#405E38", fg='white', text='J', width=6, padx=2, justify=LEFT, font="Verdana 9 bold").grid(row=posicaoA, column=3)
    Label(frame_grupos, bg="#405E38", fg='white', text='V', width=6, padx=2, justify=LEFT, font="Verdana 9 bold").grid(row=posicaoA, column=4)
    Label(frame_grupos, bg="#405E38", fg='white', text='E', width=6, padx=2, justify=LEFT, font="Verdana 9 bold").grid(row=posicaoA, column=5)
    Label(frame_grupos, bg="#405E38", fg='white', text='D', width=6, padx=2, justify=LEFT, font="Verdana 9 bold").grid(row=posicaoA, column=6)
    Label(frame_grupos, bg="#405E38", fg='white', text='GP', width=6, padx=2, justify=LEFT, font="Verdana 9 bold").grid(row=posicaoA, column=7)
    Label(frame_grupos, bg="#405E38", fg='white', text='GC', width=6, padx=2, justify=LEFT, font="Verdana 9 bold").grid(row=posicaoA, column=8)

    # Montando a Coluna 0 (a classificação é fixa)
    Label(frame_grupos, bg="#405E38", fg='white', text='1', width=3, padx=2, justify=LEFT, font="Verdana 8 bold").grid(row=2, column=0, padx=2)
    Label(frame_grupos, bg="#405E38", fg='white', text='2', width=3, padx=2, justify=LEFT, font="Verdana 8 bold").grid(row=3, column=0, padx=2)
    Label(frame_grupos, bg="#405E38", fg='white', text='3', width=3, padx=2, justify=LEFT, font="Verdana 8 bold").grid(row=4, column=0, padx=2)
    Label(frame_grupos, bg="#405E38", fg='white', text='4', width=3, padx=2, justify=LEFT, font="Verdana 8 bold").grid(row=5, column=0, padx=2)


    # Dados da Primeira Seleção
    Label(frame_grupos, bg='white', fg='black', text=selecao1_nome, width=30, padx=2, justify=LEFT, font="Verdana 9 bold").grid(row=colocacaoA, column=1)
    Label(frame_grupos, bg='white', fg='black', text=selecao1_pontos, width=6, padx=2, justify=LEFT, font="Verdana 9 bold").grid(row=colocacaoA, column=2)
    Label(frame_grupos, bg='white', fg='black', text=selecao1_jogos, width=6, padx=2, justify=LEFT, font="Verdana 9 bold").grid(row=colocacaoA, column=3)
    Label(frame_grupos, bg='white', fg='black', text=selecao1_vitorias, width=6, padx=2, justify=LEFT, font="Verdana 9 bold").grid(row=colocacaoA, column=4)
    Label(frame_grupos, bg='white', fg='black', text=selecao1_empates, width=6, padx=2, justify=LEFT, font="Verdana 9 bold").grid(row=colocacaoA, column=5)
    Label(frame_grupos, bg='white', fg='black', text=selecao1_derrotas, width=6, padx=2, justify=LEFT, font="Verdana 9 bold").grid(row=colocacaoA, column=6)
    Label(frame_grupos, bg='white', fg='black', text=selecao1_gols_favoraveis, width=6, padx=2, justify=LEFT, font="Verdana 9 bold").grid(row=colocacaoA, column=7)
    Label(frame_grupos, bg='white', fg='black', text=selecao1_gols_contrarios, width=6, padx=2, justify=LEFT, font="Verdana 9 bold").grid(row=colocacaoA, column=8)

    # Dados da Segunda Seleção
    Label(frame_grupos, bg='white', fg='black', text=selecao2_nome, width=30, padx=2, justify=LEFT, font="Verdana 9 bold").grid(row=colocacaoB, column=1)
    Label(frame_grupos, bg='white', fg='black', text=selecao2_pontos, width=6, padx=2, justify=LEFT, font="Verdana 9 bold").grid(row=colocacaoB, column=2)
    Label(frame_grupos, bg='white', fg='black', text=selecao2_jogos, width=6, padx=2, justify=LEFT, font="Verdana 9 bold").grid(row=colocacaoB, column=3)
    Label(frame_grupos, bg='white', fg='black', text=selecao2_vitorias, width=6, padx=2, justify=LEFT, font="Verdana 9 bold").grid(row=colocacaoB, column=4)
    Label(frame_grupos, bg='white', fg='black', text=selecao2_empates, width=6, padx=2, justify=LEFT, font="Verdana 9 bold").grid(row=colocacaoB, column=5)
    Label(frame_grupos, bg='white', fg='black', text=selecao2_derrotas, width=6, padx=2, justify=LEFT, font="Verdana 9 bold").grid(row=colocacaoB, column=6)
    Label(frame_grupos, bg='white', fg='black', text=selecao2_gols_favoraveis, width=6, padx=2, justify=LEFT, font="Verdana 9 bold").grid(row=colocacaoB, column=7)
    Label(frame_grupos, bg='white', fg='black', text=selecao2_gols_contrarios, width=6, padx=2, justify=LEFT, font="Verdana 9 bold").grid(row=colocacaoB, column=8)

    # Dados da Terceira Seleção
    Label(frame_grupos, bg='white', fg='black', text=selecao3_nome, width=30, padx=2, justify=LEFT, font="Verdana 9 bold").grid(row=colocacaoC, column=1)
    Label(frame_grupos, bg='white', fg='black', text=selecao3_pontos, width=6, padx=2, justify=LEFT, font="Verdana 9 bold").grid(row=colocacaoC, column=2)
    Label(frame_grupos, bg='white', fg='black', text=selecao3_jogos, width=6, padx=2, justify=LEFT, font="Verdana 9 bold").grid(row=colocacaoC, column=3)
    Label(frame_grupos, bg='white', fg='black', text=selecao3_vitorias, width=6, padx=2, justify=LEFT, font="Verdana 9 bold").grid(row=colocacaoC, column=4)
    Label(frame_grupos, bg='white', fg='black', text=selecao3_empates, width=6, padx=2, justify=LEFT, font="Verdana 9 bold").grid(row=colocacaoC, column=5)
    Label(frame_grupos, bg='white', fg='black', text=selecao3_derrotas, width=6, padx=2, justify=LEFT, font="Verdana 9 bold").grid(row=colocacaoC, column=6)
    Label(frame_grupos, bg='white', fg='black', text=selecao3_gols_favoraveis, width=6, padx=2, justify=LEFT, font="Verdana 9 bold").grid(row=colocacaoC, column=7)
    Label(frame_grupos, bg='white', fg='black', text=selecao3_gols_contrarios, width=6, padx=2, justify=LEFT, font="Verdana 9 bold").grid(row=colocacaoC, column=8)

    # Dados da Quarta Seleção
    Label(frame_grupos, bg='white', fg='black', text=selecao4_nome, width=30, padx=2, justify=LEFT, font="Verdana 9 bold").grid(row=colocacaoD, column=1)
    Label(frame_grupos, bg='white', fg='black', text=selecao4_pontos, width=6, padx=2, justify=LEFT, font="Verdana 9 bold").grid(row=colocacaoD, column=2)
    Label(frame_grupos, bg='white', fg='black', text=selecao4_jogos, width=6, padx=2, justify=LEFT, font="Verdana 9 bold").grid(row=colocacaoD, column=3)
    Label(frame_grupos, bg='white', fg='black', text=selecao4_vitorias, width=6, padx=2, justify=LEFT, font="Verdana 9 bold").grid(row=colocacaoD, column=4)
    Label(frame_grupos, bg='white', fg='black', text=selecao4_empates, width=6, padx=2, justify=LEFT, font="Verdana 9 bold").grid(row=colocacaoD, column=5)
    Label(frame_grupos, bg='white', fg='black', text=selecao4_derrotas, width=6, padx=2, justify=LEFT, font="Verdana 9 bold").grid(row=colocacaoD, column=6)
    Label(frame_grupos, bg='white', fg='black', text=selecao4_gols_favoraveis, width=6, padx=2, justify=LEFT, font="Verdana 9 bold").grid(row=colocacaoD, column=7)
    Label(frame_grupos, bg='white', fg='black', text=selecao4_gols_contrarios, width=6, padx=2, justify=LEFT, font="Verdana 9 bold").grid(row=colocacaoD, column=8)


    janela2.mainloop()
def janela_quizz():
    pergunta = str("Pergunta para o QUIZZ. Ficou boa a interface? Acho que devo fazer uma pergunta gigantesca para testar todas as possibilidades de erro.")
    resposta1 = str("CLARO!!")
    resposta2 = str("NÃO SEI AINDA!!")
    resposta3 = str("ESTÁ MUITO PROFISSIONAL!! rs")
    resposta4 = str("FICOU HORRÍVEL!!!")
    pontuacao = str(10)

    janela2 = Toplevel()
    janela2.title("SHOW DE BOLA - QUIZZ")
    janela2.configure(background='#4A2A2D')
    janela2.geometry("800x400+200+200")
    janela2.transient(janela)
    janela2.focus_force()
    janela2.grab_set()
    janela2.resizable(False, False)

    # Personaliza o background
    bg = ImageTk.PhotoImage(Image.open('imagens/estadio.png').resize((800, 400)))
    canvas = Canvas(janela2, width=800, height=400)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg, anchor="nw")

    # Exibe o título do corpo da janela
    label_titulo = Label(janela2,
                         text="QUIZZ",
                         font="Verdana 20 bold",
                         bg="#0E0405",
                         fg="#911724")
    label_titulo.place(anchor=N, rely=0.05, relx=0.5, relwidth=0.9)


    # QUIZZ
    frame_quiz = Frame(janela2, bg="#0E0405")
    frame_quiz.grid_anchor(CENTER)
    frame_quiz.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.6)
    var = IntVar()

    label_pergunta = Label(frame_quiz,
                           text="PERGUNTA:",
                           font="Verdana 14 bold",
                           bg="#0E0405",
                           fg="#911724",
                           padx=5,
                           pady=5,
                           height=2,
                           justify=LEFT)
    label_pergunta.grid(row=0, column=0, sticky=E)

    label_questao = Label(frame_quiz,
                           text=pergunta,
                           font="Verdana 10 bold",
                           bg="#0E0405",
                           fg="white",
                           height=4,
                           justify=LEFT,
                           wraplength=500)
    label_questao.grid(row=0, column=1, sticky=W)

    #Opcao 1
    radiobtn1 = Radiobutton(frame_quiz,
                            variable=var,
                            bd=0,
                            padx=0,
                            pady=0,
                            bg="#0E0405",
                            value=1)
    radiobtn1.grid(row=1, column=0, sticky=E)
    label_resposta4 = Label(frame_quiz,
                            text=resposta1,
                            font="Verdana 10 bold",
                            bg="#0E0405",
                            fg="white",
                            wraplength=400)
    label_resposta4.grid(row=1, column=1, sticky=W)

    #Opcao 2
    radiobtn2 = Radiobutton(frame_quiz,
                            variable=var,
                            bd=0,
                            padx=0,
                            pady=0,
                            bg="#0E0405",
                            value=2)
    radiobtn2.grid(row=2, column=0, sticky=E)
    label_resposta4 = Label(frame_quiz,
                            text=resposta2,
                            font="Verdana 10 bold",
                            bg="#0E0405",
                            fg="white",
                            wraplength=400)
    label_resposta4.grid(row=2, column=1, sticky=W)

    #Opcao 3
    radiobtn3 = Radiobutton(frame_quiz,
                            variable=var,
                            bd=0,
                            padx=0,
                            pady=0,
                            bg="#0E0405",
                            value=3)
    radiobtn3.grid(row=3, column=0, sticky=E)
    label_resposta4 = Label(frame_quiz,
                            text=resposta3,
                            font="Verdana 10 bold",
                            bg="#0E0405",
                            fg="white",
                            wraplength=400)
    label_resposta4.grid(row=3, column=1, sticky=W)

    #Opcao 4
    radiobtn4 = Radiobutton(frame_quiz,
                            variable=var,
                            bd=0,
                            padx=0,
                            pady=0,
                            bg="#0E0405",
                            value=4)
    radiobtn4.grid(row=4, column=0, sticky=E)
    label_resposta4 = Label(frame_quiz,
                            text=resposta4,
                            font="Verdana 10 bold",
                            bg="#0E0405",
                            fg="white",
                            wraplength=400)
    label_resposta4.grid(row=4, column=1, sticky=W)

    # Verificar Resposta
    btn_avancar = Button(frame_quiz,
                         font="Verdana 10 bold",
                         text="VERIFICAR RESPOSTA",
                         bd=0,
                         padx=2,
                         pady=2,
                         bg="#911724",
                         fg="white",
                         command=lambda: quit(janela2))
    btn_avancar.grid(row=6, columnspan=2, padx=2, pady=10)

    # Frame de Rodapé
    frame = Frame(janela2, bg="#0E0405")
    frame.grid_anchor(CENTER)
    frame.place(relx=0.05, rely=0.9, relwidth=0.9)

    # Label Pontuação
    str_pontuacao = "Pontuacao total: " + pontuacao
    label_pontuacao = Label(frame,
                            font="Verdana 8 bold",
                            text=str_pontuacao,
                            bd=0,
                            padx=1,
                            pady=1,
                            width=30,
                            bg="#0E0405",
                            fg="white",
                            anchor=CENTER)
    label_pontuacao.grid(row=0, column=0, padx=5)

    # Botão Próxima Pergunta
    btn_avancar = Button(frame,
                      font="Verdana 10 bold",
                      text="PROXIMA PERGUNTA",
                      bd=0,
                      padx=2,
                      pady=2,
                      bg="#911724",
                      fg="white",
                      command=lambda: quit(janela2))
    btn_avancar.grid(row=0, column=1, padx=2)

    # Botão retornar
    btn_sair = Button(frame,
                      font="Verdana 10 bold",
                      text="RETORNAR MENU",
                      bd=0,
                      padx=2,
                      pady=2,
                      bg="#911724",
                      fg="white",
                      command=lambda: quit(janela2))
    btn_sair.grid(row=0, column=2, padx=2)

    janela2.mainloop()
def janela_vidente():
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
    btn_prever = Button(janela2,
                        text="PREVER O FUTURO",
                        bd=0,
                        padx=0,
                        pady=0,
                        bg="#9f7c59",
                        fg="#5e3414",
                        command=lambda: prever(btn_prever, caixa1, caixa2, label_resultado_valor))
    btn_prever.place(relx=0.55, rely=0.56, relwidth=0.4)

    # Porção que indica o resultado
    label_resultado = Label(janela2,
                            text="RESULTADO: ",
                            font="Verdana 8 bold",
                            bg="#9f7c59",
                            fg="#5e3414")
    label_resultado.place(anchor=N, rely=0.65, relx=0.75, relwidth=0.4)
    label_resultado_valor = Label(janela2, justify=CENTER, anchor=CENTER)
    label_resultado_valor.place(relx=0.55, rely=0.63, relwidth=0.4)

    # Botão retornar
    btn_sair = Button(janela2,
                      text="RETORNAR MENU",
                      bd=0,
                      padx=0,
                      pady=0,
                      bg="#9f7c59",
                      fg="#5e3414",
                      command=lambda: quit_musica(janela2))
    btn_sair.place(relx=0.35, rely=0.85, relwidth=0.3)

    #Ao fechar a janela, utiliza protocolo de saida.
    janela2.protocol("WM_DELETE_WINDOW", lambda:quit_protocol(janela2))
    janela2.mainloop()
def janela_sobre():
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
    informacoes = Label(janela2,
                        anchor=CENTER,
                        justify=LEFT,
                        width=200,
                        bd=1,
                        relief=SOLID,
                        bg="white",
                        fg='black',
                        font="Verdana 8 bold",
                        text=info,
                        padx=10,
                        pady=10)
    informacoes.place(relx=0.05, rely=0.10, relwidth=0.9)

    # Botao de retorno
    btn_sair = Button(janela2,
                      text="RETORNAR MENU",
                      bg='white',
                      fg='black',
                      width=7,
                      height=1,
                      bd=3,
                      relief=SOLID,
                      anchor=CENTER,
                      font="bold",
                      command=lambda: quit(janela2))
    btn_sair.place(relx=0.35, rely=0.85, relwidth=0.3)

    janela2.mainloop()


#Criação da Janela e suas configurações
janela = Tk()
p1 = PhotoImage(file="imagens/icone.png")
janela.iconphoto(False, p1)
janela.geometry("600x300+300+300")
janela.title("Show de Bola!!")
janela.resizable(False, False)

# Imagem de fundo
bg = ImageTk.PhotoImage(Image.open('imagens/menu.png').resize((800, 300)))
canvas = Canvas(janela, width=700, height=300)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg, anchor="nw")

# Opções do Menu
button1 = Button(janela,
                 text="FASE DE GRUPOS",
                 bg='white', fg='black',
                 width=12,
                 height=1,
                 bd=3,
                 relief=SOLID,
                 anchor=CENTER,
                 font="bold",
                 command=janela_grupos)
button2 = Button(janela,
                 text="QUIZZ",
                 bg='white',
                 fg='black',
                 width=7,
                 height=1,
                 bd=3,
                 relief=SOLID,
                 anchor=CENTER,
                 font="bold",
                 command=janela_quizz)
button3 = Button(janela,
                 text="VIDENTE",
                 bg='white',
                 fg='black',
                 width=7,
                 height=1,
                 bd=3,
                 relief=SOLID,
                 anchor=CENTER,
                 font="bold",
                 command=janela_vidente)
button4 = Button(janela,
                 text="SOBRE",
                 bg='white',
                 fg='black',
                 width=7,
                 height=1,
                 bd=3,
                 relief=SOLID,
                 anchor=CENTER,
                 font="bold",
                 command=janela_sobre)

button1_canvas = canvas.create_window(20, 150, anchor="nw", window=button1)
button2_canvas = canvas.create_window(177, 150, anchor="nw", window=button2)
button3_canvas = canvas.create_window(282, 150, anchor="nw", window=button3)
button4_canvas = canvas.create_window(387, 150, anchor="nw", window=button4)

# Mensagem no rodapé do programa
label = Label(janela, font="Verdana 8 bold", text="Copyright ® - Todos os direitos reservados", anchor=S, justify=CENTER)
label.place(relx=0.24, rely=0.9, relwidth=0.5)

janela.mainloop()
