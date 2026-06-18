import pygame
import os
from settings import largura, altura

def mostrar_tela_inicial(tela):
    
    caminho_imagem = "assets/tela_inicio.png" 
    
    
    imagem_scaled = None
    
    if os.path.exists(caminho_imagem):
        
        imagem_original = pygame.image.load(caminho_imagem).convert()
        
        imagem_scaled = pygame.transform.scale(imagem_original, (largura, altura))
    
    clock = pygame.time.Clock()
    
    aguardando = True
    iniciar_jogo = False
    
    while aguardando:
        
        for event in pygame.event.get():
    
            if event.type == pygame.QUIT:
                aguardando = False
                iniciar_jogo = False
                
            
            if event.type == pygame.KEYDOWN:
               
                if event.key == pygame.K_RETURN:
                    aguardando = False
                    iniciar_jogo = True
                
                if event.key == pygame.K_ESCAPE:
                    aguardando = False
                    iniciar_jogo = False
        
        if imagem_scaled:
            tela.blit(imagem_scaled, (0, 0))
        else:
            
            tela.fill((40, 40, 40)) 
            
        
        pygame.display.flip()
        
        clock.tick(30)
        
    return iniciar_jogo