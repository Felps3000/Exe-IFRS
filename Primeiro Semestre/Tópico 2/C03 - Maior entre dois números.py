# Desenvolva um programa que solicite ao usuário que informe dois valores inteiros positivos.
# Verifique qual deles é maior, e mostre uma mensagem com o resultado

valor1 = int(input("Digite o primeiro valor inteiro: "))
valor2 = int(input("Digite o segundo valor inteiro: "))

print("\nQual valor é maior?")

if valor1 <= 0 or valor2 <= 0:
    print("\nInválido")

elif valor1 > valor2:
    print("\nPrimeiro")

elif valor1 < valor2:
    print("\nSegundo")

elif valor1 == valor2:
    print("\nIguais")
