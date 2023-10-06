# Desenvolva um programa que solicite ao usuário que informe um valor positivo, com até uma casa decimal,
# que representa uma temperatura em graus Fahrenheit. Calcule a temperatura correspondente em graus Celsius e
# mostre uma mensagem com o resultado, conforme determinado nos exemplos abaixo.

tempF = float(input("Informe a temperatura em Fahrenheit: "))

tempC = (tempF - 32) * 5 / 9

print(f'A temperatura em Celsius é de {tempC: .1f}°')
