import tkinter
from tkinter import *
from tkinter import ttk

############################################# CORES ######################################################

roxoclaro = "#9400D3"
preto = "#000000"
vermelho = "#8B0000"
laranjaclaro = "#FFCC99"
roxoescuro = "#8B008B"
laranjaescuro = "#FF4500"
azul = "#0000FF"

######################################## TELA PRINCIPAL ################################################

janela = Tk()
janela.title("")
janela.geometry("800x500")
janela.configure(bg=laranjaescuro)


################################### DIVISÃO DOS FRAMES ################################################


frame_esquerda = Frame(janela, width=200, height=500,
                       bg=roxoescuro, relief="raised")
frame_esquerda.grid(row=0, column=0, sticky=NW, padx=0, pady=0)


frame_meio = Frame(janela, width=400, height=500,
                   bg=laranjaescuro, relief="flat")
frame_meio.grid(row=0, column=1, sticky=NW, padx=1, pady=1)

frame_direita = Frame(janela, width=800, height=500,
                      bg=roxoescuro, relief="flat")
frame_direita.grid(row=0, column=2, sticky=NW, padx=0, pady=0)


################################### FRAME DA ESQUERDA #####################################################
app_x = Label(frame_esquerda, text="X", height=1, relief="flat",
              anchor="center", font=("Ivy 80 bold"), bg=roxoescuro, fg=vermelho)
app_x.place(x=60, y=80)

app_x = Label(frame_esquerda, text="Jogador 1", height=1, relief="flat",
              anchor="center", font=("Courier 16 bold"), bg=roxoescuro, fg=preto)
app_x.place(x=40, y=200)

app_x_pontos = Label(frame_esquerda, text="0", height=1, relief="flat",
                     anchor="center", font=("Ivy 65 bold"), bg=roxoescuro, fg=preto)
app_x_pontos.place(x=70, y=250)

app_x = Label(frame_esquerda, text="Pontos", height=1, relief="flat",
              anchor="center", font=("Courier 16 bold"), bg=roxoescuro, fg=preto)
app_x.place(x=55, y=350)

####################################### FRAME DO MEIO ###################################################


app_titulo = Label(frame_meio, text=" BEM VINDO AO NOSSO JOGO !!", height=1, relief="flat",
                   anchor="center", font=("Courier 18 bold"), bg=laranjaescuro, fg=preto)
app_titulo.place(x=10, y=30)

"""app_titulo = Label(frame_meio, text=" POR FAVOR ", height=1, relief="flat",
                   anchor="center", font=("Courier 18 bold"), bg=laranjaescuro, fg=preto)
app_titulo.place(x=110, y=60)"""

app_titulo = Label(frame_meio, text=" SELECIONE UMA OPÇÃO: ", height=1, relief="flat",
                   anchor="center", font=("Courier 18 bold"), bg=laranjaescuro, fg=preto)
app_titulo.place(x=40, y=100)

####################################### FRAME DA DIREITA ####################################################

app_o = Label(frame_direita, text="O", height=1, relief="flat",
              anchor="center", font=("Ivy 80 bold"), bg=roxoescuro, fg=azul)
app_o.place(x=60, y=80)

app_o = Label(frame_direita, text="Jogador 2", height=1, relief="flat",
              anchor="center", font=("Courier 16 bold"), bg=roxoescuro, fg=preto)
app_o.place(x=40, y=200)

app_o_pontos = Label(frame_direita, text="0", height=1, relief="flat",
                     anchor="center", font=("Ivy 65 bold"), bg=roxoescuro, fg=preto)
app_o_pontos.place(x=70, y=250)

app_o = Label(frame_direita, text="Pontos", height=1, relief="flat",
              anchor="center", font=("Courier 16 bold"), bg=roxoescuro, fg=preto)
app_o.place(x=55, y=350)


########################################### LÓGICA DO JOGO ##################################################

jogador_1 = "X"
jogador_2 = "O"

score_1 = 0
score_2 = 0

tabela = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

jogando = 'X'
joga = ''
contador = 0
contador_de_rodada = 0


