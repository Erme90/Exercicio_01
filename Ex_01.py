from random import randint
from tkinter import *

#Esta função é para quando o jogadro escolhe PEDRA.
def pedra():
    jogadorp = 'PEDRA'
    opcoes = ('PEDRA', 'PAPEL', 'TESOURA', 'LAGARTO', 'SPOCK')
    randomizador = randint(0, 4)
    computador = (opcoes[randomizador])
    if jogadorp and computador == ('PEDRA'):
        resposta_depedra = ('EMPATE!!!\nO Computador também escolheu PEDRA')
    elif jogadorp and computador == ('PAPEL'):
        resposta_depedra = (' COMPUTADOR venceu!\nO COMPUTADOR escolheu PAPEL\nE PAPEL cobre PEDRA')
    elif jogadorp and computador == ('LAGARTO'):
        resposta_depedra = ('Você venceu!\nO computador escolheu LAGARTO\nE PEDRA esmaga LAGARTO')
    elif jogadorp and computador == ('SPOCK'):
        resposta_depedra = ('COMPUTADOR VENCEU!!!\nO computador escolheu SPOCK\nE SPOCK vaporiza PEDRA')
    else:
        resposta_depedra = ('VOCÊ venceu!\nO computador escolheu TESOURA\nE PEDRA esmaga tesoura')
    resposta ['text'] = resposta_depedra
   

#Esta função é para quando o jogador escolhe PAPEL.
def papel():
    jogadorpa = 'PAPEL'
    opcoes = ('PEDRA', 'PAPEL', 'TESOURA', 'LAGARTO', 'SPOCK')
    randomizador = randint(0, 4)
    computador = (opcoes[randomizador])
    if jogadorpa and computador == ('PAPEL'):
        resposta_depapel = ('EMPATE!!!\nO computador escolheu PAPEL')
    elif jogadorpa and computador == ('PEDRA'):
        resposta_depapel =('VOCÊ VENCEU!\nComputador escolheu PEDRA\nE PAPEL cobre PEDRA')
    elif jogadorpa and computador == ('LAGARTO'):
        resposta_depapel = ('COMPUTADOR VENCEU!!!\nO computador escolheu LAGARTO\nE LAGARTO come PAPEL')
    elif jogadorpa and computador == ('SPOCK'):
        resposta_depapel = ('VOCÊ VENCEU!!!\nO computador escolheu SPOCK\nE PAPEL refuta SPOCK')
    else:
        resposta_depapel = ('COMPUTADOR venceu!\nComputador escolheu TESOURA\nE TESOURA corta PAPEL')
    resposta ['text'] = resposta_depapel
    


#Esta função é para quando o jogador escolhe TESOURA.
def tesoura():
    jogadort = 'TESOURA'
    opcoes = ('PEDRA', 'PAPEL', 'TESOURA', 'LAGARTO', 'SPOCK')
    randomizador = randint(0, 4)
    computador = (opcoes[randomizador])
    if jogadort and computador == ('TESOURA'):
        resposta_detesoura= ('EMPATE!!!\nO Computador também escolheu TESOURA')
    elif jogadort == ('TESOURA') and computador == ('PEDRA'):
        resposta_detesoura = ('COMPUTADOR venceu!\nO computador escolheu PEDRA\nE PEDRA esmaga TESOURA')
    elif jogadort and computador == ('LAGARTO'):
        resposta_detesoura = ('VOCÊ VENCEU!!!\nO computador escolheu LAGARTO\nE TESOURA decapita LAGARTO')
    elif jogadort and computador == ('SPOCK'):
        resposta_detesoura = ('COMPUTADOR VENCEU!!!\nO computador escolheu SPOCK\nE SPOCK esmaga TESOURA')
    else:
        resposta_detesoura = ('VOCÊ venceu!\nComputador escolheu PAPEL')
    resposta['text'] = resposta_detesoura


#Esta função é para quando o jogador escolhe LAGARTO.
def lagarto():
    jogadorla = 'LAGARTO'
    opcoes = ('PEDRA', 'PAPEL', 'TESOURA', 'LAGARTO', 'SPOCK')
    randomizador = randint(0, 4)
    computador = (opcoes[randomizador]) 
    if jogadorla and computador == ('PEDRA'):
        resposta_delagarto = ('COMPUTADOR VENCEU!!!\nO computador escolheu PEDRA\nE PEDRA esmaga LAGARTO.')
    elif jogadorla and computador == ('PAPEL'):
        resposta_delagarto = ('VOCÊ VENCEU!!!\nO computador escolheu PAPEL\nE LAGARTO come PAPEL')
    elif jogadorla and computador == ('TESOURA'):
        resposta_delagarto = ('O COMPUTADOR VENCEU!!!\nO computador escolheu TESOURA\nE TESOURA decapita LAGARTO ')
    elif jogadorla and computador == ('SPOCK'):
        resposta_delagarto = ('VOCÊ VENCEU!!!\nO computador escolheu SPOCK\nE LAGARTO envenena SPOCK.')
    else:
        resposta_delagarto = ('EMPATE!\nO computador também escolheu LAGARTO')
    resposta['text'] = resposta_delagarto


#Esta funçpão é para quando o jogadro escolhe SPOCK.

def spock():
    jogadorsp = 'SPOCK'
    opcoes = ('PEDRA', 'PAPEL', 'TESOURA', 'LAGARTO', 'SPOCK')
    randomizador = randint(0,4)
    computador = (opcoes[randomizador])
    if jogadorsp and computador == ('PEDRA'):
        resposta_despock = ('VOCÊ VENCEU!!!\nO computador escolheu PEDRA\nE SPOCK vaporiza PEDRA')
    elif jogadorsp and computador == ('PAPEL'):
        resposta_despock = ('COMPUTADOR VENCEU!!!\nO computador escolheu PAPEL\nE PAPEL refuta SPOCK')
    elif jogadorsp and computador == ('TESOURA'):
        resposta_despock = ('VOCÊ VENCEU!!!\nO computador escolheu TESOURA\nE SPOCK esmaga TESOURA')
    elif jogadorsp and computador == ('LAGARTO'):
        resposta_despock = ('O COMPUTADOR VENCEU!!!\nO computador escolheu LAGARTO\nE LAGARTO envenena SPOCK')
    else:
        resposta_despock = ('EMPATE!!!\nO computador também escolheu SPOCK')
    
    resposta ['text'] = resposta_despock




#interface

janela = Tk()
janela.title('JOKENPO')#titulo da janela
janela.geometry('350x400')#tamanho da janela

texto_orientacao = Label(janela, text='PEDRA, PAPEL,TESOURA,LAGARTO ou SPOCK?')#Label precisa saber de onde ele é, e o que será escrito.
texto_orientacao.grid(column=0, row=0, padx=20, pady=20)

botaopedra = Button(janela, text='PEDRA',padx=22, command=pedra)
botaopedra.grid(column=0,padx=10, pady=10, row=1)


botaopapel = Button(janela, text='PAPEL', padx=22, command=papel)
botaopapel.grid(column=0, row=2,padx=10, pady=10)


botaotes = Button(janela, text='TESOURA', command=tesoura)
botaotes.grid(column=0, row=3, padx=10, pady=10)

botaolagar = Button(janela, text='LAGARTO', command=lagarto)
botaolagar.grid(column=0, row=4, padx=10, pady=10)

botaospock = Button(janela,text='SPOCK', command=spock)
botaospock.grid(column=0, row=5, padx=10, pady=10)

resposta = Label(janela,text='')
resposta.grid(column=0, row=6)

janela.mainloop()