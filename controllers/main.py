"""
Jovan Sandhu A01201367
ACIT 2515, Set 2C
Nov 20, 2021
Trivia Pygame
"""



import pygame

from controllers import End, Difficulty, Question
from views import EndView, DifficultyView, QuestionView
from models import Game



def main():
    """Main program"""

    # Initialize pygame
    pygame.init()

    # Create a window
    window = pygame.display.set_mode((1000, 500))

    # Create the game view and controller
    game_view = DifficultyView(window)
    diffChoice = Difficulty(game_view)

    diffChoice.run()
    game = Game(diffChoice.difficulty)
    score = 0
    for question in game.questions:
        quest = QuestionView(window, question)
        start_time = pygame.time.get_ticks()
        trivia = Question(quest, score, diffChoice.difficulty, start_time)
        trivia.run(stop_after=10)
        score = trivia.score
    end_view = EndView(window, score)
    end = End(end_view)
    end.run()



if __name__ == "__main__":
    main()
