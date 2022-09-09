import requests
from .question import Question


class Game:
    def __init__(self, difficulty="easy", num=10 ):
        stuff = requests.get("https://opentdb.com/api.php?amount=" + str(num) +
                             "&difficulty=" + str(difficulty) + "&type=multiple&category=9").json()
        self.questions = [
            Question(
                elem["question"],
                elem["correct_answer"],
                elem["incorrect_answers"],
            )
            for elem in stuff["results"]
        ]

