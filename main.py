#python -m venv venv 
#.\venv\scripts\activate.ps1
#pip install pygame-ce


import pygame
pygame.init()

pantalla = pygame.display.set_mode((680, 680))

GRIS = (200, 200, 200)
NEGRO = (50, 50, 50)

CASILLA = 85

fuente = pygame.font.SysFont("segoeuisymbol", 65)

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

# Guarda la pieza seleccionada
seleccion = None

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()

        
        if event.type == pygame.MOUSEBUTTONDOWN:

            x, y = pygame.mouse.get_pos()

            col = x // CASILLA
            fila = y // CASILLA

            
            if seleccion == None:

                if piezas[fila][col] != "":
                    seleccion = (fila, col)

            
            else:

                fila2, col2 = seleccion

                piezas[fila][col] = piezas[fila2][col2]
                piezas[fila2][col2] = ""

                seleccion = None

    for fila in range(8):
        for col in range(8):

            if (fila + col) % 2 == 0:
                color = GRIS
            else:
                color = NEGRO

            pygame.draw.rect(
                pantalla,
                color,
                (col * CASILLA, fila * CASILLA, CASILLA, CASILLA)
            )

            pieza = piezas[fila][col]

            if pieza != "":

                if pieza in ["♔","♕","♖","♗","♘","♙"]:
                    color_pieza = (255, 255, 255)
                else:
                    color_pieza = (0, 0, 0)

                texto = fuente.render(pieza, True, color_pieza)

                pantalla.blit(
                    texto,
                    (col * CASILLA + 10, fila * CASILLA + 5)
                )

    pygame.display.update()
