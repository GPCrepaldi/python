import pygame
pygame.init()
caminho_mp3 = 'WelcomeToPlanetUrf.mp3'
pygame.mixer.init()
pygame.mixer.music.load(caminho_mp3)
pygame.mixer.music.play()
pygame.event.wait()