import time
import numpy as np
import matplotlib.pyplot as plt

tempo_inicial_NP = time.perf_counter_ns()

MatrizNumpy = np.array([[2,3,-1,2],
                     [0,4,-3,5],
                     [1,2,1,3],
                     [0,4,1,0]])
#print("A Matriz 4x4 é:")
#print(MatrizNumpy)
det = np.linalg.det(MatrizNumpy)
print("\nDeterminante da matriz com Numpy é:", int(det))


tempo_final = time.perf_counter_ns()
demoraProc_NP= (tempo_final - tempo_inicial_NP)
print(f'\nO tempo de processamento do código com numpy foi de: {demoraProc_NP} nanosegundos')


tempo_inicial = time.perf_counter_ns()
def remover(A, tirar_i, tirar_j):
    matriz_nova = [[int(0) for i in range(len(A) - 1)] for j in range(
        len(A) - 1)]  # aqui cria uma matriz nova menor que a original, cheia de 0 que será usada pra calcular o cofator
    ni = 0
    for i in range(len(A)):
        nj = 0
        for j in range(len(A)):
            if j != tirar_j:
                matriz_nova[ni][nj] = A[i][j]  # percorre a matriz nova e incrementa com os valores da matriz original.
                nj += 1
        if i != tirar_i:
            ni += 1
    return matriz_nova


def determinante(A):
    if len(A) != len(A[0]): #verifica se a matriz informada é quadrada
        print("A matriz não é quadrada!")
        return A
    resposta = 0
    if len(A) == 2:  # Se a matriz for quadrada, a conta sera feita
        resposta = (A[0][0] * A[1][1]) - (A[1][0] * A[0][1])
        return resposta
    if len(A) > 2:
        for j in range(
                len(A)):  # aqui é verificado se é maior que 2 e ai sim faz a conta do cofator, incrementando até chegar na matriz -1(exemplo matriz 4x4, tem 3 contas cofatores)
            resposta += A[0][j] * (-1) ** (0 + j) * determinante(
                remover(A, 0, j))  # aqui é calculado o determinante da matriz nova.
        return resposta


matriz_4x4 = [[2,3,-1,2],
                     [0,4,-3,5],
                     [1,2,1,3],
                     [0,4,1,0]]
tempo_final = time.perf_counter_ns()
demoraProc = tempo_final - tempo_inicial

print("\nDeterminante da matriz sem numpy foi de :", determinante(matriz_4x4))
print("\nTempo para excecução sem numpy foi de: ", demoraProc ,"nanosegundos")

Matrizes=["Matriz sem numpy" , "Matriz com Numpy"]
TempoProc=[(demoraProc)*10, demoraProc_NP]

plt.bar(Matrizes, TempoProc, color='red')
plt.xlabel('Tamanho da Matriz')
plt.ylabel('Tempo Decorrido em Nanosegundos')
plt.title('Diferença entre processamento com numpy e sem numpy')

plt.show()
