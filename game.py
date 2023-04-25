from cenario import *
import pygame
import time


def trocar_tela(matriz_cenario, caminho_cenario):
    try:
        # Fechar janela atual
        pygame.display.quit()
        pygame.init()

        matriz = matriz_cenario 
        caminho = caminho_cenario

        # Definir cores
        PRETO = (0, 0, 0)
        BRANCO = (255, 255, 255)
        VERMELHO = (255, 0, 0)
        COR_GRAMA= (144, 207, 84)
        COR_FLORESTA = (3, 151, 74)
        COR_AGUA = (89, 138, 214)
        COR_AREIA = (196, 188, 150)
        COR_MONTANHA= (148, 140, 83)
        AZUL= (0, 0, 255)
        CINZACLARO = (221, 221, 221)
        CINZAESCURO = (160, 160, 160)

        # Definir a largura e a altura de cada bloco
        BLOCK_WIDTH = 15
        BLOCK_HEIGHT = 15

        # Inicializar pygame
        #pygame.init()

        # Definir as dimensões da janela
        WINDOW_WIDTH = len(matriz[0]) * BLOCK_WIDTH
        WINDOW_HEIGHT = len(matriz) * BLOCK_HEIGHT
        WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
        tela = pygame.display.set_mode(WINDOW_SIZE)
        
        # Definir o título da janela
        pygame.display.set_caption("A* Algoritimo")

        # Dicionário para definir as cores de cada caractere
        mapa_cores = {
            "n": CINZAESCURO,
            "q": CINZACLARO,
            "m": COR_MONTANHA,            
            "g": COR_GRAMA,
            "a": COR_AREIA,
            "f": COR_FLORESTA,
            "w": COR_AGUA,
            "x": AZUL,

        }
        

        # Desenhar a matriz na tela
        def desenhar_matriz(matriz):
            for lin in range(len(matriz)):
                for col in range(len(matriz[lin])):
                    cor = mapa_cores[matriz[lin][col]]
                    rect = pygame.Rect(col*BLOCK_WIDTH, lin*BLOCK_HEIGHT, BLOCK_WIDTH, BLOCK_HEIGHT)
                    pygame.draw.rect(tela, cor, rect)

        # Desenhar o caminho na tela
        def desenhar_matriz(matriz):
            for lin in range(len(matriz)):
                for col in range(len(matriz[lin])):
                    cor = mapa_cores[matriz[lin][col]]
                    x = col * BLOCK_WIDTH
                    y = lin * BLOCK_HEIGHT
                    quadrado = pygame.Rect(x, y, BLOCK_WIDTH, BLOCK_HEIGHT)
                    # Desenha o quadrado sem borda
                    pygame.draw.rect(tela, cor, quadrado)
                    # Desenha a borda do quadrado
                    pygame.draw.rect(tela, (138, 138, 138), quadrado, 1)
            pygame.display.flip()

        def desenhar_caminho(caminho):
            if caminho:
                # Obter o caminho invertido
                caminho_invertido = caminho[::-1]
                for i, no in enumerate(caminho_invertido):
                    lin, col = no.x, no.y
                    x = col * BLOCK_WIDTH
                    y = lin * BLOCK_HEIGHT
                    quadrado = pygame.Rect(x, y, BLOCK_WIDTH, BLOCK_HEIGHT)
                    
                    # Desenhar o bloco sem borda
                    pygame.draw.rect(tela, AZUL, quadrado)
                    
                    # Desenhar a borda do bloco
                    pygame.draw.rect(tela, (40, 40, 40), quadrado, 1)

                    # Apagar o bloco anterior
                    if i > 0:
                        lin, col = caminho_invertido[i-1].x, caminho_invertido[i-1].y
                        rect = pygame.Rect(col*BLOCK_WIDTH, lin*BLOCK_HEIGHT, BLOCK_WIDTH, BLOCK_HEIGHT)
                        cor = mapa_cores[matriz[lin][col]]
                        pygame.draw.rect(tela, cor, rect)

                    pygame.display.flip()

                    # Desenha a borda da matriz novamente
                    for lin in range(len(matriz)):
                        for col in range(len(matriz[lin])):
                            quadrado = pygame.Rect(col * BLOCK_WIDTH, lin * BLOCK_HEIGHT, BLOCK_WIDTH, BLOCK_HEIGHT)
                            pygame.draw.rect(tela, (60, 60, 60), quadrado, 1)

                    pygame.display.flip()

                    time.sleep(0.1)

        # Desenhe a matriz inicial na tela
        desenhar_matriz(matriz)
        desenhar_caminho(caminho)
        # Iniciar o loop do jogo
        running = True
        while running:

            # Eventos tecla espaco muda mapa
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        running = False
                    if event.key == pygame.K_LEFT:
                        desenhar_caminho(caminho)
            
       

            # Atualizar o display
            pygame.display.flip()
            time.sleep(0.01)

        # Sair do Game
    finally:
        pygame.quit()



    


