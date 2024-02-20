# O cozinheiro é responsável pela produção e distribuição das refeições de uma empresa de viagens.
# Para saber quantas refeições congeladas ele solicita que lhe informem
# quantos viajantes compõem o grupo e quantos dias será a viagem.
# Desenvolva um programa para um usuário informar quantos viajantes e quantos dias de viagem,
# para depois calcular e mostrar o total de refeições que o cozinheiro deve entregar.

viajante = int(input("Informe o número de viajantes: "))
dias = int(input("Informe a duração da viagem em dias: "))

print(f'O total de refeições congeladas necessárias é: {viajante*dias} refeições')
