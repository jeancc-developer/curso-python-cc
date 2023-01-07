segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

a = segundos // 86400 # Calculo de dias
b = (segundos // 3600) - (a * 24)  # Calculo de horas
seg_restantes = segundos % 3600
c = seg_restantes // 60 # Calculo de minutos
d = seg_restantes % 60 # Calculo de segundos


print(a, "dias,", b,"horas,", c, "minutos e", d,"segundos.")
