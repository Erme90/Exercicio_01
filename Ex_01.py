# Área da randomização
from random import randint
from time import sleep

print('Vamos jogar JO KEN PÔ!')
print('Iniciando o jogo!')
#sleep(2)
opcoes = ('PEDRA', 'PAPEL', 'TESOURA')
randomizador = randint(0, 2)
computador = (opcoes[randomizador])

# Bloco do jogadores
print('PEDRA, PAPEL OU TESOURA? ')
jogador = input('> ').strip().upper()
resp = ('')
while resp != ('NÃO', 'N'):
    while jogador not in ('pedra', 'PEDRA', 'Pedra',
                          'papel', 'PAPEL', 'Papel'
                        'tesoura', 'TESOURA', 'Tesoura'):
        print('Opção inválida!')
        jogador = input('PEDRA, PAPEL OU TESOURA? ').strip().upper()

        # Bloco das condicionais (Jogador joga pedra)

    # Bloco "PEDRA"
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
    resp = input('Jogar novamente? ').upper()

#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