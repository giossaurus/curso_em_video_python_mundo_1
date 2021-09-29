#O pygame mudou um pouco desde a postagem do vídeo.
#Agora é necessário alterar a linha 2 para pygame.mixer.init() e inserir um input() na linha 5.

import pygame
pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()