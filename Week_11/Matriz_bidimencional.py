# Programa 1: Busqueda en Matriz Bidimencional

def buscar_valor(matriz,valor):

 for i in range(0,len(matriz)):
    for j in range(0,len(matriz[i])):
        if matriz[i][j] == valor:
            return matriz[i][j]
        return i,j #return la posicion si lo encuentra
    return None #return name si no esta
 # Matriz 3x3
Matriz = [[10,20,30],[40,50,60],[70,80,90]]

# solicita valor a buscar

buscar = buscar_valor(Matriz,10)
# resultado = buscar_valor(matriz,valor_buscar)
if buscar:


 print(f'valor encontrado en la posicion: {buscar[ressultado]}')
else:
    print('No se encontra la posicion en la matriz')