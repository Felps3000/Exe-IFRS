# Desenvolva um programa que solicite ao usuário que informe três valores inteiros positivos.
# Mostre uma mensagem com os valores em ordem crescente

num1 = int(input("Insira o primeiro número inteiro: "))
num2 = int(input("Insira o segundo número inteiro: "))
num3 = int(input("Insira o terceiro número inteiro: "))

numeros = [num1, num2, num3]

if any(val <= 0 for val in numeros):
    print("-")

else:
    print(sorted(numeros))
