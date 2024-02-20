num = int(input( ))

qtdfat = 0

while num > 0:
     fat = 1
     ant = 1
     while fat * ant < num:
          res = fat * ant
          ant = res
          fat += 1
     num = num - ant
     qtdfat += 1

print(qtdfat)