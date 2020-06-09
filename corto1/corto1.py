#Secuencia Collatz

def collatz(numero):
    if (numero % 2 == 0):
        return numero // 2
    elif (numero %  2 == 1):
        return numero * 3 + 1
    else:
        print('algo no funciona por el momento')
        return None

print('Ingresar un numero.')
numero = int(input())
print('Secuencia Collatz:')
while (numero !=1):
    numero = collatz(numero)
    print(numero)
print(numero)