from termcolor import colored, cprint
import emoji
from Telas.mensagens import mensagem_rodada_de_ataque
from Jogo.Players import trocar_vez
from Telas.mensagens_jogador import score


# def buscar_tabuleiro_do_adversário(tabuleiros, players):
#     for player in players:
#         if tabuleiros['jogador']['id'] != player['id']:
#             return tabuleiros


def cria_tabuleiro(player):
    tabuleiro = {
        'player': player,
        'area': []
    }
    for i in range(0, 10):
        linha = []
        for j in range(0, 10):
            linha.append(None)
        tabuleiro['area'].append(linha)

    return tabuleiro


def posicionar_barco(tabuleiros, players):
    posicoes_no_tabuleiro = []
    cprint(f'Vez de {players["nome"]} posicionar os barcos', 'yellow')
    tabuleiro = busca_tabuleiro_jogador(players, tabuleiros)
    barco = 1
    while barco != 6:
        valor_linha = int(input(colored(f'Informe qual linha você deseja ancorar seu {barco}° barco? ', 'yellow')))
        valor_coluna = int(input(colored(f'Informe qual coluna você deseja ancorar seu {barco}° barco? ', 'yellow')))
        if tabuleiro.get('area')[valor_linha][valor_coluna] != None:
            cprint('Já existe um barco nessa posição, tente novamente.', 'red')
        else:
            barco += 1

        cprint('=-' * 75, 'blue', attrs=['blink'])
        tabuleiro.get('area')[valor_linha][valor_coluna] = emoji.emojize(':boat:')
    posicoes_no_tabuleiro.append(tabuleiro)

    return posicoes_no_tabuleiro


def busca_tabuleiro_jogador(player, tabuleiros):
    if tabuleiros.get('player').get('id') == player.get('id'):
        return tabuleiros


def buscar_tabuleiro_do_adversario(player1, tabuleiros):
    if player1['vez']:
        tabuleiro = tabuleiros[1][0]['area']
    else:
        tabuleiro = tabuleiros[0][0]['area']
    return tabuleiro


def rodada_de_ataque(players, tabuleiro, player1, player2):
    mensagem_rodada_de_ataque()
    cprint(f'{players["nome"]} está na vez, faça sua jogada. Boa sorte!', 'green')

    linha_de_ataque = int(input(colored(f'{players["nome"]}, Informe qual linha do tabuleiro você deseja jogar a bomba: ', 'yellow')))
    coluna_de_ataque = int(input(colored(f'{players["nome"]}, Agora informe qual coluna do tabuleiro você deseja jogar a bomba: ', 'yellow')))

    if tabuleiro[linha_de_ataque][coluna_de_ataque] == 'fogo':
        cprint('Voce já acertou este navio! Tente novamente.', 'red')

    elif tabuleiro[linha_de_ataque][coluna_de_ataque] != None:
        tabuleiro[linha_de_ataque][coluna_de_ataque] = 'fogo'
        players['pontos'] += 1
        cprint('')
        cprint('BARCO INIMIGO ATINGIDO E AFUNDADO!!', 'green')

    else:
        cprint('Acertou a água! :(', 'red')

    trocar_vez(player1, player2)
    score(player1, player2)
