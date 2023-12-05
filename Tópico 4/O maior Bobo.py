# O Reino dos Emparelhamentos é governado por um generoso Comendador. A fama do Comendador e de suas grandes qualidades
# é conhecida por todos, inclusive em reinos vizinhos. Uma de suas mais famosas qualidades é seu bom humor,
# que é nutrido diariamente por um bobo da corte, eleito anualmente no Grande Concurso de Comédia (GCC) do reino.
# O bobo da corte ajuda a aliviar as tensões das diversas reuniões políticas que o cargo exige,
# alegrando não só o Comendador como também a totalidade do reino.
#  O jovem Carlos é um grande comediante cujo sonho é se tornar bobo da corte na próxima temporada.
# Ele passou os últimos meses anotando piadas e trocadilhos dos mais diversos tipos, muitos dos quais sobre sua
# própria (diminuta) estatura. Chegou a época da eleição do bobo da corte, e um total de N candidatos se inscreveram.
# Cada um dos candidatos terá cinco minutos para se apresentar perante uma plateia. Após as apresentações,
# cada cidadão do Reino dos Emparelhamentos poderá votar em um dos candidatos,
# e o mais votado será o novo bobo da corte. Caso haja empate entre um ou mais candidatos,
# aquele que tiver feito a inscrição primeiro é eleito. Sabendo disso, o jovem Carlos passou noites na
# frente do escritório eleitoral e garantiu que sua inscrição fosse a primeira a ser feita.
# Após a votação, resta apenas apurar os resultados. A urna eletrônica gera um relatório com N inteiros, correspondentes
# ao número de votos de cada candidato, ordenados pela ordem de inscrição.
# Sua missão é determinar se o jovem Carlos foi eleito ou não.
#
# Entrada:
# A primeira linha da entrada contém um inteiro N(Que significa p número de participantes do concurso),
# satisfazendo 2 ≤ N ≤ 104. As N linhas seguintes conterão N inteiros positivos v1, . . . , vN , um em cada linha,
# correspondentes ao número de votos recebido por cada um dos candidatos,
# em ordem de inscrição(Lembrando que a primeira inscrição é de Carlos).
# Como a população do Reino dos Emparelhamentos é de 100.000 pessoas,
# o número total de votos não será superior a este valor.
#
# Saída:
# Seu programa deve produzir uma única linha contendo o caractere ‘S’ caso o jovem Carlos seja eleito bobo da corte,
# ou o caractere ‘N’ caso contrário.

p = int(input("Insira o número de participantes: "))  # número de participantes
r = int(input("Insira o número de votos do 1º participante: "))  # reserva do número de votos do Carlos
c = 1  # contador do loop
v = 0  # número de votos
m = 0  # maior número de votos inserido

while c < p:  # roda o loop enquanto o contador [c] for menor que o número de participantes [p]
    v = int(input(f"Insira o número de votos do {c+1}º participante: "))
    if v > r:  # checa o número de votos [v] é maior que o número de votos do Carlos [r]
        m = v  # caso seja define [v] como o maior número de votos [m]
    c += 1  # incrementa o contador

print(f"Carlos é o vencedor?", end=" ")

if m > r:  # checa se após o loop o maior número inserido [m] é maior que o número de votos do Carlos [r]
    print("Não!")

else:
    print("sim!")
