#1. Calcular el cuadrado de un número:  Ejemplo: Numero(5) = 5x5=25

def cuadrado(numero):
    i = 0
    resultado = 0
    while i < numero:
        resultado += numero
        #i += 1
    return resultado

resultado=cuadrado(2)
print(resultado)