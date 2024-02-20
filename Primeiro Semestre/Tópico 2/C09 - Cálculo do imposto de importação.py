# Desenvolva um programa que solicite ao usuário que informe valores positivos
# com até duas casas decimais que representa o total de um pedido de importação de equipamentos.
# Calcule o total de imposto a ser recolhido,
# sabendo que para o cálculo existem três faixas de valores/tarifa, apresentadas pela tabela abaixo:
#
# Valor                     Taxa
# até R$1.000,00	        Isento
# - - - - - - - - - - - - - - -
# mais de R$1.000,00
# e menos de R$2.000,00	     10%
# - - - - - - - - - - - - - - -
# mais de R$2.000,00 	     20%
# - - - - - - - - - - - - - - -
#
# Ao final, o programa deve mostra uma mensagem com o valor total do imposto

valor = float(input("Insira o valor total do pedido: "))

if 1000 < valor < 2000:

    valor = valor - 1000

    valor = (10 * valor) / 100

    print(f"{valor: .2f}")

elif valor > 2000:

    valor = valor - 2000

    valor = (20 * valor) / 100 + 100

    print(f"{valor: .2f}")

else:
    print(f"0,0")
