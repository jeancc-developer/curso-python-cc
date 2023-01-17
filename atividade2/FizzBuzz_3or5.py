
print("----- Número divisivel por 3 ou por 5 -------")

num = int(input("Digite um número: "))
result_3 = num % 3
result_5 = num % 5
if ((result_3 == 0) and (result_5 == 5 or result_5 == 0)):
    print("FizzBuzz")
else:
    print(num)