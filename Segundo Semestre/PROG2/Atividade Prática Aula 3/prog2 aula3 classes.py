class Pessoa:
    nome = sobrenome = idade = None


lista = [Pessoa()]

lista[0].nome = "Filipe"
lista[0].sobrenome = "Assis"
lista[0].idade = 32

lista.append(Pessoa())
lista[1].nome = "Gui"
lista[1].sobrenome = "Freitas"
lista[1].idade = 28

lista.append(Pessoa())
lista[2].nome = "Aline"
lista[2].sobrenome = "Luz"
lista[2].idade = 47

lista[3].append(Pessoa()).nome

'''
p1 = Pessoa()
p1.nome = "Filipe"
p1.sobrenome = "Assis"
p1.idade = 32

p2 = Pessoa()
p2.nome = "Gui"
p2.sobrenome = "Freitas"
p2.idade = 28

p3 = Pessoa()
p3.nome = "Aline"
p3.sobrenome = "Luz"
p3.idade = 47

p4 = Pessoa()
p4.nome = "Lilo"
p4.sobrenome = "Gonzales"
p4.idade = "29"
'''

print(f"Olá, {lista[0].nome} {lista[0].sobrenome}; {lista[0].idade}")

print(f"Olá, {lista[1].nome} {lista[1].sobrenome}; {lista[1].idade}")

print(f"Olá, {lista[2].nome} {lista[2].sobrenome}; {lista[2].idade}")

print(f"Olá, {lista[3].nome} {lista[3].sobrenome}; {lista[3].idade}")
