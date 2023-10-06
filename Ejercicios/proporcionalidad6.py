#6. Calcular el área de un triángulo:

def area_triangulo(base, altura):
    if base > 0 and altura > 0:
        return (base * altura) / 2
    else:
        return "Error: valores inválidos."
    
resultado=area_triangulo(4, 2)
print(resultado)