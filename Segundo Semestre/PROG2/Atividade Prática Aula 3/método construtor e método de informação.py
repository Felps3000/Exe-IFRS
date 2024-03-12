class Empresa:
    def __init__(self, nome, cnpj, endereco, servico):
        self.nome = nome
        self.cnpj = cnpj
        self.endereco = endereco
        self.servico = servico

    def info(self):
        print(f"Nome: {self.nome}; "
              f"CNPJ: {self.cnpj}; "
              f"Endereço: {self.endereco}; "
              f"Serviço: {self.servico}")


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

empresa1.info()
empresa2.info()
empresa3.info()


class Remedio:
    def __init__(self, nome, tarja, valor, laboratorio, estoque):
        self.nome = nome
        self.tarja = tarja
        self.valor = valor
        self.laboratorio = laboratorio
        self.estoque = estoque

    def info(self):
        print(f"Nome: {self.nome}; "
              f"Tarja: {self.tarja}; "
              f"Valor: {self.valor}; "
              f"Laboratório: {self.laboratorio}; "
              f"Estoque: {self.estoque}")


remedio1 = Remedio("Escitalopram",
                   "Vermelha",
                   "R$60,00",
                   "Medley",
                   "500")

remedio2 = Remedio("Lexotan",
                   "Preta",
                   "R$40,00",
                   "Roche",
                   "700")

remedio3 = Remedio("Depakene",
                   "Vermelha",
                   "R$20,00",
                   "Abbott",
                   "900")

print("\nRemédios")

remedio1.info()
remedio2.info()
remedio3.info()


class Funcionario:
    def __init__(self, nome, sobrenome, cpf, salario, cargo):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.salario = salario
        self.cargo = cargo

    def info(self):
        print(f"Nome: {self.nome} "
              f"{self.sobrenome}; "
              f"CPF: {self.cpf}; "
              f"Salário: {self.salario}; "
              f"Cargo: {self.cargo}")


funcionario1 = Funcionario("Filipe",
                           "Assis",
                           "000.000.000-00",
                           "R$3.000,00",
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

funcionario1.info()
funcionario2.info()
funcionario3.info()


class Livro:
    def __init__(self, titulo, isbn, valor, autor, editora, estoque):
        self.titulo = titulo
        self.isbn = isbn
        self.valor = valor
        self.autor = autor
        self.editora = editora
        self.estoque = estoque

    def info(self):
        print(f"Título: {self.titulo}; "
              f"ISBN: {self.isbn}; "
              f"Valor: {self.valor}; "
              f"Autor: {self.autor}; "
              f"Editora: {self.editora}; "
              f"Estoque: {self.estoque}")


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

livro1.info()
livro2.info()
livro3.info()
