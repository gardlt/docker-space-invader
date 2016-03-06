from settings import DEFAULT_LIVES
class Player:
    def __init__(self):
        self.lives = DEFAULT_LIVES
        self.score = 0

    def add_pointes(self, points):
        self.score = self.score + points
