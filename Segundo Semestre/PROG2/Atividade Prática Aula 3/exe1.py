class Empresa:
    nome = \
        cnpj = \
        endereco = \
        servico = \
        None


class Remedio:
    nome = \
        tarja = \
        valor = \
        laboratorio = \
        estoque = None


class Funcionario:
    nome = \
        sobrenome = \
        cpf = \
        salario = \
        cargo = None


class Livro:
    titulo = \
        isbn = \
        valor = \
        autor = \
        editora = \
        estoque = None


lista1 = [Empresa()]

print("Empresas")

lista1[0].nome = "Google"
lista1[0].cnpj = "00.000.000/0001-00"
lista1[0].endereco = "Av. dos Andradas 3000 - Belo Horizonte"
lista1[0].servico = "Pesquisa na web"

lista1.append(Empresa())
lista1[1].nome = "Microsoft"
lista1[1].cnpj = "11.111.111/0001-11"
lista1[1].endereco = "Av. dos Andradas 5000 - Belo Horizonte"
lista1[1].servico = "Software"

lista1.append(Empresa())
lista1[2].nome = "Sony"
lista1[2].cnpj = "22.222.222/0001-22"
lista1[2].endereco = "Av. dos Andradas 7000 - Belo Horizonte"
lista1[2].servico = "Jogos"

print(f"Nome: {lista1[0].nome}; "
      f"CNPJ: {lista1[0].cnpj}; "
      f"Endereço: {lista1[0].endereco}; "
      f"Serviço: {lista1[0].servico}")

print(f"Nome: {lista1[1].nome}; "
      f"CNPJ: {lista1[1].cnpj}; "
      f"Endereço: {lista1[1].endereco}; "
      f"Serviço: {lista1[1].servico}")

print(f"Nome: {lista1[2].nome}; "
      f"CNPJ: {lista1[2].cnpj}; "
      f"Endereço: {lista1[2].endereco}; "
      f"Serviço: {lista1[2].servico}")

print("\nRemédios")

lista2 = [Remedio()]

lista2[0].nome = "Escitalopram"
lista2[0].tarja = "Vermelha"
lista2[0].valor = "R$60,00"
lista2[0].laboratorio = "Medley"
lista2[0].estoque = "500"

lista2.append(Remedio())
lista2[1].nome = "Lexotan"
lista2[1].tarja = "Preta"
lista2[1].valor = "R$40,00"
lista2[1].laboratorio = "Roche"
lista2[1].estoque = "700"

lista2.append(Remedio())
lista2[2].nome = "Depakene"
lista2[2].tarja = "Vermelha"
lista2[2].valor = "R$20,00"
lista2[2].laboratorio = "Abbott"
lista2[2].estoque = "900"

print(f"Nome: {lista2[0].nome}; "
      f"Tarja: {lista2[0].tarja}; "
      f"Valor: {lista2[0].valor}; "
      f"Laboratório: {lista2[0].laboratorio}; "
      f"Estoque: {lista2[0].estoque}"
      )

print(f"Nome: {lista2[1].nome}; "
      f"Tarja: {lista2[1].tarja}; "
      f"Valor: {lista2[1].valor}; "
      f"Laboratório: {lista2[1].laboratorio}; "
      f"Estoque: {lista2[1].estoque}"
      )

print(f"Nome: {lista2[2].nome}; "
      f"Tarja: {lista2[2].tarja}; "
      f"Valor: {lista2[2].valor}; "
      f"Laboratório: {lista2[2].laboratorio}; "
      f"Estoque: {lista2[2].estoque}"
      )

print("\nFuncionários")

lista3 = [Funcionario()]

lista3[0].nome = "Filipe"
lista3[0].sobrenome = "Assis"
lista3[0].cpf = "000.000.000-00"
lista3[0].salario = "000.000.000-00"
lista3[0].cargo = "Carteiro"

lista3.append(Funcionario())
lista3[1].nome = "Lilo"
lista3[1].sobrenome = "Gonzales"
lista3[1].cpf = "111.111.111-11"
lista3[1].salario = "R$2.000,00"
lista3[1].cargo = "Professor"

lista3.append(Funcionario())
lista3[2].nome = "Jão"
lista3[2].sobrenome = "Silva"
lista3[2].cpf = "222.222.222-22"
lista3[2].salario = "R$10.000,00"
lista3[2].cargo = "Pedreiro"

print(f"Nome: {lista3[0].nome} "
      f"{lista3[0].sobrenome}; "
      f"CPF: {lista3[0].cpf}; "
      f"Salário: {lista3[0].salario}; "
      f"Cargo: {lista3[0].cargo}"
      )

print(f"Nome: {lista3[1].nome} "
      f"{lista3[1].sobrenome}; "
      f"CPF: {lista3[1].cpf}; "
      f"Salário: {lista3[1].salario}; "
      f"Cargo: {lista3[1].cargo}"
      )

print(f"Nome: {lista3[2].nome} "
      f"{lista3[2].sobrenome}; "
      f"CPF: {lista3[2].cpf}; "
      f"Salário: {lista3[2].salario}; "
      f"Cargo: {lista3[2].cargo}"
      )

print("\nLivros")

lista4 = [Livro()]

lista4[0].titulo = "Manifesto do Partido Comunista"
lista4[0].isbn = "9788585934231"
lista4[0].valor = "R$49,00"
lista4[0].autor = "Karl Marx & Friedrich Engels"
lista4[0].editora = "Boitempo"
lista4[0].estoque = "10.000"

lista4.append(Livro())
lista4[1].titulo = "O Estado e a Revolução"
lista4[1].isbn = "8587394991"
lista4[1].valor = "R$38,80"
lista4[1].autor = "Vladimir Lenin"
lista4[1].editora = "Expressão Popular"
lista4[1].estoque = "8.000"

lista4.append(Livro())
lista4[2].titulo = "O Livro Vermelho"
lista4[2].isbn = "8572325603"
lista4[2].valor = "R$28,90"
lista4[2].autor = "Mao Zedong"
lista4[2].editora = "Martin Claret"
lista4[2].estoque = "6.000"

print(f"Título: {lista4[0].titulo}; "
      f"ISBN: {lista4[0].isbn}; "
      f"Valor: {lista4[0].valor}; "
      f"Autor: {lista4[0].autor}; "
      f"Editora: {lista4[0].editora}; "
      f"Estoque: {lista4[0].estoque}; "
      )

print(f"Título: {lista4[1].titulo}; "
      f"ISBN: {lista4[1].isbn}; "
      f"Valor: {lista4[1].valor}; "
      f"Autor: {lista4[1].autor}; "
      f"Editora: {lista4[1].editora}; "
      f"Estoque: {lista4[1].estoque}; "
      )

print(f"Título: {lista4[2].titulo}; "
      f"ISBN: {lista4[2].isbn}; "
      f"Valor: {lista4[2].valor}; "
      f"Autor: {lista4[2].autor}; "
      f"Editora: {lista4[2].editora}; "
      f"Estoque: {lista4[2].estoque}; "
      )

