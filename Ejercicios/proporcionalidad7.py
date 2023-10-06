#7. Calcular la media de una lista de números:

def media_lista(lista):
    suma = 0
    for num in lista:
        suma += num
    return suma / len(lista)

lista=[1, 2, 3, 4]
resultado=media_lista(lista)
print(resultado)
