#5. Imprimir todos los números pares hasta n:

def numeros_pares(n):
    for i in range(2, n + 1, 2):
        print(i)

numeros_pares(50)