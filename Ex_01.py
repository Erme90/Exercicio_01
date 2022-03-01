# Área da randomização
from random import randint
from time import sleep

print('Vamos jogar JO KEN PÔ!')
print('Iniciando o jogo!')
#sleep(2)

opcoes = ('PEDRA', 'PAPEL', 'TESOURA')
while True:
    randomizador = randint(0, 2)
    computador = (opcoes[randomizador])
    print('PEDRA, PAPEL OU TESOURA?')
    jogador = input('Resposta: ').strip().upper()

    if jogador == ('PEDRA') and computador == ('PEDRA'):
        print(f'Computador escolheu {computador}.')
        print('EMPATE!!!')
    elif jogador == ('PEDRA') and computador == ('PAPEL'):
        print(f'Computador escolheu {computador}.')
        print('Computador venceu!')
    elif jogador == ('PEDRA') and computador == ('TESOURA'):
        print(f'Computador escolheu {computador}.')
        print('Você venceu!')



    #Bloco "PAPEL"
    elif jogador == ('PAPEL') and computador == ('PAPEL'):
        print(f'Computador escolheu {computador}.')
        print('EMPATE!!!')
    elif jogador == ('PAPEL') and computador == ('TESOURA'):
        print(f'Computador escolheu {computador}.')
        print('Computador venceu!')
    elif jogador == ('PAPEL') and computador == ('PEDRA'):
        print(f'Computador escolheu {computador}.')
        print('Você venceu!')


    #Bloco "TESOURA"
    elif jogador == ('TESOURA') and computador == ('TESOURA'):
        print(f'Computador escolheu {computador}.')
        print('EMPATE!!!')
    elif jogador == ('TESOURA') and computador == ('PEDRA'):
        print(f'Computador escolheu {computador}.')
        print('Computador venceu!')
    elif jogador == ('TESOURA') and computador == ('PAPEL'):
        print(f'Computador escolheu {computador}.')
        print('Você venceu!')

    repete = input('Deseja continuar? ').strip().upper()
    if repete == 'N':
        break

print('Jogo finalizado')
