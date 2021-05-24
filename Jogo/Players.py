from termcolor import cprint
from Telas.mensagens_jogador import pedir_nome, mensagem_criacao_jogador
from random import randint

def criar_jogador(id):
    nome = pedir_nome(id)
    return {
        'id': id,
        'nome': nome,
        'pontos': 0,
        'vez': False
    }

def criar_jogadores():
    cprint('=-' * 75, 'blue')
    player1 = criar_jogador(1)
    mensagem_criacao_jogador(f'{player1.get("nome")}')
    cprint('=-' * 75, 'blue')
    player2 = criar_jogador(2)
    mensagem_criacao_jogador(f'{player2.get("nome")}')
    cprint('=-' * 75, 'blue')
    return player1, player2


def sortear_vez(player1, player2):
    players = player1, player2
    numero_vez = randint(0,1)
    players[numero_vez]['vez'] = True
    if player1.get('vez'):
        cprint(f'{player1.get("nome")} começa!', 'green')
    else:
        cprint(f'{player2.get("nome")} começa!', 'green')
    return players


def trocar_vez(player1, player2):
    if player1['vez']:
        player2['vez'] = True
        player1['vez'] = False
    else:
        player2['vez'] = False
        player1['vez'] = True


def jogador_da_vez(player1, player2):
    return player1 if player1['vez'] else player2