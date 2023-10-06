#14. Comprobar si un número es divisible por otro:

def divisible(num1, num2):
    if num2 != 0 and num1 % num2 == 0:
        return True
    else:
        return False
    
resultado=divisible(2,12)
print(resultado)
