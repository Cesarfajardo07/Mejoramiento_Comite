#12. Imprimir los números primos hasta un número dado:

def numeros_primos(n):
    i = 2
    while i <= n:
        es_primo = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                es_primo = False
                break
        if es_primo:
            print(i)
        i += 1

resultado=numeros_primos(10)
print(resultado)