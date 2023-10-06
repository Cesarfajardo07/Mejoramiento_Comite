#4. Calcular la suma de los primeros n números 

def suma_n_numeros(n):
    suma = 0
    i = 1
    while i <= n:
        suma += i
        i += 1
    return suma

resultado=suma_n_numeros(2)
print(resultado)