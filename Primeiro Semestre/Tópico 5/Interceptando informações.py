entrada = int(input("Insira o valor do 1º bit: "))

c = 1
saida = True

while c < 8:
    entrada = int(input(f"Insira o valor do {c+1}º bit: "))
    c += 1
    if entrada == 9:
        saida = False

if saida:
        print("S")
else:
        print("F")

