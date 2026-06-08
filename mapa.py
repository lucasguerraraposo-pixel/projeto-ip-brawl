import pygame
import sys

# 1. Configurações Iniciais
pygame.init()

# Cores inspiradas no Brawl Stars
# RGB: R (Vermelho), G (Verde), B (Azul)
COR_CHAO = (144, 238, 144)    # Verde claro
COR_MURO = (139, 69, 19)      # Marrom (tipo caixas de madeira)
COR_ARBUSTO = (34, 139, 34)   # Verde escuro (para se esconder)
COR_FUNDO = (50, 50, 50)       # Cinza escuro para fora do mapa

# Configuração da Grade e Tela
LARGURA_TILE = 40  # Tamanho de cada quadrado em pixels (40x40)
ALTURA_TILE = 40

# Definindo o Mapa (Matriz)
# 0 = Chão, 1 = Muro, 2 = Arbusto
# Dica: No Brawl Stars os mapas são simétricos!
mapa_data = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 2, 2, 0, 0, 1, 1, 0, 0, 2, 2, 0, 0, 0, 1],
    [1, 0, 2, 2, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# Calcula tamanho da tela baseado no mapa
LARGURA_TELA = len(mapa_data[0]) * LARGURA_TILE
ALTURA_TELA = len(mapa_data) * ALTURA_TILE

tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Projeto IP Brawl - Protótipo de Mapa")
relogio = pygame.time.Clock()

# 2. Função para desenhar o mapa
def desenhar_mapa(superficie, dados_mapa):
    # Passamos por cada linha (row) e coluna (col) da matriz
    for num_linha, linha in enumerate(dados_mapa):
        for num_coluna, tile in enumerate(linha):
            
            # Calcula a posição X e Y exata na tela
            x = num_coluna * LARGURA_TILE
            y = num_linha * ALTURA_TILE
            
            # Cria o quadrado (Rect) para desenhar
            quadrado = pygame.Rect(x, y, LARGURA_TILE, ALTURA_TILE)
            
            # Define qual cor desenhar baseado no número na matriz
            if tile == 0:
                pygame.draw.rect(superficie, COR_CHAO, quadrado)
            elif tile == 1:
                pygame.draw.rect(superficie, COR_MURO, quadrado)
            elif tile == 2:
                # Desenha o chão por baixo e o arbusto menor no centro
                pygame.draw.rect(superficie, COR_CHAO, quadrado)
                margem_arbusto = 5
                arbusto_rect = pygame.Rect(x + margem_arbusto, y + margem_arbusto, 
                                           LARGURA_TILE - margem_arbusto*2, ALTURA_TILE - margem_arbusto*2)
                pygame.draw.rect(superficie, COR_ARBUSTO, arbusto_rect, border_radius=5)

# 3. Loop Principal do Jogo
while True:
    # Trata eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Desenha as coisas
    tela.fill(COR_FUNDO) # Limpa a tela
    
    desenhar_mapa(tela, mapa_data) # Desenha o mapa

    # Atualiza a tela
    pygame.display.flip()
    relogio.tick(60) # 60 FPS