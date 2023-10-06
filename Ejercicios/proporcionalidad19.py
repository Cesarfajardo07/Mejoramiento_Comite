#19. Sumar los dígitos de un número:

def suma_digitos(numero):
    suma = 0
    while numero != 0:
        suma += numero % 10
        numero //= 10
    return suma

resultado=suma_digitos(320)
print(resultado)