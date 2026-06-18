import pygame
from game import Game
from settings import resolucao
from telainicial import mostrar_tela_inicial

def main():
    pygame.init()

    tela = pygame.display.set_mode(resolucao, pygame.FULLSCREEN | pygame.SCALED)
    pygame.display.set_caption("xama no brawl")

    iniciar = mostrar_tela_inicial(tela)

    if iniciar:
        meu_jogo = Game(tela)
        meu_jogo.run()

    pygame.quit()

if __name__ == "__main__":
    main()