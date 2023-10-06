#13. Calcular el área de un rectángulo: Area = Base * Altura

def area_rectangulo(base, altura):
    if base > 0 and altura > 0:
        return base * altura
    else:
        return "Error: valores inválidos."
    
resultado=area_rectangulo(4, 2)
print(resultado)