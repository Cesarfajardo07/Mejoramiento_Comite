#18. Comprobar si un número es par o impar:

def par_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Impar"
    
resultado=par_impar(6)
print(resultado)