import pygame
import time

while (True):
    pygame.init()
    img_fundo = pygame.image.load('./images/fundo.png')
    tela = pygame.display.set_mode([640, 480])
    pygame.display.set_caption('Jogo da forca')
    tela.fill([65, 105, 225])
    rect = img_fundo.get_rect()
    rect.left, rect.top = [0, 0]
    tela.blit(img_fundo, rect)

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit
