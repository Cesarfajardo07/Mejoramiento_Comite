#3. Encontrar el máximo común divisor de dos números

def mcd(num1, num2):
    for i in range(min(num1, num2), 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i
        
resultado=mcd(15, 30)
print(resultado)