num1 = float(input())
num2 = float(input())

numC1 = (num2 * 0.01) * num1
numC2 = (num1 * 0.01) * num2

print(f"{num1}% de {num2} é {numC1:.2f}")
print(f"{num2}% de {num1} é {numC2:.2f}")
