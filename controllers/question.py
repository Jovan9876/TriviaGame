import pygame.locals
import pygame

from .base import PygameController


class Question(PygameController):
    """Difficulty choice controller"""

    def __init__(self, view, score, difficulty, start_time):
        """Constructor - sets variables"""
        super().__init__(view)
        self.difficulty = ''
        self.answer = 0
        self.correct_index = self.view.question.answer_id
        self.score = score
        mapping = {
            'easy': 1,
            'medium': 2,
            'hard': 3,
        }
        self.difficulty = mapping.get(difficulty, 1)
        self.start_time = start_time

    def process(self, event):
        """
        This method overrides the parent's.
        Its job is to do something when the user hits a number.
        """
        running = super().process(event)

        if running is False:
            return False

        if event.type == pygame.KEYUP:
            t1 = pygame.time.get_ticks()
            key = pygame.key.name(event.key)
            if key in '1234' and key == str(self.correct_index):
                elapsed_time = (t1 - self.start_time) / 100
                if elapsed_time > 10:
                    self.score += (10 * self.difficulty)
                elif elapsed_time < 10:
                    self.score += int(self.difficulty *
                                      (2000 / elapsed_time - 19 * elapsed_time))
            print(f'Score: {self.score}')
            return False
        return True
