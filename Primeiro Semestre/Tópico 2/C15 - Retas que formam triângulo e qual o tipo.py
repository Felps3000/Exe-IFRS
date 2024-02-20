#  Desenvolva um programa que solicite ao usuário que informe três valores inteiros positivos, os quais representam
#  três segmentos de reta. Verifique se é possível compor um triângulo com esses segmentos e mostre uma mensagem com
#  o resultado, conforme determinado nos exemplos abaixo.

#  ENTRADA 	SAÍDA
#       3
#       4   escaleno
#       5
# - - - - - - - - - - - -
#       4
#       4   isósceles
#       2
# - - - - - - - - - - - -
#       1
#       1   equilátero
#       1
# - - - - - - - - - - - -
#      -3
#       0   inválido
#       5
# - - - - - - - - - - - -
#       3
#       1   não
#       5
# - - - - - - - - - - - -

a = int(input('Insira o primeiro valor inteiro da reta: '))
b = int(input('Insira o segundo valor inteiro da reta: '))
c = int(input('Insira o terceiro valor inteiro da reta: '))

if (a <= 0) or (b <= 0) or (c <= 0):
    print(f'inválido')

elif (a + b <= c) or (a + c <= b) or (b + c <= a):
    print(f'não')

elif (a == b) and (a == c):
    print(f'equilátero')

elif (a == b) or (a == c) or (b == c):
    print(f'isósceles')

elif a == b == c:
    print(f'equilátero')

else:
    print(f'escaleno')
