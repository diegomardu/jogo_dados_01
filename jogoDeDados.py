from dado import dado
from logJogo import logJogo


class jodoDeDados:
    def __init__(self):
        self._dado1 = dado()
        self._dado2 = dado()
        self._log = []

    def jogar(self, nome):
        self._nome = nome
        self._dado1.lancar()
        self._dado2.lancar()
        soma = self._dado1.getFace() + self._dado2.getFace()
        if soma == 7:
            partida = logJogo(nome,soma,"Ganhou")
            self._log.append(partida)
            return True
        else:
            partida = logJogo(nome, soma, "Perdeu")
            self._log.append(partida)
            return False

    def obterHistoricoJogos(self):
        historico = ""
        for i in self._log:
            historico+= i.getNome() + " " + i.getResultado() + " com " + str(i.getPontos()) + "\n"
        return historico