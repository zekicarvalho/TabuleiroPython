''' 
Oito filas com oito casas para representar um tabuleiro.
fila8 e fila7 peças pretas e fila2 e fila1 peças brancas.
'''

fila8 = {
    'A': 'Tp', 'B': 'Cp', 'C': 'Bp', 'D': 'Qp', 'E': 'Kp', 'F': 'Bp', 'G': 'Cp', 'H': 'Tp'
}
fila7 = {
    'A': 'Pp', 'B': 'Pp', 'C': 'Pp', 'D': 'Pp', 'E': 'Pp', 'F': 'Pp', 'G': 'Pp', 'H': 'Pp'
}
fila6 = {
    'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': []
}
fila5 = {
    'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': []
}
fila4 = {
    'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': []
}
fila3 = {
    'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': []
}
fila2 = {
    'A': 'Pb', 'B': 'Pb', 'C': 'Pb', 'D': 'Pb', 'E': 'Pb', 'F': 'Pb', 'G': 'Pb', 'H': 'Pb'
}
fila1 = {
    'A': 'Tb', 'B': 'Cb', 'C': 'Bb', 'D': 'Qb', 'E': 'Kb', 'F': 'Bb', 'G': 'Cb', 'H': 'Tb'
}

#função limpar retira o valor da peça em sua posição de saída para evitar duplicação.
def limpar(filaEstou, casaEstou):
    globals()[filaEstou][casaEstou] = vazio

#função mover colocar o valor da peça em sua posição de chegada.
def mover(filaVou, casaVou):
    globals()[filaVou][casaVou] = piece

#função start nos mostra o tabuleiro.
def start():
    print(fila8)
    print(fila7)
    print(fila6)
    print(fila5)
    print(fila4)
    print(fila3)
    print(fila2)
    print(fila1)

#laço de repetição criado para dar proseguimento a partida, pode ser interrompido por 'sair'.
while True:
    start()
    piece = input("""
Digite 'sair' para encerrar.
Qual peça deseja mover? (Permitidas: Pb, Tb, Cb, Bb, Qb ou Kb)
Jogador1 (brancas) > """)
    if (piece == 'sair'):
        print('Adeus.')
        break
    else:
        vazio = [] #valor a ser adicionado na posição de saída para ajudar a função limpar.
        filaEstou = input('Qual fileira você esta? (Ex: "fila1" até "fila8") ')
        filaVou = input('Para qual fileira você vai? ')
        colunaEstou = input('Qual coluna você esta? (Ex: "A" até "H") ')
        colunaVou = input('Para qual coluna você vai? ')
        limpar(filaEstou, colunaEstou)
        mover(filaVou, colunaVou)

    start()
    piece = input(""" 

Digite 'sair' para encerrar.
Qual peça deseja mover? (Permitidas: Pp, Tp, Cp, Bp, Qp ou Kp)
Jogador2 (pretas) > """)
    if (piece == 'sair'):
        print('Adeus.')
        break
    else:
        vazio = [] #valor a ser adicionado na posição de saída para ajudar a função limpar.
        filaEstou = input('Qual fileira você esta? (Ex: "fila1" até "fila8") ')
        filaVou = input('Para qual fileira você vai? ')
        colunaEstou = input('Qual coluna você esta? (Ex: "A" até "H") ')
        colunaVou = input('Para qual coluna você vai? ')
        limpar(filaEstou, colunaEstou)
        mover(filaVou, colunaVou)
