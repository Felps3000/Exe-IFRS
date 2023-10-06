#Desenvolva um programa que solicite ao usuário que informe um valor inteiro positivo,
# que representa o valor a ser sacado na máquina, que possui cédulas de 100, 20, 5 e 1.
# Calcule o menor número de cédulas possíveis no qual o valor pode ser decomposto
# e mostre uma mensagem com o resultado, conforme determinado nos exemplos abaixo.

valor = int(input("Insira o valor inteiro a ser sacado: "))

cedCem = int(valor // 100)
restoCem = int(valor % 100)

cedVinte = int(restoCem // 20)
restoVinte = int(restoCem % 20)

cedCinco = int(restoVinte // 5)

cedUm = int(restoVinte % 5)

print(f'\n{cedCem} de 100\n{cedVinte} de 20\n{cedCinco} de 5\n{cedUm} de 1')
