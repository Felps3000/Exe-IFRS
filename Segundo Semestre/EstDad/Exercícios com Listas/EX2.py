nadador = []
tempo = []
media = i = 0

while i <= 6:
    nadador.append(str(input("Insira o nome do nadador: ")))
    tempo.append(float(input("Insira o tempo do nadador: ")))
    media += tempo[i]
    i += 1

melhor = tempo.index(min(tempo))
pior = tempo.index(max(tempo))
media = media / 7

print(f"\nNadador com melhor tempo: {nadador[melhor]} com {min(tempo):.2f}s")
print(f"Nadador com pior tempo: {nadador[pior]} com {max(tempo):.2f}s")
print(f"Média de tempo dos nadadores: {media:.2f}s")
