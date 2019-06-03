from jogoDeDados import jodoDeDados
jogador = jodoDeDados()
while True:
    print("1-Jogar\n2-Historico\n0-Sair")
    try:
        n = int(input("Opção Selecionada:"))
        if n == 1:
            resultado = jogador.jogar(input("Nome do jogador:"))
            if resultado:
                print("Parabens")
            else:
                print("Deu ruim")
        elif n == 2:
            historico = jogador.obterHistoricoJogos()
            print(historico)
        else:
            break
    except ValueError:
        print("Valor invalido")


