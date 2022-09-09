from .base import PygameView


class EndView(PygameView):
    """View when the game is won"""

    def __init__(self, view, score):
        super().__init__(view)
        self.score = score

    def draw(self):

        self.window.fill((50, 50, 50))

        end = self.render_text_surface("Game ended.")
        self.window.blit(end, (200, 40))
        score = self.render_text_surface(f'Your score was: {str(self.score)}')

        self.window.blit(score, (200, 200))
