class GameContext:
    _instance = None

    @staticmethod
    def getGameContext( _village, _foret, _donjon, _player):
        if GameContext._instance==None:
            GameContext._instance = GameContext( _village, _foret, _donjon, _player)
        return GameContext._instance


    def __init__(self, _village, _foret, _donjon, _player):
        self.village = _village
        self.Foret = _foret
        self.donjon= _donjon
        self.player = _player

    def launch(self):

        pass

    def save(self):
        pass

    def load(self):
        pass

    
