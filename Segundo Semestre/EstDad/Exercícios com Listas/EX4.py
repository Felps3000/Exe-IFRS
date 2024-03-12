import math
lista = []

try:
    quantidade = int(input("Insira um valor ímpar e maior que 1: "))
    if quantidade <= 1 or quantidade % 2 == 0:
        print("Valor inválido")
    else:
        for i in range(quantidade):
            lista.append((int(input("Insira o número: "))))
        central = lista[len(lista) // 2]
        print(f"O elemento central da lista é {central}")
        print(f"Seu fatorial é {math.factorial(central)}")

except ValueError:
    print("Valor inválido")
