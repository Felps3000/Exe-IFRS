# Desenvolva um programa que solicite ao usuário que informe três valores positivos
# com até uma casa decimal que representam as três notas obtidas pelo estudante nas avaliações.
# Calcule a média final desse aluno, sabendo que para o cálculo são atribuídos os pesos 1, 2 e 3 para cada nota,
# respectivamente (média ponderada!). O resultado do estudante é atribuído pela tabela abaixo:
#      Média        Resultado
#     M < 4.0       Reprovado
# 4.0 <= M < 7.0	Em Exame
#     M > 7.0     	Aprovado

nota1 = float(input("Insira a nota da primeira prova: "))
nota2 = float(input("Insira a nota da segunda prova: "))
nota3 = float(input("Insira a nota da terceira prova: "))

provas = nota1 + 2 * nota2 + 3 * nota3

media = provas / 6

if media < 4.0:
    print(f"{media: .2f} Reprovado")

elif media == 4.0 or media < 7.0:
    print(f"{media: .2f} Em Exame")

else:
    print(f"{media: .2f} Aprovado")
