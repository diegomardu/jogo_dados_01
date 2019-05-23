from random import *

class dado:
    def __init__(self , face = 1):
        if (face >= 1) and (face <= 6):
            self._face = face
        else:
            self._face = 1

    def getFace(self):
        return self._face
    def lancar(self):
        cache = self._face
        while True:
            self._face = randint(1,7)
            if self._face != cache:
                break