def sair_jogo():
    b_jogar1p.destroy()
    b_jogar2p.destroy()
    encerramento = Label(frame_meio, text="Programa finalizado",
                         font="arial 14", background="purple", foreground="white")
    encerramento.pack()


def iniciar_jogo():
    b_jogar1p.place(x=800, y=350)
    if b_jogar2p == iniciar_jogo:
        escolher_simbolo()
    b_jogar2p.destroy()
    sair_jogo.destroy()
    app_titulo.destroy()

    def controlar(i):
        global jogando
        global contador
        global jogar

        if i == str(1):
            if b_0['text'] == '':

                if jogando == 'X':
                    cor = vermelho
                if jogando == 'O':
                    cor = azul

                b_0['fg'] = cor  # Cor da Posição
                b_0['text'] = jogando  # Texto da Posição
                tabela[0][0] = jogando  # Valor Posição

                if jogando == 'X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                contador += 1

        if i == str(2):
            if b_1['text'] == '':

                if jogando == 'X':
                    cor = vermelho
                if jogando == 'O':
                    cor = azul

                b_1['fg'] = cor
                b_1['text'] = jogando
                tabela[0][1] = jogando

                if jogando == 'X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                contador += 1

        if i == str(3):
            if b_2['text'] == '':

                if jogando == 'X':
                    cor = vermelho
                if jogando == 'O':
                    cor = azul

                b_2['fg'] = cor
                b_2['text'] = jogando
                tabela[0][2] = jogando

                if jogando == 'X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'
                contador += 1

        if i == str(4):
            if b_3['text'] == '':

                if jogando == 'X':
                    cor = vermelho
                if jogando == 'O':
                    cor = azul

                b_3['fg'] = cor
                b_3['text'] = jogando
                tabela[1][0] = jogando

                if jogando == 'X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                contador += 1

        if i == str(5):
            if b_4['text'] == '':

                if jogando == 'X':
                    cor = vermelho
                if jogando == 'O':
                    cor = azul

                b_4['fg'] = cor
                b_4['text'] = jogando
                tabela[1][1] = jogando

                if jogando == 'X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                contador += 1

        if i == str(6):
            if b_5['text'] == '':

                if jogando == 'X':
                    cor = vermelho
                if jogando == 'O':
                    cor = azul

                b_5['fg'] = cor
                b_5['text'] = jogando
                tabela[1][2] = jogando

                if jogando == 'X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                contador += 1

        if i == str(7):
            if b_6['text'] == '':

                if jogando == 'X':
                    cor = vermelho
                if jogando == 'O':
                    cor = azul

                b_6['fg'] = cor
                b_6['text'] = jogando
                tabela[2][0] = jogando

                if jogando == 'X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                contador += 1

        if i == str(8):
            if b_7['text'] == '':

                if jogando == 'X':
                    cor = vermelho
                if jogando == 'O':
                    cor = azul

                b_7['fg'] = cor
                b_7['text'] = jogando
                tabela[2][1] = jogando

                if jogando == 'X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                contador += 1

        if i == str(9):
            if b_8['text'] == '':

                if jogando == 'X':
                    cor = vermelho
                if jogando == 'O':
                    cor = azul

                b_8['fg'] = cor
                b_8['text'] = jogando
                tabela[2][2] = jogando

                if jogando == 'X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                contador += 1

