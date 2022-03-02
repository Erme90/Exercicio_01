from random import randint
from tkinter import *

def pedra():
    jogadorp = 'PEDRA'
    opcoes = ('PEDRA', 'PAPEL', 'TESOURA')
    randomizador = randint(0, 2)
    computador = (opcoes[randomizador])
    print(f'O computador jogou {computador}')
    if jogadorp == ('PEDRA') and computador == ('PEDRA'):
        print('EMPATE!!!')
    elif jogadorp == ('PEDRA') and computador == ('PAPEL'):
        print('Computador venceu!')
    elif jogadorp == ('PEDRA') and computador == ('TESOURA'):
        print('Você venceu!')

def papel():
    jogadorpa = 'PAPEL'
    opcoes = ('PEDRA', 'PAPEL', 'TESOURA')
    randomizador = randint(0, 2)
    computador = (opcoes[randomizador])
    print(f'O computador jogou {computador}')
    if jogadorpa == ('PAPEL') and computador == ('PAPEL'):
        print('EMPATE!!!')
    elif jogadorpa == ('PAPEL') and computador == ('PEDRA'):
        print('VOCÊ venceu!')
    elif jogadorpa == ('PAPEL') and computador == ('TESOURA'):
        print('COMPUTADOR venceu!')

def tesoura():
    jogadort = 'TESOURA'
    opcoes = ('PEDRA', 'PAPEL', 'TESOURA')
    randomizador = randint(0, 2)
    computador = (opcoes[randomizador])
    print(f'O computador jogou {computador}')
    if jogadort == ('TESOURA') and computador == ('TESOURA'):
        print ('EMPATE!!!')
    if jogadort == ('TESOURA') and computador == ('PEDRA'):
        print('COMPUTADOR venceu!')
    if jogadort == ('TESOURA') and computador == ('PAPEL'):
        print('VOCÊ venceu!')

#interface

janela = Tk()
janela.title('JOKENPO')#titulo da janela
janela.geometry('250x350')#tamanho da janela

texto_orientacao = Label(janela, text='PEDRA, PAPEL OU TESOURA?')#Label precisa saber de onde ele é, e o que será escrito.
texto_orientacao.grid(column=0, row=0, padx=20, pady=20)

botaopedra = Button(janela, text='PEDRA',padx=22, command=pedra)
botaopedra.grid(column=0,padx=10, pady=10, row=1)

botaopapel = Button(janela, text='PAPEL', padx=22, command=papel)
botaopapel.grid(column=0, row=2,padx=10, pady=10)

botaotes = Button(janela, text='TESOURA', command=tesoura)
botaotes.grid(column=0, row=3, padx=10, pady=10)


janela.mainloop()