import pygame
import constantes

pygame.init()

ventana = pygame.display.set_mode((constantes.ANCHO_PANTALLA, 
                                   constantes.ALTO_PANTALLA))
run = True

while run == True:
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               run = False
pygame.quit() 