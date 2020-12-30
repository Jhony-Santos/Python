def historico(numeroPartidas, vitoria1, vitoria2, empate):
    print('Numero de partidas realizadas:', numeroPartidas)
    if numeroPartidas > 0:
        percentual1 = (vitoria1 * 100) / numeroPartidas
        print('Percentual de vitorias jogador 1:', percentual1)
        percentual2 = (vitoria2 * 100) / numeroPartidas
        print('Percentual de vitorias jogador 2:', percentual2)
    else:
        print('Não foi jogado nenhuma vez!')
    print('Numero de empates é igual:', empate)


import random

suasJogadas = []
jogadasComputador = []
numeroPartidasH = 0
empateH = 0
suasVitorias = 0
vitoriasComputador = 0
jogadas1 = []
jogadas2 = []
numeroPartidasC = 0
empateC = 0
vitoria1 = 0
vitoria2 = 0
jogoLigado = True
while jogoLigado == True:
    print('OPÁ VAMOS JOGAR?!\n'
          'PARA JOGAR  HUMANO X HUMANO TECLE 5\n'
          'PARA JOGAR HUMANO X COMPUTADOR TECLE 10\n'
          'PARA VER O HISTÓRICO TECLE (HUMANO X HUMANO) 15\n'
          'PARA VER O HISTÓRICO TECLE (HUMANO X COMPUTADOR) 20\n'
          'PARA ENCERRAR TECLE 25\n')
    entrada = int(input('O que deseja fazer '))
    if entrada == 5:
        print('ENTÃO VAMOS AO JOGO\n'
              'PEDRA = 1\n'
              'PAPEL = 2\n'
              'TESOURA = 3\n')
        j1 = int(input('Jogador 1 entre com uma das três opções '))
        j2 = int(input('Jogador 2 entre com uma das opções '))
        if j1 == 1:
            jogadas1.append('Pedra')
        elif j1 == 2:
            jogadas1.append('Papel')
        elif j1 == 3:
            jogadas1.append('Tesoura')
        if j2 == 1:
            jogadas2.append('Pedra')
        elif j2 == 2:
            jogadas2.append('Papel')
        elif j2 == 3:
            jogadas2.append('Tesoura')

        if j1 == 1 and j2 == 3 or j1 == 2 and j2 == 1 or j1 == 3 and j2 == 2:
            print('O jogador 1 venceu a partida')
            vitoria1 = vitoria1 + 1
        elif j1 == 3 and j2 == 1 or j1 == 1 and j2 == 2 or j1 == 2 and j2 == 3:
            print('O jogador 2 venceu a partida')
            vitoria2 = vitoria2 + 1
        elif j1 == 1 and j2 == 1 or j1 == 2 and j2 == 2 or j1 == 3 and j2 == 3:
            print('Houve empate')
            empateH = empateH + 1
        else:
            print('Valor invalido')

            continue
        numeroPartidasH = numeroPartidasH + 1

    elif entrada == 10:
        print('ENTÃO VAMOS AO JOGO\n'
              'PEDRA = 1\n'
              'PAPEL = 2\n'
              'TESOURA = 3\n')
        j1 = int(input('Jogador 1 entre com uma das três opções '))
        computador = random.randint(1, 3)
        if j1 == 1:
            suasJogadas.append('Pedra')
        elif j1 == 2:
            suasJogadas.append('Papel')
        elif j1 == 3:
            suasJogadas.append('Tesoura')
        if computador == 1:
            jogadasComputador.append('Pedra')
        elif computador == 2:
            jogadasComputador.append('Papel')
        elif computador == 3:
            jogadasComputador.append('Tesoura')

        if j1 == 1 and computador == 3 or j1 == 2 and computador == 1 or j1 == 3 and computador == 2:
            print('Você ganhou a partida')
            suasVitorias = suasVitorias + 1
        elif j1 == 3 and computador == 1 or j1 == 1 and computador == 2 or j1 == 2 and computador == 3:
            print('O computador GANHOU a partida')
            vitoriasComputador = vitoriasComputador + 1
        elif j1 == 1 and computador == 1 or j1 == 2 and computador == 2 or j1 == 3 and computador == 3:
            print('Houve empate')
            empateC = empateC + 1
        else:
            print('Valor invalido')

            continue
        numeroPartidasC = numeroPartidasC + 1


    elif entrada == 15:
        print('HISTORICO')
        print('Jogadas Jogador 1 :', jogadas1)
        print('Jogadas Jogador 2 :', jogadas2)
        # HUMANO X HUMANO
        historico(numeroPartidasH, vitoria1, vitoria2, empateH)

    elif entrada == 20:
        print('HISTORICO')
        print('você é jogador 1 e o computador é o jogador 2')
        print('Suas jogadas foram', suasJogadas)
        print('As jogadas do computador :', jogadasComputador)
        # HUMANO X COMPUTADOR
        historico(numeroPartidasC, suasVitorias, vitoriasComputador, empateC)
    elif entrada == 25:
        print('Desligando Máquina.')
        break
    else:
        print('Digite uma opção válida!')
