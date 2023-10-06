# Desenvolva um programa que avalia se um usuário tem condições financeiras para contratar um empréstimo
# para compra de um imóvel. O programa deve solicitar ao usuário o valor da casa,
# o salário mensal que recebe e qual o prazo em anos que pretende contratar o financiamento.
# Depois, deve calcular o valor da prestação mensal.
# No caso dessa prestação comprometer até 30% do salário do solicitante,
# o programa mostra o valor da prestação e, se ficar acima dos 30%, mostra a recusa do financiamento

valCasa = float(input("Insira o valor da casa: "))
salario = float(input("Insira o salário: "))
prazo = int(input("Insira o prazo (em anos) do financiamento: "))

valPrest = valCasa / (prazo * 12)

if valPrest <= salario * 0.3:
    print(f"{valPrest: .2f}")

else:
    print(f"Recusado")
