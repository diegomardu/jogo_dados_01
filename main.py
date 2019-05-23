from jogoDeDados import jodoDeDados
jogador = jodoDeDados()
while True:
    print("1-Jogar\n2-Historico\n0-Sair")
    n = int(input("Opção Selecionada:"))
    if n == 1:
        jogador.jogar(input("Nome do jogador:"))
    elif n == 2:
        jogador.obterHistoricoJogos()
    else:
        break



