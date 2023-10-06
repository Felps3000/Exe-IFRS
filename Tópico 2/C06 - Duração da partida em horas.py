# Os alunos criaram um novo jogo, com partidas que podem durar até um dia inteiro
# ( máximo de 24 horas, quando inicia num dia e termina no próximo).
# Desenvolva um programa que solicite ao usuário que informe dois valores inteiros (hora cheia),
# os quais representam, respectivamente, a hora de início e a hora de finalização de uma partida.
# Calcule o tempo de duração da partida e mostre uma mensagem com o resultado

start = int(input("Insira a hora do início: "))
end = int(input("Insira a hora do final: "))

horas = [start, end]

if any(val < 0 or val > 24 for val in horas):
    print("-")

elif end > start:
    print(end - start)

else:
    print(f"\nA partida durou {24 - start + end} hora(s)")

