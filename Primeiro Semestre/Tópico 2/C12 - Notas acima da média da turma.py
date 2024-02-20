# Construa um programa para ler quatro valores inteiros que representam as notas dos alunos de uma turma.
# Calcular a média entre essas notas. Depois, verificar e mostrar todas as notas com valor acima dessa média,
# conforme determinado nos exemplos abaixo. (Obs.: utilize somente estruturas de seleção)

nota1 = int(input("Insira a nota do primeiro aluno: "))
nota2 = int(input("Insira a nota do segundo aluno: "))
nota3 = int(input("Insira a nota do terceiro aluno: "))
nota4 = int(input("Insira a nota do quarto aluno: "))

qtd = 0

if nota1 > 0:
    qtd += 1

if nota2 > 0:
    qtd += 1

if nota3 > 0:
    qtd += 1

if nota4 > 0:
    qtd += 1

media = (nota1 + nota2 + nota3 + nota4) / qtd

if nota1 > media:
    print(nota1)
if nota2 > media:
    print(nota2)
if nota3 > media:
    print(nota3)
if nota4 > media:
    print(nota4)
