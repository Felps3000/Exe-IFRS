# O novo jogo, com partidas que podem durar até um dia inteiro
# ( máximo de 24 horas, quando inicia num dia e termina no próximo)]
# se transformou num sucesso entre os alunos.
# Mas resolveram que é necessário registrar um pouco melhor o tempo de duração:
# com horas e minutos.
# Desenvolva um programa que solicite ao usuário que informe quatro valores inteiros,
# os quais representam, respectivamente, a hora e minuto de início,
# e a hora e minuto de finalização de uma partida.
# Calcule o tempo de duração da partida e mostre uma mensagem com o resultado

startHour = int(input("Insira a hora de início: "))
startMin = int(input("Insira o minuto do início: "))

endHour = int(input("Insira a hora do final: "))
endMin = int(input("Insira o minuto do final: "))

horas = [startHour, endHour]
minutos = [startMin, endMin]

if any((val < 0 or val > 24 for val in horas)) or any((val < 0 or val > 59 for val in minutos)):
    print("-")

totalHora = endHour - startHour
totalMinutos = endMin - startMin

if totalMinutos < 0:
    totalMinutos += 60
    totalHora -= 1

if (totalHora < 0) or (totalHora == 0 and totalMinutos == 0):
    totalHora += 24

print(f"{str(totalHora).zfill(2)}:{str(totalMinutos).zfill(2)}")