#################################### CONDIÇÕES DE VITÓRIA ###############################################
        if contador >= 5:

            if tabela[0][0] == tabela[0][1] == tabela[0][2] != "":
                vencedor(jogando)
            elif tabela[1][0] == tabela[1][1] == tabela[1][2] != "":
                vencedor(jogando)
            elif tabela[2][0] == tabela[2][1] == tabela[2][2] != "":
                vencedor(jogando)

            if tabela[0][0] == tabela[1][0] == tabela[2][0] != "":
                vencedor(jogando)
            elif tabela[0][1] == tabela[1][1] == tabela[2][1] != "":
                vencedor(jogando)
            elif tabela[0][2] == tabela[1][2] == tabela[2][2] != "":
                vencedor(jogando)

            if tabela[0][0] == tabela[1][1] == tabela[2][2] != "":
                vencedor(jogando)
            elif tabela[0][2] == tabela[1][1] == tabela[2][0] != "":
                vencedor(jogando)

            if contador >= 9:
                vencedor('Ih, Deu velha')

    # pra decidir o vencedor

    def vencedor(i):
        global tabela
        global score_1
        global score_2
        global contador_de_rodada
        global contador

        # bloqueando os botoes
        b_0['state'] = 'disable'
        b_1['state'] = 'disable'
        b_2['state'] = 'disable'
        b_3['state'] = 'disable'
        b_4['state'] = 'disable'
        b_5['state'] = 'disable'
        b_6['state'] = 'disable'
        b_7['state'] = 'disable'
        b_8['state'] = 'disable'

        app_vencedor = Label(frame_meio, text='', width=25, relief='raise',
                             anchor='center', font=('Ivy 13 bold'), bg=preto, fg=laranjaclaro)
        app_vencedor.place(x=75, y=410)

        if i == 'X':
            score_2 += 1
            app_vencedor['text'] = 'Boa! Jogador 2 venceu!'
            app_o_pontos['text'] = score_2
        elif i == 'O':
            score_1 += 1
            app_vencedor['text'] = 'Boa! Jogador 1 venceu!'
            app_x_pontos['text'] = score_1
        else:
            app_vencedor['text'] = "Ahh, deu velha!"


        def start():
            # Limpeza dos Botoes
            b_0['text'] = ''
            b_1['text'] = ''
            b_2['text'] = ''
            b_3['text'] = ''
            b_4['text'] = ''
            b_5['text'] = ''
            b_6['text'] = ''
            b_7['text'] = ''
            b_8['text'] = ''

            b_0['state'] = 'normal'
            b_1['state'] = 'normal'
            b_2['state'] = 'normal'
            b_3['state'] = 'normal'
            b_4['state'] = 'normal'
            b_5['state'] = 'normal'
            b_6['state'] = 'normal'
            b_7['state'] = 'normal'
            b_8['state'] = 'normal'

            app_vencedor.destroy()
            b_jogar1p.destroy()
            b_jogar2p.destroy()
            sair_jogo.destroy()

        b_jogar1p = Button(frame_meio, command=start, text='Proxima rodada', height=1,  font=(
            'Ivy 10 bold'), overrelief=RIDGE, relief='raised', bg=preto, fg=laranjaclaro)
        b_jogar1p.place(x=150, y=450)

        def jogo_acabou():
            b_jogar1p.destroy()
            b_jogar2p.destroy()
            sair_jogo.destroy()

            app_vencedor.destroy()

            terminar()

        if contador_de_rodada >= 5:
            jogo_acabou()
        else:
            contador_de_rodada += 1
            # RESTART NA TABELA
            tabela = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
            contador = 0

    def terminar():
        global tabela
        global contador_de_rodada
        global score_1
        global score_2
        global contador

        tabela = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        contador_de_rodada = 0
        score_1 = 0
        score_2 = 0
        contador = 0

        # TRAVANDO BOTÕES
        b_0['state'] = 'disable'
        b_1['state'] = 'disable'
        b_2['state'] = 'disable'
        b_3['state'] = 'disable'
        b_4['state'] = 'disable'
        b_5['state'] = 'disable'
        b_6['state'] = 'disable'
        b_7['state'] = 'disable'
        b_8['state'] = 'disable'

        app_fim = Label(frame_meio, text='Fim de Jogo!', width=17, relief='flat',
                        anchor='center', font=('Ivy 13 bold'), bg=preto, fg=laranjaclaro)
        app_fim.place(x=75, y=410)

        def jogar_denovo():
            app_x_pontos['text'] = '0'
            app_o_pontos['text'] = '0'
            app_fim.destroy()
            b_jogar1p.destroy()
            b_jogar2p.destroy()
            sair_jogo.destroy()

            iniciar_jogo()

        b_jogar1p = Button(frame_meio, command=jogar_denovo, text='Jogar Novamente!', height=20,  font=(
            'Ivy 10 bold'), overrelief=RIDGE, relief='raised', bg=preto, fg=laranjaclaro)
        b_jogar1p.place(x=150, y=450)

    ####################################### TABULEIRO ##############################################

        # LINHA 0 #

    b_0 = Button(frame_meio, command=lambda: controlar("1"), text="", width=5, height=2,  font=(
        "Ivy 20 bold"), overrelief=RIDGE, relief="raise", bg=laranjaescuro, fg=preto)
    b_0.place(x=50, y=110)

    b_1 = Button(frame_meio, command=lambda: controlar("2"), text="", width=5, height=2,  font=(
        "Ivy 20 bold"), overrelief=RIDGE, relief="raise", bg=laranjaescuro, fg=preto)
    b_1.place(x=150, y=110)

    b_2 = Button(frame_meio, command=lambda: controlar("3"), text="", width=5, height=2,  font=(
        "Ivy 20 bold"), overrelief=RIDGE, relief="raise", bg=laranjaescuro, fg=preto)
    b_2.place(x=250, y=110)

    # LINHA 1 #

    b_3 = Button(frame_meio, command=lambda: controlar("4"), text="", width=5, height=2,  font=(
        "Ivy 20 bold"), overrelief=RIDGE, relief="raise", bg=laranjaescuro, fg=preto)
    b_3.place(x=50, y=205)

    b_4 = Button(frame_meio, command=lambda: controlar("5"), text="", width=5, height=2,  font=(
        "Ivy 20 bold"), overrelief=RIDGE, relief="raise", bg=laranjaescuro, fg=preto)
    b_4.place(x=150, y=205)

    b_5 = Button(frame_meio, command=lambda: controlar("6"), text="", width=5, height=2,  font=(
        "Ivy 20 bold"), overrelief=RIDGE, relief="raise", bg=laranjaescuro, fg=preto)
    b_5.place(x=250, y=205)

    # LINHA 3 #

    b_6 = Button(frame_meio, command=lambda: controlar("7"), text="", width=5, height=2,  font=(
        "Ivy 20 bold"), overrelief=RIDGE, relief="raise", bg=laranjaescuro, fg=preto)
    b_6.place(x=50, y=300)
    b_7 = Button(frame_meio, command=lambda: controlar("8"), text="", width=5, height=2,  font=(
        "Ivy 20 bold"), overrelief=RIDGE, relief="raise", bg=laranjaescuro, fg=preto)
    b_7.place(x=150, y=300)
    b_8 = Button(frame_meio, command=lambda: controlar("9"), text="", width=5, height=2,  font=(
        "Ivy 20 bold"), overrelief=RIDGE, relief="raise", bg=laranjaescuro, fg=preto)
    b_8.place(x=250, y=300)


