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


#-----------------------------------------------------------------------------
# JANELAS
def janela_grupos():
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
button1 = Button(janela, text="FASE DE GRUPOS", bg='white', fg='black', width=12, height=1, bd=3, relief=SOLID, anchor=CENTER, font="bold", command=janela_grupos)
button2 = Button(janela, text="QUIZZ", bg='white', fg='black', width=7, height=1, bd=3, relief=SOLID, anchor=CENTER, font="bold", command=janela_quizz)
button3 = Button(janela, text="VIDENTE", bg='white', fg='black', width=7, height=1, bd=3, relief=SOLID, anchor=CENTER, font="bold", command=janela_vidente)
button4 = Button(janela, text="SOBRE", bg='white', fg='black', width=7, height=1, bd=3, relief=SOLID, anchor=CENTER, font="bold", command=janela_sobre)

button1_canvas = canvas.create_window(20, 150, anchor="nw", window=button1)
button2_canvas = canvas.create_window(177, 150, anchor="nw", window=button2)
button3_canvas = canvas.create_window(282, 150, anchor="nw", window=button3)
button4_canvas = canvas.create_window(387, 150, anchor="nw", window=button4)

# Mensagem no rodapé do programa
label = Label(janela, font="Verdana 8 bold", text="Copyright ® - Todos os direitos reservados", anchor=S, justify=CENTER)
label.place(relx=0.24, rely=0.9, relwidth=0.5)

janela.mainloop()