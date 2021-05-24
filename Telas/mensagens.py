from termcolor import cprint, colored


def start_game():
    print('=-' * 5, 'BATALHA NAVAL', '-=' * 5)
    print(colored('Iniciando o jogo!', 'yellow'))


def apresentacao():
    cprint('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-BATALHA NAVAL-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=', 'green', attrs=['blink'])
    cprint('Iniciando o jogo...', 'yellow', attrs=['blink'])


def mensagem_rodada_de_ataque():
    cprint('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-RODADA DE ATAQUE=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-', 'yellow')