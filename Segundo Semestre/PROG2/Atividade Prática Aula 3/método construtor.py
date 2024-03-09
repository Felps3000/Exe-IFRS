class Empresa:
    def __init__(self, nome, cnpj, endereco, servico):
        self.nome = nome
        self.cnpj = cnpj
        self.endereco = endereco
        self.servico = servico


empresa1 = Empresa("Google",
                   "00.000.000/0001-00",
                   "Av. dos Andradas 3000 - Belo Horizonte",
                   "Pesquisa na web")

empresa2 = Empresa("Microsoft",
                   "11.111.111/0001-11",
                   "Av. dos Andradas 5000 - Belo Horizonte",
                   "Software")

empresa3 = Empresa("Sony",
                   "22.222.222/0001-22",
                   "Av. dos Andradas 7000 - Belo Horizonte",
                   "Jogos")

print("Empresas")
print(f"Nome: {empresa1.nome}; "
      f"CNPJ: {empresa1.cnpj}; "
      f"Endereço: {empresa1.endereco}; "
      f"Serviço: {empresa1.servico}")

print(f"Nome: {empresa2.nome}; "
      f"CNPJ: {empresa2.cnpj}; "
      f"Endereço: {empresa2.endereco}; "
      f"Serviço: {empresa2.servico}")

print(f"Nome: {empresa3.nome}; "
      f"CNPJ: {empresa3.cnpj}; "
      f"Endereço: {empresa3.endereco}; "
      f"Serviço: {empresa3.servico}")


class Remedio:
    def __init__(self, nome, tarja, valor, laboratorio, estoque):
        self.nome = nome
        self.tarja = tarja
        self.valor = valor
        self.laboratorio = laboratorio
        self.estoque = estoque


remedio1 = Remedio("Escitalopram",
                   "Vermelha",
                   "R$60,00",
                   "Medley",
                   500)

remedio2 = Remedio("Lexotan",
                   "Preta",
                   "R$40,00",
                   "Roche",
                   700)

remedio3 = Remedio("Depakene",
                   "Vermelha",
                   "R$20,00",
                   "Abbott",
                   900)

print("\nRemédios")
print(f"Nome: {remedio1.nome}; "
      f"Tarja: {remedio1.tarja}; "
      f"Valor: {remedio1.valor}; "
      f"Laboratório: {remedio1.laboratorio}; "
      f"Estoque: {remedio1.estoque}")

print(f"Nome: {remedio2.nome}; "
      f"Tarja: {remedio2.tarja}; "
      f"Valor: {remedio2.valor}; "
      f"Laboratório: {remedio2.laboratorio}; "
      f"Estoque: {remedio2.estoque}")

print(f"Nome: {remedio3.nome}; "
      f"Tarja: {remedio3.tarja}; "
      f"Valor: {remedio3.valor}; "
      f"Laboratório: {remedio3.laboratorio}; "
      f"Estoque: {remedio3.estoque}")


class Funcionario:
    def __init__(self, nome, sobrenome, cpf, salario, cargo):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.salario = salario
        self.cargo = cargo


funcionario1 = Funcionario("Filipe",
                           "Assis",
                           "000.000.000-00",
                           "000.000.000-00",
                           "Carteiro")

funcionario2 = Funcionario("Lilo",
                           "Gonzales",
                           "111.111.111-11",
                           "R$2.000,00",
                           "Professor")

funcionario3 = Funcionario("Jão",
                           "Silva",
                           "222.222.222-22",
                           "R$10.000,00",
                           "Pedreiro")

print("\nFuncionários")
print(f"Nome: {funcionario1.nome} "
      f"{funcionario1.sobrenome}; "
      f"CPF: {funcionario1.cpf}; "
      f"Salário: {funcionario1.salario}; "
      f"Cargo: {funcionario1.cargo}")

print(f"Nome: {funcionario2.nome} "
      f"{funcionario2.sobrenome}; "
      f"CPF: {funcionario2.cpf}; "
      f"Salário: {funcionario2.salario}; "
      f"Cargo: {funcionario2.cargo}")

print(f"Nome: {funcionario3.nome} "
      f"{funcionario3.sobrenome}; "
      f"CPF: {funcionario3.cpf}; "
      f"Salário: {funcionario3.salario}; "
      f"Cargo: {funcionario3.cargo}")


class Livro:
    def __init__(self, titulo, isbn, valor, autor, editora, estoque):
        self.titulo = titulo
        self.isbn = isbn
        self.valor = valor
        self.autor = autor
        self.editora = editora
        self.estoque = estoque


livro1 = Livro("Manifesto do Partido Comunista",
               9788585934231,
               "R$49,00",
               "Karl Marx & Friedrich Engels",
               "Boitempo",
               "10.000")

livro2 = Livro("O Estado e a Revolução",
               8587394991,
               "R$38,80",
               "Vladimir Lenin",
               "Expressão Popular",
               "8.000")

livro3 = Livro("O Livro Vermelho",
               8572325603,
               "R$28,90",
               "Mao Zedong",
               "Martin Claret",
               "6.000")

print("\nLivros")
print(f"Título: {livro1.titulo}; "
      f"ISBN: {livro1.isbn}; "
      f"Valor: {livro1.valor}; "
      f"Autor: {livro1.autor}; "
      f"Editora: {livro1.editora}; "
      f"Estoque: {livro1.estoque}")

print(f"Título: {livro2.titulo}; "
      f"ISBN: {livro2.isbn}; "
      f"Valor: {livro2.valor}; "
      f"Autor: {livro2.autor}; "
      f"Editora: {livro2.editora}; "
      f"Estoque: {livro2.estoque}")

print(f"Título: {livro3.titulo}; "
      f"ISBN: {livro3.isbn}; "
      f"Valor: {livro3.valor}; "
      f"Autor: {livro3.autor}; "
      f"Editora: {livro3.editora}; "
      f"Estoque: {livro3.estoque}")
