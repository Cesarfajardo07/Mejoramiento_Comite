#15. Calcular la raíz cuadrada de un número:

def raiz_cuadrada(numero):
    for i in range(numero + 1):
        if i * i == numero:
            return i
    return "No se encontró la raíz cuadrada entera."

resultado=raiz_cuadrada(25)
print(resultado)