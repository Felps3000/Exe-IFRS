#  Faça um programa para ler dois pares (quatro) valores que representam, respectivamente, duas datas compostas por
#  dia e mês. Considerando que as datas estão dentro do mesmo ano, mostrar as datas em ordem cronológica,
#  conforme apresentadas no exemplo abaixo:

dia1 = int(input("Insira o dia da primeira data: "))
mes1 = int(input("Insira o mês da primeira data: "))
dia2 = int(input("Insira o dia da segunda data: "))
mes2 = int(input("Insira o mês da segunda data: "))

if mes1 == mes2:
    if dia1 > dia2:
        print(f'{str(dia2).zfill(2)}/{str(mes2).zfill(2)} - {str(dia1).zfill(2)}/{str(mes1).zfill(2)}')
    else:
        print(f'{str(dia1).zfill(2)}/{str(mes1).zfill(2)} - {str(dia2).zfill(2)}/{str(mes2).zfill(2)}')

elif mes2 > mes1:
    print(f'{str(dia1).zfill(2)} / {str(mes1).zfill(2)} - {str(dia2).zfill(2)} / {str(mes2).zfill(2)}')
else:
    print(f'{str(dia2).zfill(2)} / {str(mes2).zfill(2)} - {str(dia1).zfill(2)} / {str(mes1).zfill(2)}')
