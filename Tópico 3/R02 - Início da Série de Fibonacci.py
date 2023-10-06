# A Série de Fibonacci é uma sequencia de valores onde cada elemento é o resultado da soma dos seus dois antecessores,
# considerando que os dois primeiros elementos são 0 e 1.
# Construa um programa que, a partir de uma estratégia que usa repetições,
# gere os primeiros dez elementos da Série de Fibonacci e apresenta uma mensagem informando o resultado,
# conforme determinado nos exemplos abaixo.
# SAÍDA: 0  1  1  2  3  5  8  13  21  34

termo1 = 1
termo2 = 1

fib = 0

if fib == 0:
    print(f"{fib}", end=" ")
else:
    while fib <= 34:
        fib = termo2 + termo1
        termo1 = termo2
        termo2 = termo1

        print(f"{fib}", end=" ")