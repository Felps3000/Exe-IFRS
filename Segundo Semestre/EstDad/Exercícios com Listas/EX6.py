import math
import random

lista = []
tamanho = int(input("Insira a quantidade de itens na lista: "))

if tamanho > 1:
    for x in range(tamanho):
        lista.append(random.randint(1, tamanho))
    multi = math.prod(lista)
    media = multi ** (1 / tamanho)
    print(f"A lista ", ", ".join(map(str, lista)), end=" ")
    print(f"tem o seu produto de {multi} e retornou a média geométrica de {media:.2f}")

else:
    print("Insira um valor maior que 1!")
