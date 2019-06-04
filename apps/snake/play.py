import pygame
from apps.snake.game import Game
from apps.snake.menu import StartMenu


class Play:
    def __init__(self):
        self.menu = None
        self.game = None
        self.screenX = 1000
        self.screenY = 500
        self.start()

    def run(self, speed, size):
        del self.menu
        self.game = Game(self, speed, size)
        self.game.loop()

    def restart(self):
        del self.game
        self.start()

    def start(self):
        pygame.init()
        self.menu = StartMenu(self)
        self.menu.mainloop()
