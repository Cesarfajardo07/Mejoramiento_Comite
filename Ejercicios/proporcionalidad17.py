#17. Imprimir los números múltiplos de 5 entre dos valores usando un bucle while:


def multiplos_cinco(inicio, fin):
    i = inicio
    while i <= fin:
        if i % 5 == 0:
            print(i)
        i += 1

resultado=multiplos_cinco(1, 20)
print(resultado)