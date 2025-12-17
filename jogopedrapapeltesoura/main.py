from random import choice
from time import sleep

#Introdução
print("🪨  \033[30mPEDRA\033[m <-> 📄 \033[37mPAPEL\033[m <-> ✂️  \033[35mTESOURA\033[m")
print("    \033[4mMELHOR DE 3 😀 ✖️  🤖\033[m")
print("\n") 
# Nome
nome = str(input('Diga seu nome antes de jogar: ')).title().strip()

# Objetos do Jogo
pedra = 'PEDRA'
papel = 'PAPEL'
tesoura = 'TESOURA'
opcoes = [pedra, papel, tesoura]
usuario_pontos = 0
cpu_pontos = 0
empate = 0
fim_jogo = 0
novamente = ""

while True:

    # Escolha do Computador
    computador = choice(opcoes)
    # print("A escolha do CPU é {}".format(computador))

    # Escolha do Usuário
    sleep(0.5)
    print("\n                          <<< OPÇÕES >>>")
    sleep(0.5)
    print('''
                        \033[30m  [ 1 ] Pedra \033[m 
                        \033[37m  [ 2 ] Papel \033[m 
                        \033[35m  [ 3 ] Tesoura \033[m''')

    usuario = str(input('Escolha uma opção: '))
    print("------------------------------------------")
    sleep(0.5)

    # Quantidade de Partidas
    fim_jogo += 1

    # Verifica se o Usuário Digitou 1, 2 ou 3
    while True:
        if usuario not in "123":
            usuario = input(str("\033[33mResposta inválida!\033[m Digite 1(\033[30mPEDRA\033[m), 2(\033[37mPAPEL\033[m) ou 3(\033[35mTESOURA\033[m): "))
            sleep(1)
        elif usuario == "1" or usuario == "2" or usuario == "3":
            break
    
    # Usuário Ganha
    if usuario == '1' and computador == tesoura:
        print('\nCOMPUTADOR (\033[35mTESOURA\033[m) X (\033[30mPEDRA\033[m) {}\n \033[1;32m\nO VENCEDOR É O(A) JOGADOR(A) ({})\033[m'.format(nome, nome))
        usuario_pontos += 1
        
        sleep(1)
    elif usuario == '2' and computador == pedra:
        print('\nCOMPUTADOR (\033[37mPEDRA\033[m) X (\033[37mPAPEL\033[m) {}\n \033[1;32m\nO VENCEDOR É O(A) JOGADOR(A) ({})\033[m'.format(nome, nome))
        usuario_pontos += 1
        
        sleep(1)
    elif usuario == '3' and computador == papel:
        print('\nCOMPUTADOR (\033[37mPAPEL\033[m) X (\033[35mTESOURA\033[m) {}\n \033[1;32m\nO VENCEDOR É O(A) JOGADOR(A) ({})\033[m'.format(nome, nome))
        usuario_pontos += 1
        
        sleep(1)

    # CPU Ganha
    elif usuario == '1' and computador == papel:
        print('\nCOMPUTADOR (\033[37mPAPEL\033[m) X (\033[30mPEDRA\033[m) {}\n \033[1;31m\nO VENCEDOR É O COMPUTADOR\033[m'.format(nome))
        cpu_pontos += 1
        
        sleep(1)
    elif usuario == '2' and computador == tesoura:
        print('\nCOMPUTADOR (\033[35mTESOURA\033[m) X (\033[37mPAPEL\033[m) {}\n \033[1;31m\nO VENCEDOR É O COMPUTADOR\033[m'.format(nome))
        cpu_pontos += 1
        
        sleep(1)
    elif usuario == '3' and computador == pedra:
        print('\nCOMPUTADOR (\033[30mPEDRA\033[m) X (\033[35mTESOURA\033[m) {}\n \033[1;31m\nO VENCEDOR É O COMPUTADOR\033[m'.format(nome))
        cpu_pontos += 1
        
        sleep(1)

    # Empate
    elif usuario == '1' and computador == pedra:
        print('\nCOMPUTADOR (\033[30mPEDRA\033[m\033[m) X (\033[30mPEDRA\033[m) {}\n \033[1;33m\nEMPATE\033[m'.format(nome))
        empate += 1
        
        sleep(1)
    elif usuario == '2' and computador == papel:
        print('\nCOMPUTADOR (\033[37mPAPEL\033[m) X (\033[37mPAPEL\033[m) {}\n \033[1;33m\nEMPATE\033[m'.format(nome))
        empate += 1
        
        sleep(1)
    elif usuario == '3' and computador == tesoura:
        print('\nCOMPUTADOR (\033[35mTESOURA\033[m) X (\033[35mTESOURA\033[m) {}\n \033[1;33m\nEMPATE\033[m'.format(nome))
        empate += 1
        sleep(1)

    # Correção de Erro
    else:
        print('\nOpção inválida. Tente novamente!')
        sleep(0.5)
    
    print("\n------------------------------------------")
    sleep(0.5)
    if fim_jogo == 3:
        break

# Resultado se o CPU Ganhar
if cpu_pontos > usuario_pontos:
    print("\nQue pena em. O CPU ganhou de você com {} vitória(s), {} derrota(s) e {} empate(s).".format(cpu_pontos, usuario_pontos, empate))

# Resultado se o Usuário Ganhar
if usuario_pontos > cpu_pontos:
    print("\n\033[1m{}\033[m você ganhou meus PARABÉNS!!! Com {} vitória(s), {} derrota(s) e {} empate(s).".format(nome, usuario_pontos, cpu_pontos, empate))

# Resultado se Empatar
if empate == 3:
    print("\nQue jogo em! Todas com empate.")
