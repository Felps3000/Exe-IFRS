import random
nomes = []

while True:
    nome = input(str("Insira um nome: "))
    nomes.append(nome)
    continuar = input("Deseja continuar? ")

    if continuar.upper() == "N":
        if len(nomes) < 2:
            print("Insira pelo menos mais um nome na lista!")
        else:
            break

random.shuffle(nomes)
vencedor = random.choice(nomes)

print(f"O vencedor da rifa foi {vencedor}!")
