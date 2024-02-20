# O técnico saiu de casa para atender um cliente. Estava com algum dinheiro na carteira e,
# depois do trabalho realizado, recebeu o pagamento desse cliente e voltou para casa.
# Desenvolva um programa que solicite ao usuário que informe dois valores inteiros,
# onde o primeiro representa o valor que o técnico já possuía e o segundo, o valor recebido pelo serviço prestado.
# Calcule e mostre com quanto dinheiro o técnico chegou em casa ao final do dia,
# conforme determinado nos exemplos abaixo.

saldo = int(input("Informe seu saldo anterior: "))
pagamento = int(input("Informe o valor recebido: "))

print(f'O seu saldo total é de R${saldo+pagamento}')
