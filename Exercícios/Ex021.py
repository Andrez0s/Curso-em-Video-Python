# Importar e reproduzir arquivo mp3
import pygame

pygame.init()
pygame.mixer.music.load('Ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input()
