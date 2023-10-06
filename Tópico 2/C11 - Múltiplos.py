# Desenvolva um programa que solicite ao usuário que informe dois valores inteiros e positivos,
# verifica se são múltiplos e apresenta essa informação

valor1 = int(input(f"Insira o primeiro valor inteiro e positivo: "))
valor2 = int(input(f"Insira o segundo valor inteiro e positivo: "))

if (valor1 <= 0) or (valor2 <= 0):
    print(f"-")

elif (valor1 % valor2 == 0) or (valor2 % valor1 == 0):
    print(f"Sim")

else:
    print(f"Não")
