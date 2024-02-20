idadeM = int(input("Insira a idade da Dona Mônica: "))
idade1 = int(input("Insira a idade de um dos filhos: "))
idade2 = int(input("Insira a idade de outro filho: "))

idade3 = ((idade1 + idade2) - idadeM) * -1

if idade3 >= idade1 and idade3 >= idade2:
    print(idade3)

elif idade1 > idade2:
    print(idade1)

else:
    print(idade2)
