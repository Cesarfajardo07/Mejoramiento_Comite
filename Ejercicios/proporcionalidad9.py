#9. Imprimir los números impares entre dos valores:

def numeros_impares(inicio, fin):
    i = inicio
    while i <= fin:
        if i % 2 != 0:
            print(i)
        i += 1

resultado=numeros_impares(1, 10)
print(resultado)