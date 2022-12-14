from JogoDaVelha import criarBoard, printBoard, getInputValido, \
                        verificarMovimento, fazMovimento, verificaGanhador


jogador = 0
board = criarBoard()
ganhador = verificaGanhador(board)
while(not ganhador):
    printBoard(board)
    i = getInputValido("Digite a linha: ")
    j = getInputValido("Digite a coluna: ")

    if(verificarMovimento(board, i, j)):
        fazMovimento(board, i, j, jogador)
        jogador = (jogador + 1)%2
    else:
        print("A posição informada já está ocupada")

    ganhador = verificaGanhador(board)


print("========================")        
printBoard(board)
print("Ganhador = ", ganhador)
print("========================") 