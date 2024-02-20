# Desenvolva um programa que solicite ao usuário que informe um valor positivo,
# com até uma casa decimal, que representa uma temperatura em graus Fahrenheit.
# Calcule a temperatura correspondente em Kelvin e mostre uma mensagem com o resultado,
# conforme determinado nos exemplos abaixo.

tempF = float(input("Informe a temperatura em Fahrenheit: "))
tempK = ((tempF-32) * 5) / 9 + 273

print(f'A temperatura em Kelvin é de {tempK: .2f}')
