

print("----- Soma dos digitos -------")

n = int(input("Digite o valor n: "))

i = 0
while n:
    i += n % 10  # Soma `s` ao ultimo numeral de `n`
    n //= 10  # Remove o ultimo numero de `n`
print(i)
