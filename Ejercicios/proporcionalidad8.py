#8. Comprobar si un número es positivo, negativo o cero:

def tipo_numero(numero):
    if numero > 0:
        return "Positivo"
    elif numero < 0:
        return "Negativo"
    else:
        return "Cero"

resultado=tipo_numero(-4)
print(resultado)