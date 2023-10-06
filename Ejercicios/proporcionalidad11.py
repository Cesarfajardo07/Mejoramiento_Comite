#11. Calcular el factorial de un número: Ejemplo= NUMERO(5) FACTORIAL= 1*2*3*4*5 = 120

def factorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

resultado=factorial(5)
print(resultado)