# Desenvolva um programa que solicite ao usuário que informe um valor inteiro.
# Verifique se este valor é par ou é ímpar, e mostre uma mensagem com o resultado

valor = int(input("Digite um valor inteiro: "))
print("O valor é par ou ímpar?", end=" ")
if valor % 2 == 0:
    print("Par")
else:
    print("Ímpar")
