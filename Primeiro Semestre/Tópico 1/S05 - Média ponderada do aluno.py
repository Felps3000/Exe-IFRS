# Agora o professor resolveu mudar a forma de avaliação:
# somente três provas e passou a considerar cada uma com peso diferente.
# Desenvolva um programa onde o professor informa a nota de cada uma das provas com seu peso.
# Dessa maneira, são digitados seis valores positivos
# - que podem conter até duas casas decimais -
# formando 3 pares de valores onde cada par é composto pela nota e o respectivo peso desta nota.
# Calcule a média final, utilizando a estratégia de média ponderada entre eles e mostre uma mensagem com o resultado,
# conforme determinado nos exemplos abaixo.
#
# No primeiro exemplo, os valores informados 5 2 6 2 6 4 indicam que a primeira nota (5) tem peso (2),
# a segunda nota (6) tem peso (2) e a terceira nota (6) tem peso (4).

nota1 = float(input("Insira a nota da primeira prova (0-10): "))
peso1 = float(input("Insira o peso da primeira prova (0-10): "))

nota2 = float(input("Insira a nota da segunda prova (0-10): "))
peso2 = float(input("Insira o peso da segunda prova (0-10): "))

nota3 = float(input("Insira a nota da terceira prova (0-10): "))
peso3 = float(input("Insira o peso da terceira prova (0-10): "))

provas = peso1*nota1 + peso2*nota2 + peso3*nota3

pesos = peso1 + peso2 + peso3

media = provas / pesos

print(f'A média final é de: {media}')
