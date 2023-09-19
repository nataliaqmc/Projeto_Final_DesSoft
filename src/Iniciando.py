#Importando as bibliotecas necessárias:
import pygame
from Classes import *
from Jogo import *
from Configuracoes import *
import imagem
import som
#Estrutura básica/principal do jogo
pygame.init()

g = Game()
g.tela_inicio()
#Estado do jogo
while g.running:
    g.novo_jogo()
    g.game_over()
 
pygame.quit()


    