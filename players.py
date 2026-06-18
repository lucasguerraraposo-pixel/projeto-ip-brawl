import pygame


class Player:
    def __init__(self, x, y, color, controls):
        self.rect = pygame.Rect(x, y, 24, 24)
        self.speed = 1
        self.color = color
        self.controls = controls
        self.hidden = False

        self.spawn_x = x
        self.spawn_y = y
        self.vida_max = 5
        self.vida = self.vida_max
        

    def move(self, mapa):
        old_x = self.rect.x
        old_y = self.rect.y

        keys = pygame.key.get_pressed()

        # movimento direto 
        if keys[self.controls["left"]]:
            self.rect.x -= self.speed
        if keys[self.controls["right"]]:
            self.rect.x += self.speed
        if keys[self.controls["up"]]:
            self.rect.y -= self.speed
        if keys[self.controls["down"]]:
            self.rect.y += self.speed

        # colisão com parede
        for wall in mapa.walls:
            if self.rect.colliderect(wall):
                self.rect.x = old_x
                self.rect.y = old_y

        # colisão com água
        for water in mapa.waters:
            if self.rect.colliderect(water):
                self.rect.x = old_x
                self.rect.y = old_y

        # arbusto (esconder)
        self.hidden = False
        for bush in mapa.bushes:
            if self.rect.colliderect(bush):
                self.hidden = True

    def draw(self, surface):
        if not self.hidden:
            pygame.draw.rect(surface, self.color, self.rect)

    def draw_hud(self, surface, label_x, label_y):
        font = pygame.font.SysFont(None, 20)
        label = font.render(f"P{self.player_num}", True, self.color)
        surface.blit(label, (label_x, label_y))

        heart_size = 12
        gap = 4
        for i in range(self.vida_max):
            x = label_x + 28 + i *(heart_size + gap)
            if i < self.vida:
                pygame.draw.rect(surface, self.color, (x, label_y, heart_size, heart_size))
            else:
                pygame.draw.rect(surface, (80, 80, 80), (x, label_y, heart_size, heart_size))

    def damage(self):
        self.vida -= 1
        if self.vida<= 0:
            return True
        return False
        #se a vida acabar retorna true

    def respawn(self):
        self.vida = self.vida_max
        self.rect.x = self.spawn_x
        self.rect.y = self.spawn_y
        #volta pra vida maxima e respawna

class Player1(Player):
    def __init__(self, x, y):     # cor              # controles
        super().__init__(x, y, (0, 0, 255), {"left": pygame.K_a, "right": pygame.K_d, "up": pygame.K_w, "down": pygame.K_s})
        self.player_num = 1
class Player2(Player):
    def __init__(self, x, y):     # cor              # controles
        super().__init__(x, y, (255, 0, 0), { "left": pygame.K_LEFT, "right": pygame.K_RIGHT, "up": pygame.K_UP, "down": pygame.K_DOWN})
        self.player_num = 2