######################################## BOTÕES ###############################################################

b_jogar1p = Button(frame_meio, text='1 Player', width=20, height=1,  font=(
    'Ivy 15'), overrelief=RIDGE, relief='raised', bg=preto, fg=laranjaclaro)
b_jogar1p.place(x=77, y=175)

b_jogar2p = Button(frame_meio, command=iniciar_jogo, text='2 Players', width=20, height=1,  font=(
    'Ivy 15 '), overrelief=RIDGE, relief='raised', bg=preto, fg=laranjaclaro)
b_jogar2p.place(x=77, y=237)

sair_jogo = Button(frame_meio, command=sair_jogo, text='Sair do Jogo', width=20, height=1,  font=(
    'Ivy 15 '), overrelief=RIDGE, relief='raised', bg=preto, fg=laranjaclaro)
sair_jogo.place(x=77, y=300)


def escolher_simbolo():

    # Botao P1
    b_opcaoX = Button(frame_meio, command=escolher_simbolo, text="X", width=6, height=2, font=(
        "Ivy 30 bold"), overrelief=RIDGE, relief="raised", bg=preto, fg=vermelho)
    b_opcaoX.place(x=30, y=200)

    # Botao P2
    b_opcaoY = Button(frame_meio, command=escolher_simbolo, text="O", width=6, height=2, font=(
        "Ivy 30 bold"), overrelief=RIDGE, relief="raised", bg=preto, fg=azul)
    b_opcaoY.place(x=220, y=200)


janela.mainloop()