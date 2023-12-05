# Um sistema tributário progressivo é aquele que possui diferentes tarifas de imposto para determinadas faixas de renda,
# onde cada percentual é aplicado somente naquela faixa. Para este exercício, vamos usar a seguinte tabela:
#
# Faixas de Renda 	                 % de Imposto
#  de R$0,00 a R$1.000,00 	         0,0% (Isento)
#  de R$1.000,01 a R$2.000,00  	     10%
#  de R$2.000,01 a R$3.000,00  	     20%
#  de R$3.000,01 a R$4.000,00  	     30%
#  de R$4.000,01 a R$5.000,00     	 40%
#  acima de R$5.000,00 	             50%
#
# Para ilustrar, se uma pessoa recebe R$900,00, ela não pagará qualquer valor de imposto.
# Se outra pessoa recebe R$1.500,00, ela pagará 10% sobre R$500,00 e está isenta sobre R$1.000,00,
# totalizando um imposto de R$50,00. Por fim, se uma pessoa recebe R$3.200,00, tem isenção sobre R$1.000,00,
# paga 10% sobre mais R$1.000,00, paga mais 20% sobre outros R$1.000,00 e também paga 30% sobre R$200,00,
# totalizando R$360,00 de imposto a ser pago.
# OBS.: Lembrar que no programa, o divisor de centavos é o ponto e não a vírgula!
#
# O programa deve ler o valor total de uma renda e apresentar como resultado o valor de imposto a ser pago

valor = float(input("Insira o valor da sua renda mensal: "))

# isento
if valor < 1000:
    print(f"0.00")

# faixa de 1000,01 a 2000, pagando 10%
elif (valor > 1000) and (valor <= 2000):
    valor -= 1000  # retira mil pq os primeiros mil são isentos
    valor = valor * 0.10  # calcula os 10% do valor restante
    print(f"{valor: .2f}")

# faixa de 2000,01 a 3000, pagando 20%
elif (valor > 2000) and (valor <= 3000):
    valor -= 2000  # retira os mil inteiros
    valor = valor * 0.2 + 100  # 20% do valor restante mais 10% do 2º mil
    print(f"{valor: .2f}")

# faixa de 3000,01 a 4000, pagando 30%
elif (valor > 3000) and (valor <= 4000):
    valor -= 3000  # retira os mil inteiros
    valor = valor * 0.3 + 300  # 30% do valor restante mais 10% do 2º mil e 20% do 3º mil
    print(f"{valor: .2f}")

# faixa de 4000,01 a 5000, pagando 40%
elif (valor > 4000) and (valor <= 5000):
    valor -= 4000  # retira os mil inteiros
    valor = valor * 0.4 + 600  # 40% do valor restante mais 10% do 2º mil, 20% do 3º mil e 30% do 4º mil
    print(f"{valor: .2f}")

# faixa acima de 5000, pagando 50%
else:
    valor -= 5000  # retira os mil inteiros
    valor = valor * 0.5 + 1000  # 50% do valor restante mais 10% do 2º mil, 20% do 3º mil, 30% do 4º mil e 40% do 5º mil
    print(f"R${valor: .2f}")
