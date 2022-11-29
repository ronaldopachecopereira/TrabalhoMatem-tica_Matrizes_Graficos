import time
import numpy as np
from numpy import matrix
import matplotlib.pyplot as plt



def calcula_det(A):
    tempo_inicial = time.perf_counter_ns()
    det = np.linalg.det(A)
    tempo_final = time.perf_counter_ns()
    demoraProc = tempo_final - tempo_inicial

    return demoraProc, det


matrix_list = []

matrix_list.append(matrix([[2,3,-1,2],
                     [0,4,-3,5],
                     [1,2,1,3],
                     [0,4,1,0]]))

matrix_list.append(matrix([[1, 2, 9, 4, 5],
                    [7, 3, 1, 1, 6],
                    [2, 5, 8, 1, 7],
                    [4, 4, 2, 4, 9],
                    [1, 4, 4, 4, 1]]))

matrix_list.append(matrix([[1, 2, 9, 4, 5,4],
                    [7, 3, 1, 1, 6,3],
                    [2, 5, 8, 9, 7,2],
                    [4, 4, 2, 4, 9,1],
                    [1, 4, 4, 4, 1,7],
                    [1, 4, 4, 4, 1,8]]))

matrix_list.append(matrix([[1, 2, 9, 1, 4, 5,4],
                    [7, 3, 1, 1, 1, 6,3],
                    [2, 5, 8, 9, 1, 7,2],
                    [4, 4, 2, 7,4, 9,1],
                    [1, 4, 4, 9, 4, 1,7],
                    [1, 4, 5, 9, 4, 1,8],
                    [1, 4, 4, 7, 4, 1,8]]))

matrix_list.append(matrix([[6, 1, 2, 9, 1, 4, 5,4],
            [4, 7, 3, 1, 1, 1, 6,3],
            [2, 2, 5, 8, 9, 1, 7,2],
            [3, 4, 4, 2, 7,4, 9,1],
            [2, 1, 4, 4, 8, 4, 1,7],
            [1, 1, 4, 5, 4, 4, 1,8],
            [3, 1, 4, 4, 7, 4, 1,8],
            [2, 1, 4, 4, 7, 4, 1,8]]))

matrix_list.append(matrix([[6, 1, 2, 9, 1, 4, 5, 4, 7],
            [4, 7, 3, 1, 1, 1, 6, 3, 8],
            [2, 2, 5, 8, 9, 1, 7, 2, 9],
            [3, 4, 4, 2, 7, 4, 9, 1, 5],
            [2, 1, 4, 4, 6, 4, 1, 7, 7],
            [1, 1, 4, 5, 4, 5, 1, 8, 2],
            [3, 1, 4, 4, 7, 4, 1, 8, 2],
            [2, 1, 4, 4, 8, 4, 1, 8, 7],
            [2, 1, 4, 4, 7, 4, 1, 8, 7]]))

demora_procs = []
lista_tamanhos = []

for matrix in matrix_list:
    lmatrix = len(matrix)
    print(f"Processando Matrix quadrada de tamanho {lmatrix}")
    resultado = calcula_det(matrix)
    demora_procs.append(resultado[0])
    lista_tamanhos.append(f"{lmatrix}x{lmatrix}")
    print(f"Determinante da Matrix de tamanho {lmatrix}: {resultado[1]:.0f}")


plt.bar(lista_tamanhos, demora_procs, color='purple')
plt.xticks(lista_tamanhos)
plt.xlabel('Tamanho da Matriz')
plt.ylabel('Tempo Decorrido em Nanosegundos')
plt.title('Relação tempo de execução X tamanho da Matriz')
plt.show()