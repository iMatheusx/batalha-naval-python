from termcolor import colored, cprint


def pedir_nome(id):
    return input(colored(f'Informe o nome do jogador {id}: ', 'yellow'))


def mensagem_criacao_jogador(player):
    cprint(f'Tenha um bom jogo, {player}!', 'blue', attrs=['blink'])


def score(player1, player2):
    cprint('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-PLACAR=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-', 'blue')
    nomep1, pontosp1, nomep2, pontosp2 = player1.get('nome'), player1.get('pontos'), player2.get('nome'), player2.get('pontos')

    cprint(f'{nomep1} - {pontosp1} pontos\n{nomep2} - {pontosp2} pontos', 'red', attrs=['dark'])
    player_vez = player1.get('nome') if player1.get('vez') else player2.get('nome')
    # cprint(f'{player_vez} está na vez, faça bom uso!', 'green')
    cprint('=-' * 75, 'blue', attrs=['blink'])
