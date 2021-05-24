from time import sleep
from termcolor import cprint
import emoji


def mostrar_tabuleiro(tabuleiros):
    for i, tabuleiro in enumerate(tabuleiros):
        id_jogador = tabuleiro['player']['id']
        area = tabuleiro['area']
        for j, linha in enumerate(area):
            if j == 0 and id_jogador == 1:
                mostrar_indice_coluna(len(linha))
            mostrar_indice_linha(j)
            for posicao in linha:
                valor = posicao or ' * '
                cprint(emoji.emojize(f' |:onda:| ', language='pt'), 'blue', end='')
            print()
            if j == len(area) - 1 and (id_jogador) == 2:
                mostrar_indice_coluna(len(linha))
            sleep(0.05)
        if i == 0:
            cprint('~'* 58, 'red')


def mostrar_indice_coluna(tamanho_linha):
    for count in range(0, tamanho_linha):
        end = '\n' if count == tamanho_linha - 1 else ' '
        espaco_extra = '  ' if count == 0 else ''
        cprint(f'{espaco_extra}|{count}|  ', 'yellow', end=end)


def mostrar_indice_linha(indice):
    cprint((indice), 'yellow', end=':')


def mostrar_tabuleiro_finalizado(tabuleiros):
    print('')
    for i, tabuleiro in enumerate(tabuleiros):
        id_jogador = tabuleiro[0]['player']['id']
        area = tabuleiro[0]['area']
        for j, linha in enumerate(area):
            if j == 0 and id_jogador == 1:
                mostrar_indice_coluna(len(linha))
            mostrar_indice_linha(j)
            for posicao in linha:
                mostrar = emoji.emojize(':onda:', language='pt') if posicao == None else emoji.emojize(':cruzeiro:', language='pt')
                cor = 'blue' if id_jogador == 1 else 'cyan'
                cprint(f" |{mostrar}|", cor, end=' ')
            print()
            if j == len(area) - 1 and id_jogador == 2:
                mostrar_indice_coluna(len(linha))
        if i == 0:
            cprint('~'* 58, 'red')