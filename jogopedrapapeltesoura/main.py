from random import choice
# Nome
nome = str(input('Diga seu nome antes de jogar: ')).title()
# Objetos do Jogo
pedra = 'PEDRA'
papel = 'PAPEL'
tesoura = 'TESOURA'
opcoes = [pedra, papel, tesoura]
# Escolha do Computador
computador = choice(opcoes)
# Escolha do Usuário
print('''
                    \033[37m  Pedra [ 1 ]\033[m 
                    \033[30m  Papel [ 2 ]\033[m 
                    \033[35mTesoura [ 3 ]\033[m''')
usuario = str(input('Escolha uma opção: '))
# Usuario Ganha
if usuario == '1' and computador == tesoura:
    print('COMPUTADOR (\033[35mTESOURA\033[m) X (\033[37mPEDRA\033[m) {}\n \033[1;34mO VENCEDOR É O JOGADOR ({})'.format(nome, nome))
elif usuario == '2' and computador == pedra:
    print('COMPUTADOR (\033[37mPEDRA\033[m) X (\033[30mPAPEL\033[m) {}\n \033[1;34mO VENCEDOR É O JOGADOR ({})'.format(nome, nome))
elif usuario == '3' and computador == papel:
    print('COMPUTADOR (\033[30mPAPEL\033[m) X (\033[35mTESOURA\033[m) {}\n \033[1;34mO VENCEDOR É O JOGADOR ({})'.format(nome, nome))
# Usuário Perde
elif usuario == '1' and computador == papel:
    print('COMPUTADOR (\033[30mPAPEL\033[m) X (\033[37mPEDRA\033[m) {}\n \033[1;31mO VENCEDOR É O COMPUTADOR'.format(nome))
elif usuario == '2' and computador == tesoura:
    print('COMPUTADOR (\033[35mTESOURA\033[m) X (\033[30mPAPEL\033[m) {}\n \033[1;31mO VENCEDOR É O COMPUTADOR'.format(nome))
elif usuario == '3' and computador == pedra:
    print('COMPUTADOR (\033[37mPEDRA\033[m) X (\033[35mTESOURA\033[m) {}\n \033[1;31mO VENCEDOR É O COMPUTADOR'.format(nome))
# Empate
elif usuario == '1' and computador == pedra:
    print('COMPUTADOR (\033[37mPEDRA\033[m\033[m) X (\033[37mPEDRA\033[m) {}\n \033[1;33mEMPATE'.format(nome))
elif usuario == '2' and computador == papel:
    print('COMPUTADOR (\033[30mPAPEL\033[m) X (\033[30mPAPEL\033[m) {}\n \033[1;33mEMPATE'.format(nome))
elif usuario == '3' and computador == tesoura:
    print('COMPUTADOR (\033[35mTESOURA\033[m) X (\033[35mTESOURA\033[m) {}\n \033[1;33mEMPATE'.format(nome))
else:
    print('Opção inválida. Tente novamente!')