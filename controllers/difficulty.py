import pygame.locals

from .base import PygameController

rectEasy = pygame.Rect(10, 170, 100, 100)
rectMed = pygame.Rect(210, 170, 100, 100)
rectHard = pygame.Rect(390, 170, 100, 100)


class Difficulty(PygameController):
    """Difficulty choice controller"""

    def __init__(self, view):
        """Constructor - sets variables"""
        super().__init__(view)
        self.difficulty = ''

    def process(self, event):
        """
        This method overrides the parent's.
        Its job is to do something when the user clicks in the shape.
        """

        # First call the parent method, just in case we want to exit
        running = super().process(event)

        if running is False:
            return False

        if event.type == pygame.locals.MOUSEBUTTONDOWN:
            # Check the click position, and register the number of clicks
            easy = rectEasy.collidepoint(pygame.mouse.get_pos())
            medium = rectMed.collidepoint(pygame.mouse.get_pos())
            hard = rectHard.collidepoint(pygame.mouse.get_pos())
            if (easy):
                self.difficulty = 'easy'
            elif (medium):
                self.difficulty = 'medium'
            elif (hard):
                self.difficulty = 'hard'
            return False
        return True
