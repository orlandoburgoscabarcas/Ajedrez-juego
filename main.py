#python -m venv venv 
#.\venv\scripts\activate.ps1
#pip install pygame-ce


import pygame
pygame.init()

pantalla = pygame.display.set_mode((480, 480))

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
CASILLA = 60

fuente = pygame.font.SysFont("segoeuisymbol", 48)


piezas = [
    ["♜","♞","♝","♛","♚","♝","♞","♜"],
    ["♟","♟","♟","♟","♟","♟","♟","♟"],
    ["","","","","","","",""],
    ["","","","","","","",""],
    ["","","","","","","",""],
    ["","","","","","","",""],
    ["♙","♙","♙","♙","♙","♙","♙","♙"],
    ["♖","♘","♗","♕","♔","♗","♘","♖"]
]


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
            # Dibujar piezas
            pieza = piezas[fila][col]

            if pieza != "":
                texto = fuente.render(pieza, True, (255, 0, 0))

                pantalla.blit(
                    texto,
                    (col * CASILLA + 10, fila * CASILLA + 5)
                )


    pygame.display.update()
