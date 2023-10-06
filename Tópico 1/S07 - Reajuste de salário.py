# Desenvolva um programa que solicite ao usuário que informe dois valores positivos,
# com até duas casas decimais, que representam, respectivamente, o salário e o percentual de reajuste salarial.
# Calcule qual o novo salário e mostre uma mensagem com o resultado, conforme determinado nos exemplos abaixo.

salario = float(input("Informe o salário: "))
reajuste = float(input("Informe o valor do reajuste: "))

salarioNovo = salario * reajuste / 100 + salario

print(f'O novo valor do salário é de R${salarioNovo: .2f}')
