
# Programa 1: Busqueda en Matriz bidimencional

def buscar_valor(matriz,valor):

 for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == valor:
            return matriz[i][j]
        return i,j #return la posicion si lo encuentra
    return None #return name si no esta
 # Matriz 3x3
Matriz = [[10,20,30],
          [40,50,60],
          [70,80,90]
          ]

# solicita valor a buscar

buscar = buscar_valor(Matriz,valor=10)
# resultado = buscar_valor(matriz,valor_buscar)
if buscar:
    resultado = 42
    print(resultado)

else:
    print('No se encontra la posicion en la matriz')
