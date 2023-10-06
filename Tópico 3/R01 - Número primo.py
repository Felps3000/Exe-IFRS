numero = int(input("Informe o número: "))

d = 1 # incrementa o divisor pra checar se é divisível
q = 0 # quantidade de vezes que o resto da divisão foi zero

while d <= numero: # checa todos números abaixo do input
    r = numero % d # testa se o input resta zero
    d += 1 # testa o próximo número
    if r == 0: # se o resto é igual a zero...
        q += 1 # ...incrementa a quantidade de divisores

if q == 2: # se o divisor for igual a 2, o número é primo
    print(f"Sim, o número {numero} é primo!")

else:
    print(f"Não, o número {numero} não é primo!")