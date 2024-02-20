# Desenvolva um programa que solicite ao usuário que informe três valores inteiros positivos,
# os quais representam três segmentos de reta.

a = int(input("Digite o primeiro valor inteiro positivo: "))
b = int(input("Digite o segundo valor inteiro positivo: "))
c = int(input("Digite o terceiro valor inteiro positivo: "))

print(f"É possível compôr um triângulo?", end=" ")

if a <= 0 or b <= 0 or c <= 0:

    print("Inválido")

elif (a < (b + c)) & (b < (a + c)) & (c < (a + b)):
    print("sim")

else:
    print("não")
