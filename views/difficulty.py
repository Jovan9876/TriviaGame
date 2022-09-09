import pygame

from .base import PygameView


class DifficultyView(PygameView):
    """Main view for the game - draws a rectangle on the screen"""

    def draw(self):
        self.window.fill((50, 50, 50))

        rectEasy = pygame.Rect(10, 170, 100, 100)
        rectMed = pygame.Rect(210, 170, 100, 100)
        rectHard = pygame.Rect(390, 170, 100, 100)
        pygame.draw.rect(self.window, (255, 0, 0), rectEasy)
        pygame.draw.rect(self.window, (0, 255, 0), rectMed)
        pygame.draw.rect(self.window, (0, 0, 255), rectHard)

        easy = self.render_text_surface("Easy")
        medium = self.render_text_surface("Medium")
        hard = self.render_text_surface("Hard")
        self.window.blit(easy, (10, 170))
        self.window.blit(medium, (210, 170))
        self.window.blit(hard, (390, 170))
