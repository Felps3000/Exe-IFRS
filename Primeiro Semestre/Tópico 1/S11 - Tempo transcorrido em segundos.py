# Desenvolva um programa que solicite ao usuário que informe três valores positivos,
# que representam, respectivamente, as horas, minutos e segundos em um determinado momento do dia.
# Calcule o total de segundo transcorridos neste dia e mostre uma mensagem com o resultado,
# conforme determinado nos exemplos abaixo.

horas = int(input("Insira a quantidade de horas: "))
minutos = int(input("Insira a quantidade de minutos: "))
segundos = int(input("Insira a quantidade de segundos: "))

horasTotal = horas * 3600
minutosTotal = minutos * 60

total = horasTotal + minutosTotal + segundos

print(f'O total transcorrido neste dia foi de {total} segundos.')
