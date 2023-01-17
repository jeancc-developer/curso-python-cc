import math

print("----- Equação do segundo grau -------")
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

delta = math.pow(b, 2) - 4 * a * c

if (a == 0):
    print("Não atende a função do segundo grau")
    print("a deve ser maior que 0")
else:
    if(delta > 0):
        raiz = math.sqrt(delta)
        x1 = (-b + raiz) / (2 * a)
        x2 = (-b - raiz) / (2 * a)
        print("Raiz de x1 é:",x1,"Raiz de x2 é:", x2)

    elif(delta == 0):
        print("A equação possui apenas uma raiz")
        x1 = (-b) / (2 * a)
        print("Raiz de x é:",x1)

    else:
        print("A equação não possui raiz")