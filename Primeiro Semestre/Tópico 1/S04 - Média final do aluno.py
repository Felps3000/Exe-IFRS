# Um professor resolveu utilizar quatro provas para testar o conhecimento dos alunos.
# Desenvolva um programa que solicite ao usuário que informe as quatro notas de um aluno
# - valores positivos que podem conter até duas casas decimais -
# e calcule a média final, apresentando esse resultado na tela.
# O cálculo utiliza a média aritmética, conforme determinado nos exemplos abaixo.

nota1 = float(input("Insira a primeira nota (0-10): "))
nota2 = float(input("Insira a segunda nota (0-10): "))
nota3 = float(input("Insira a terceira nota (0-10): "))
nota4 = float(input("Insira a quarta nota (0-10): "))

media = (nota1+nota2+nota3+nota4) / 4

print(f'A média é: {media: .2f}')
