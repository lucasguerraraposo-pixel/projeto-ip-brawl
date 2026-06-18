import pygame
import sys
from players import Player1, Player2
from itens import Itens, Projectile
from settings import resolucao, largura, altura
from mapa import Mapa

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(resolucao)
        pygame.display.set_caption("Meu Jogo Quadrado")

        self.clock = pygame.time.Clock()
        self.fps = 60
        self.running = True

        #Instancia o Player 1 no lado esquerdo e Player 2 no lado direito
        self.player1 = Player1(3, 238)
        self.player2 = Player2(765, 238)

        #Instancia o item central
        self.cube = Itens(largura // 2, altura // 2)

        self.mapa = Mapa("assets/mapa_brawl.tmx")

        self.bullets = []

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    nova_bala = Projectile(
                        x=self.player1.rect.centerx,
                        y=self.player1.rect.centery,
                        target_x=self.player2.rect.centerx,
                        target_y=self.player2.rect.centery,
                        color=(0, 150, 255) # bala azul para o player1
                    )
                    self.bullets.append(nova_bala)

                if event.key == pygame.K_RETURN:
                    nova_bala = Projectile(
                        x=self.player2.rect.centerx,
                        y=self.player2.rect.centery,
                        target_x=self.player1.rect.centerx,
                        target_y=self.player1.rect.centery,
                        color=(255, 50, 50) #bala vermelha pro player 2
                    )
                    self.bullets.append(nova_bala)

    def checar_bala(self, bala):
        if bala.x < 0 or bala.x > largura or bala.y < 0 or bala.y > altura: # Saiu da tela
            return True


        if any(bala.rect.colliderect(parede) for parede in self.mapa.walls):
            return True

        # Bala vermelha acerta Player 1
        if bala.color == (255, 50, 50) and bala.rect.colliderect(self.player1.rect):
            morreu = self.player1.damage() # se morre retorna true
            print(f"P1 tomou! Vida restante: {self.player1.vida}")
            if morreu:
                self.player1.respawn()
                self.player2.respawn()
                self.bullets.clear()
            return True

        # Bala azul acerta Player 2
        if bala.color == (0, 150, 255) and bala.rect.colliderect(self.player2.rect):
            morreu = self.player2.damage() #se morre retorna true
            print(f"P2 tomou! Vida restante: {self.player2.vida}")
            if morreu:
                self.player1.respawn()
                self.player2.respawn()
                self.bullets.clear()
            return True

        return False

    def update(self):
        """Atualiza a lógica do jogo"""
        self.player1.move(self.mapa)
        self.player2.move(self.mapa)

        # Opcional: Impede o jogador de sair das bordas da tela
        self.player1.rect.clamp_ip(self.screen.get_rect())
        self.player2.rect.clamp_ip(self.screen.get_rect())

        for bala in self.bullets[:]: #[:] faz a iteração com a lista de balas funcionar, sem esse comando a remoção de balas no mapa fica uma confusão
            bala.move()

        balas_para_remover = [bala for bala in self.bullets if self.checar_bala(bala)]

        for bala in balas_para_remover:
            if bala in self.bullets: # garante que o bullets.clear() do respawn não cause erro
                self.bullets.remove(bala)

    def draw(self):
        
        self.screen.fill((30, 30, 30))  # Fundo grafite escuro

        self.mapa.draw(self.screen)
        # Desenha o cube
        self.cube.draw(self.screen)
        # Desenha o jogador
        self.player1.draw(self.screen)
        self.player2.draw(self.screen)

        for bala in self.bullets:
            bala.draw(self.screen)

        # HUD de vida P1 no canto esquerdo P2 no direito
        self.player1.draw_hud(self.screen, label_x=10, label_y=10)
        self.player2.draw_hud(self.screen, label_x=largura - 130, label_y=10)

        # Atualiza a tela 
        pygame.display.flip()

    def run(self):
        """Loop principal do jogo"""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.fps)

        pygame.quit()
        sys.exit()