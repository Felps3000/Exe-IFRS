# Desenvolva um programa que solicite ao usuário que informe um valore inteiro positivo.
# Verifique se este valor é maior do que 100 e mostre uma mensagem com o resultado

valor = int(input("Digite um valor inteiro: "))
print("O valor é maior que 100?", end=" ")
if valor > 100:
    print("Sim")
else:
    print("Não")
