# Desenvolva um programa que solicite ao usuário que informe dados referentes ao seu carro e uma determinada viagem:
# consumo de combustível do carro (Kl/litros),
# valor do litro de combustível (R$),
# distância percorrida (Km),
# total de pedágios no trajeto e o valor unitário de cada pedágio (R$).
# Calcule o gasto total da viagem (combustível mais pedágios)
# e mostre uma mensagem com esse resultado, conforme determinado nos exemplos abaixo.

consumo = float(input("Insira o consumo de combustível do automóvel (km/L): "))
valorL = float(input("Insira o valor do litro de combustível (R$): "))
dist = float(input("Insira a distância percorrida (km): "))
ped = int(input("Insira o número de pedágios no trajeto: "))
pedVal = float(input("Insira o valor unitário de cada pedágio: "))

consumoTotal = dist / consumo
consumoValor = consumoTotal * valorL
pedTotal = ped * pedVal

total = consumoValor + pedTotal

print(f'O Valor total gasto na viagem foi de R${total: .2f}')
