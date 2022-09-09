import pygame

from .base import PygameView


class QuestionView(PygameView):
    def __init__(self, window, question):
        super().__init__(window)
        self.question = question

    def draw(self):
        self.window.fill((50, 50, 50))

        # Draws the question on to the screen
        quest = self.render_text_surface(self.question.question)
        self.window.blit(quest, (20, 20))

        # Draws the options to the screen
        quest_num = 1
        y = 100
        for answers in self.question.answers:
            answer = self.render_text_surface(f'{quest_num}. {answers}')
            self.window.blit(answer, (20, y))
            quest_num += 1
            y += 40
