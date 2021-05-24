from termcolor import cprint, colored
from Telas.tabuleiro import mostrar_tabuleiro_finalizado
from time import sleep
from Jogo.Table import cria_tabuleiro, posicionar_barco, buscar_tabuleiro_do_adversario, rodada_de_ataque
from Telas.tabuleiro import mostrar_tabuleiro
from Telas.mensagens_jogador import score
from Jogo.Players import criar_jogadores, sortear_vez, jogador_da_vez
from Telas.mensagens import apresentacao


def menu():
    cprint('=-'*75, 'blue', attrs=['blink'])
    cprint('                                                               1.....Iniciar  jogo\
    \n                                                               2........Opções\
    \n                                                               3......Informações', 'yellow')
    cprint('=-'*75, 'blue', attrs=['blink'])


def destino_menu():
    choose = int(input(colored('>>> ', 'red', attrs=['dark'])))
    if choose == 1:
        start_game()
    elif choose == 2:
        tela_opcoes()
    elif choose == 3:
        tela_informacoes()

def tela_opcoes():
    cprint('=-'*75, 'blue', attrs=['blink'])
    cprint('Essa tela ainda não possui nenhuma funcionalidade, porém já está em desenvolvimento', 'yellow')
    cprint('=-' * 75, 'blue', attrs=['blink'])


def tela_informacoes():
    cprint('=-'*75, 'blue', attrs=['blink'])
    cprint('Projeto básico de batalha naval, com o entuito de desenvolver a lógica de programação', 'yellow')
    cprint('=-' * 75, 'blue', attrs=['blink'])


def terminar_jogo(player1, player2, tabuleiros):
    if player1['pontos'] == 5:
        cprint(f'{player1["nome"]} É O VENCEDOR, AFUNDANDO TODOS OS BARCO DE {(player2["nome"]).upper}!!', 'green')
        cprint('=-' * 75, 'blue')
        mostrar_tabuleiro_finalizado(tabuleiros)
        return False
    elif player2['pontos'] == 5:
        cprint(f'{player1["nome"].upper} É O VENCEDOR, AFUNDANDO TODOS OS BARCO DE {player2["nome"].upper}!!', 'green')
        cprint('=-' * 75, 'blue')
        mostrar_tabuleiro_finalizado(tabuleiros)
        return False
    else:
        return True


def start_game():
    sleep(0.05)
    apresentacao()
    player1, player2 = criar_jogadores()
    player1, player2 = sortear_vez(player1, player2)
    tabuleiro1 = cria_tabuleiro(player1)
    tabuleiro2 = cria_tabuleiro(player2)
    mostrar_tabuleiro((tabuleiro1, tabuleiro2))
    score(player1, player2)
    tabuleiro1 = posicionar_barco(tabuleiro1, player1)
    tabuleiro2 = posicionar_barco(tabuleiro2, player2)
    tabuleiros = tabuleiro1, tabuleiro2
    while terminar_jogo(player1, player2, tabuleiros):
        rodada_de_ataque(jogador_da_vez(player1, player2), buscar_tabuleiro_do_adversario(player1, tabuleiros), player1, player2)


menu()
destino_menu()


