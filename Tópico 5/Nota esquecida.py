nota = int(input("Insira a nota de uma prova: "))
media = int(input("Insira a média entre as duas notas das provas: "))

if (100 >= nota >= 0) and (100 >= media >= 0):
    print(2 * media - nota)
