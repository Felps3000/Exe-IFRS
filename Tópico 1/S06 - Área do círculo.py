# Desenvolva um programa que solicite ao usuário que informe um valore
# positivo inteiro que representa o diâmetro de um círculo em cm,
# calcule a área deste círculo e mostre uma mensagem com o resultado, conforme determinado nos exemplos abaixo.
#
# Obs.: Use PI = 3.1415

import math

diam = int(input("Insira o diâmetro do círculo (cm): "))

raio = int(diam / 2)

area = math.pi * (raio * raio)

print(f'A área total do círculo é de {area: .2f} cm²')
