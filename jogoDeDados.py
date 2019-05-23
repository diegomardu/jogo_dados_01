from dado import dado
from logJogo import logJogo


class jodoDeDados:
    def __init__(self):
        self._dado1 = dado()
        self._dado2 = dado()
        self._log = []

    def jogar(self, nome):
        partida = logJogo("",0,"")
        self._nome = nome
        self._dado1.lancar()
        self._dado2.lancar()
        soma = self._dado1.getFace() + self._dado2.getFace()
        if soma == 7:
            partida.setNome(nome)
            partida.setPontos(7)
            partida.setResultado("Ganhou")
        else:
            partida.setNome(nome)
            partida.setPontos(soma)
            partida.setResultado("Perdeu")
        self._log.append(partida)
        print(partida.getResultado())
    def obterHistoricoJogos(self):
        for i in self._log:
            print("%s %s com %s pontos"%(i.getNome(),i.getResultado(),i.getPontos()))