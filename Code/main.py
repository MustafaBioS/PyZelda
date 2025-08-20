import pygame, sys
from settings import *
from level import Level
import tracemalloc
import time
tracemalloc.start()
for i in range(10):
    a = [j for j in range(100000)]  # simulate work
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current: {current / 1024 / 1024:.2f} MB, Peak: {peak / 1024 / 1024:.2f} MB")
    time.sleep(1)
tracemalloc.stop()

class Game():
    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('PyZelda')
        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()


