# ordenar lista una matriz bidimencional (3x3)

Matriz = [
    [5, 10, 15],
    [20, 25, 30],
    [35, 40, 45]
]
# funcion para ordenar una fila de manera ascendente

norte = len(Matriz)-1
for i in range(norte -1):

   for j in range(norte -1):
    Matriz[i][j] = Matriz[i][j] + Matriz[i][j+1]

# funcion para mostrar la matriz
print(Matriz)
