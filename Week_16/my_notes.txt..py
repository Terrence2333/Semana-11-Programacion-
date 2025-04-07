# abrir archivo para escritura
from os import write
Archivo = open("datos.txt","w")
# write  3 line
Archivo.write("Aprender algo como la ingineria de programacion es muy fascinante./")

Archivo.write("Se demostro que la edad nunca es impedimento para formarce como profecional./")

Archivo.write("Tambien se demostro que con diciplina, desicion y esfurezo los sueños se cumplen./")

# Cerrar el archivo despues de escribir
Archivo.close()
# Abrir archivo para lectura
Archivo = open("datos.txt","r")
# indicar la lectura linea a linea

print(Archivo.readline())

Archivo.close()