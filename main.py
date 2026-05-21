import pygame
pygame.init()

pantalla = pygame.display.set_mode((480, 480))

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
CASILLA = 60

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    for fila in range(8):
        for col in range(8):
            if (fila + col) % 2 == 0:
                color = BLANCO
            else:
                color = NEGRO

            pygame.draw.rect(
                pantalla,color,
                (col * CASILLA, fila * CASILLA, CASILLA, CASILLA)
            )

    pygame.display.update()
