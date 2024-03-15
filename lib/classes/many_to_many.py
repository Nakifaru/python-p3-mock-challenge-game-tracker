class Game:

    all = []

    def __init__(self, title):
        self._title = title
        Game.all.append(self)
    @property
    def title(self):
        if isinstance(self._title, str) and len(self._title) > 0:
            return self._title
    @title.setter
    def title(self, title):
        if hasattr(Game, 'title'):
            print('Cannot change title')

    def results(self):
        pass

    def players(self):
        pass

    def average_score(self, player):
        pass

class Player:

    all = []

    def __init__(self, username):
        self._username = username
        Player.all.append(self)
    @property
    def username(self):
        if isinstance(self._username, str) and 2 <= len(self._username) <= 16:
            return self._username
        
    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username

    def results(self):
        pass

    def games_played(self):
        pass

    def played_game(self, game):
        pass

    def num_times_played(self, game):
        pass

class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    @property
    def score(self):
        if isinstance(self.score, int) and 1 <= self.score <= 5000:
            return self.score
    @score.setter
    def score(self, score):
        if hasattr(Result, 'score'):
            print('Cannot change score')

    @property
    def player(self):
        if isinstance(self.player, Player):
            return self.player

    @property
    def game(self):
        if isinstance(self.game, Game):
            return self.game