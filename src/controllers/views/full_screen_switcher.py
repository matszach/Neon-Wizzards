import pygame


def set_windowed_mode():
    import main as m
    m.flags[0] = pygame.RESIZABLE | pygame.DOUBLEBUF
    m.surface[0] = pygame.display.set_mode((0, 0), m.flags[0])


def set_full_screen_mode():
    import main as m
    m.flags[0] = pygame.FULLSCREEN | pygame.DOUBLEBUF
    m.surface[0] = pygame.display.set_mode((0, 0), m.flags[0])
