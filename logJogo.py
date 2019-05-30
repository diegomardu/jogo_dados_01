class logJogo:
    def __init__(self,nome="",pontos=0,resultado=""):
        self._nome = nome
        self._pontos = pontos
        self._resultado = resultado

    def getNome(self):
        return self._nome
    def setNome(self,nome):
        self._nome = nome

    def getPontos(self):
        return self._pontos
    def setPontos(self,pontos):
        self._pontos = pontos

    def getResultado(self):
        return self._resultado
    def setResultado(self,resultado):
        self._resultado = resultado