pa = [int(input("Insira o primeiro termo da PA: ")),  # índice 0
      int(input("Insira a quantidade de termos da PA: ")),  # índice 1
      int(input("Insira a razão da PA: "))]  # índice 2

lista = [pa[0]]  # inicializa a lista com o primeiro termo da PA
i = 1

while i < pa[1]:  # roda o loop enquanto o contador for menor que o número de termos
    lista.append(lista[-1] + pa[2])  # acrescenta o termo a partir da soma do último item da lista com a razão da PA
    i += 1

#  .join() é uma função da string que concatena elementos iteráveis
#  map() e str() transforma todos itens da lista em strings
print(f"\nTermos:", ", ".join(map(str, lista)))
print(f"Soma dos termos: {sum(lista)}")
